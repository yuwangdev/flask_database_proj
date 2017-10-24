import logging

import operator

import datetime

from src.dao.Resource_DAO import Resource_DAO
from src.dao.Incident_DAO import Incident_DAO
from math import sin, cos, atan2, sqrt, radians
from src.dao.User_DAO import User_DAO
from src.dao.ResourceRequest_DAO import ResourceRequest_DAO
from src.dao.RepairResource_DAO import RepairResource_DAO

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Search_Result_DataService():
    #########################################################################
    # if no incident selected, ignore distance calculation and return all resources
    #########################################################################

    def __init__(self):
        logging.debug("start the Search_Result_DataService()")
        self.res_dao = Resource_DAO()
        self.inci_dao = Incident_DAO()
        self.user_dao = User_DAO()
        self.res_request_dao = ResourceRequest_DAO()
        self.repair_resource_dao = RepairResource_DAO()
        self.incidentEntry = ""
        self.username = ""

    def get_incident_position(self, incident_entry):
        '''
        @rtype: list
        '''

        assert isinstance(incident_entry, str)

        temp = incident_entry[incident_entry.index("(") + 1:incident_entry.index(")")]

        logging.debug("incident id is " + str(temp))

        return self.inci_dao.get_incident_position_by_incidentId(int(temp))

    def get_esf_id(self, esf_entry):
        '''
        @rtype: int
        '''

        assert isinstance(esf_entry, str)

        temp = esf_entry[:esf_entry.index("#")]

        logging.debug("esf id is " + str(temp))

        return int(temp)

    def get_resourceId_searched_by_esf(self, esfEntry):
        '''
        @rtype: list
        '''
        ### includes the resoruce table, cap table, and esf table
        assert isinstance(esfEntry, str)

        srd = Search_Result_DataService()
        esf_id = srd.get_esf_id(esfEntry)

        from_primary = list()
        from_additional = list()

        from_primary = self.res_dao.get_resource_lists_by_primary_esf(esf_id)
        from_additional = self.res_dao.get_resource_lists_by_additional_esf(esf_id)

        logging.debug(from_primary)
        logging.debug(from_additional)

        temp_set = set(from_primary + from_additional)

        return list(temp_set)

    def get_resourceId_searched_by_keyword(self, keyword):
        '''
        @rtype: list
        '''

        ### includes the resoruce table, cap table, and esf table
        assert isinstance(keyword, str)

        from_res = list()
        from_cap = list()
        from_esf = list()
        from_res = self.res_dao.get_resourceId_lists_by_keyword_model_or_name(keyword)
        from_cap = self.res_dao.get_resource_lists_by_keyword_capabilities(keyword)
        from_esf = self.res_dao.get_resource_lists_by_keyword_esf(keyword)
        logging.debug(from_res)
        logging.debug(from_cap)
        logging.debug(from_esf)

        temp_set = set(from_esf + from_res + from_cap)

        return list(temp_set)

    def get_distance_between_res_inci(self, inci_lat, inci_long, resoruceId):
        '''
        @rtype: float
        '''
        assert isinstance(inci_lat, float)
        assert isinstance(inci_long, float)
        assert isinstance(resoruceId, int)

        res_pos = self.res_dao.get_resource_position_by_resourceId(resoruceId)

        if len(res_pos) == 0:
            return 0.0

        res_lat = res_pos[0]
        res_long = res_pos[1]

        delta_lat = radians(res_lat) - radians(inci_lat)
        delta_long = radians(res_long) - radians(inci_long)
        a = sin(delta_lat / 2) ** 2 + cos(radians(inci_lat)) * cos(radians(res_lat)) * sin(delta_long / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return 6371 * c

    def get_resIdDict_within_distance(self, incident_entry, distance, res_id_lists):
        '''
        @rtype: dict
        '''

        assert isinstance(res_id_lists, list)
        assert isinstance(incident_entry, str)

        srd = Search_Result_DataService()
        inci_lat = srd.get_incident_position(incident_entry)[0]
        inci_long = srd.get_incident_position(incident_entry)[1]

        result = dict()

        for id in res_id_lists:
            dist = srd.get_distance_between_res_inci(inci_lat, inci_long, id)
            if dist <= distance:
                result[id] = dist

        sorted_result = sorted(result.items(), key=operator.itemgetter(0))

        return dict(sorted_result)

    def populate_table_data(self, keyword, esfEntry, location_distance,
                            incidenEntry):
        '''
        @rtype: dict
        '''

        assert isinstance(keyword, str)
        assert isinstance(incidenEntry, str)
        assert isinstance(esfEntry, str)
        assert isinstance(location_distance, int)

        srd = Search_Result_DataService()
        table_lists = list()

        if keyword != "" and esfEntry != "" and incidenEntry != "":

            self.incidentEntry = incidenEntry

            temp1 = srd.get_resourceId_searched_by_keyword(keyword)
            temp2 = srd.get_resourceId_searched_by_esf(esfEntry)

            tempset = set(temp1 + temp2)

            resource_id_list = list(tempset)
            resource_id_distance_dict = srd.get_resIdDict_within_distance(incidenEntry, location_distance,
                                                                          resource_id_list)

            logging.debug("final resourceid-distance mapping")
            logging.debug(resource_id_distance_dict)

            for k, v in resource_id_distance_dict.iteritems():
                temp_list = list()
                temp_list.append(k)
                temp_list.append(v)
                logging.debug(self.res_dao.get_resource_owner_by_resourceId(k))
                temp_list.append(
                        self.user_dao.get_nameinfo_by_username(self.res_dao.get_resource_owner_by_resourceId(k)))
                temp_list.append(self.res_dao.get_resource_costtext_by_resourceId(k))
                temp_status = self.res_dao.get_resource_status_by_resourceId(k)
                temp_list.append(temp_status)
                if temp_status == "available":
                    temp_list.append("now")

                if temp_status == "not available":
                    temp_list.append(self.res_request_dao.get_expectedreturndate_by_resourceId(k))

                if temp_status == "in repair":
                    temp_list.append(self.repair_resource_dao.get_enddate_by_resourceId(k))

                table_lists.append(temp_list)

        if keyword == "" and esfEntry != "" and incidenEntry != "":

            self.incidentEntry = incidenEntry

            temp2 = srd.get_resourceId_searched_by_esf(esfEntry)

            tempset = set(temp2)

            resource_id_list = list(tempset)
            resource_id_distance_dict = srd.get_resIdDict_within_distance(incidenEntry, location_distance,
                                                                          resource_id_list)

            logging.debug("final resourceid-distance mapping")
            logging.debug(resource_id_distance_dict)

            for k, v in resource_id_distance_dict.iteritems():
                temp_list = list()
                temp_list.append(k)
                temp_list.append(v)
                logging.debug(self.res_dao.get_resource_owner_by_resourceId(k))
                temp_list.append(
                        self.user_dao.get_nameinfo_by_username(self.res_dao.get_resource_owner_by_resourceId(k)))
                temp_list.append(self.res_dao.get_resource_costtext_by_resourceId(k))
                temp_status = self.res_dao.get_resource_status_by_resourceId(k)
                temp_list.append(temp_status)
                if temp_status == "available":
                    temp_list.append("now")
                if temp_status == "not available":
                    temp_list.append(self.res_request_dao.get_expectedreturndate_by_resourceId(k))

                if temp_status == "in repair":
                    temp_list.append(self.repair_resource_dao.get_enddate_by_resourceId(k))

                table_lists.append(temp_list)

        if keyword == "" and esfEntry == "" and incidenEntry != "":

            self.incidentEntry = incidenEntry

            resource_id_list = list(self.res_dao.get_all_resource_id())
            resource_id_distance_dict = srd.get_resIdDict_within_distance(incidenEntry, location_distance,
                                                                          resource_id_list)

            logging.debug("final resourceid-distance mapping")
            logging.debug(resource_id_distance_dict)

            for k, v in resource_id_distance_dict.iteritems():
                temp_list = list()
                temp_list.append(k)
                temp_list.append(v)
                logging.debug(self.res_dao.get_resource_owner_by_resourceId(k))
                temp_list.append(
                        self.user_dao.get_nameinfo_by_username(self.res_dao.get_resource_owner_by_resourceId(k)))
                temp_list.append(self.res_dao.get_resource_costtext_by_resourceId(k))
                temp_status = self.res_dao.get_resource_status_by_resourceId(k)
                temp_list.append(temp_status)
                if temp_status == "available":
                    temp_list.append("now")
                if temp_status == "not available":
                    temp_list.append(self.res_request_dao.get_expectedreturndate_by_resourceId(k))

                if temp_status == "in repair":
                    temp_list.append(self.repair_resource_dao.get_enddate_by_resourceId(k))

                table_lists.append(temp_list)

        if keyword == "" and esfEntry == "" and incidenEntry == "":

            resource_id_list = list(self.res_dao.get_all_resource_id())

            logging.debug("final resourceid-distance mapping")

            for k in resource_id_list:
                temp_list = list()
                temp_list.append(k)
                temp_list.append("N.A.")
                logging.debug(self.res_dao.get_resource_owner_by_resourceId(k))
                temp_list.append(
                        self.user_dao.get_nameinfo_by_username(self.res_dao.get_resource_owner_by_resourceId(k)))
                temp_list.append(self.res_dao.get_resource_costtext_by_resourceId(k))
                temp_status = self.res_dao.get_resource_status_by_resourceId(k)
                temp_list.append(temp_status)
                if temp_status == "available":
                    temp_list.append("now")
                if temp_status == "not available":
                    temp_list.append(self.res_request_dao.get_expectedreturndate_by_resourceId(k))

                if temp_status == "in repair":
                    temp_list.append(self.repair_resource_dao.get_enddate_by_resourceId(k))

                table_lists.append(temp_list)

        return table_lists

    def populate_action_lists(self, table_data_lists, username):
        '''
        @rtype: list
        '''

        assert isinstance(table_data_lists, list)
        assert isinstance(username, str)

        result = list()

        for row in table_data_lists:
            currentStatus = row[4]
            logging.debug(currentStatus)

            owner = str(self.res_dao.get_resource_owner_by_resourceId(int(row[0])))

            if currentStatus == "in repair" and owner != username:
                temp = list()
                result.append(temp)

            if currentStatus == "not available":
                temp = list()
                temp.append("request")
                result.append(temp)

            if currentStatus == "available" and owner != username:
                temp = list()
                temp.append("request")
                result.append(temp)

            if currentStatus == "available" and owner == username:
                temp = list()

                startdate_repair = self.repair_resource_dao.get_startdate_by_resourceId(int(row[0]))

                currentDate = str(datetime.datetime.today().date())

                print currentDate
                print startdate_repair

                if startdate_repair == "":
                    sd = datetime.datetime.strptime(currentDate, "%Y-%m-%d")
                    cd = datetime.datetime.strptime(currentDate, "%Y-%m-%d")
                else:
                    sd = datetime.datetime.strptime(startdate_repair, "%Y-%m-%d")
                    cd = datetime.datetime.strptime(currentDate, "%Y-%m-%d")

                print sd

                print cd

                if sd < cd:
                    temp.append("cancel repair")
                else:
                    if self.incidentEntry != "":

                        temp.append("deploy")
                        temp.append("repair")
                    else:
                        temp.append("repair")

                result.append(temp)

            if self.incidentEntry == "" and owner != username:
                temp = list()
                result.append(temp)

        return result
