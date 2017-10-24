import logging

from db_utils import run_sql_string_statement
from src.dao.ESF_DAO import ESF_DAO

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
STATUS = ["available", "not available", "in repair"]


class Resource_DAO:
    def __init__(self):

        logging.info("construct the Resource_DAO class")

    @classmethod
    def insert_resource(self, ResourceID, ResourceName, model, CurrentStatus, Latitude, Longitude, Owner, CostPerValue,
                        EsfID, CostUnit, CurrentUser, StartDate, DueDate):
        '''
        @rtype: bool
        '''
        ####################################################################
        # the EsfID in the argument is for the primary ESF
        # additional ESFIDs are inserted into the Additional table
        # above parts will be centrally implemented in the Add_Resource_DataService class
        ####################################################################



        assert isinstance(ResourceID, int)
        assert isinstance(ResourceName, str)
        assert isinstance(model, str)
        assert isinstance(CurrentStatus, str)
        assert isinstance(Latitude, float)
        assert isinstance(Longitude, float)
        assert isinstance(Owner, str)
        assert isinstance(CostPerValue, float)
        assert isinstance(EsfID, int)
        assert isinstance(CostUnit, str)
        assert isinstance(CurrentUser, str)
        assert isinstance(StartDate, str)
        assert isinstance(DueDate, str)

        if CurrentStatus not in STATUS:
            raise ValueError("current status should be in the list of available, not available, in repair")

        sql_statement = "insert Resource values({0}, '{1}', '{2}', '{3}', {4}, {5}, '{6}', {7}, {8}, '{9}', '{10}', '{11}', '{12}');"
        sql_statement = sql_statement.format(str(ResourceID), ResourceName, model, CurrentStatus, str(Latitude),
                                             str(Longitude), Owner,
                                             str(CostPerValue), str(EsfID), CostUnit, CurrentUser, StartDate, DueDate)

        result = run_sql_string_statement(sql_statement)

        return len(result) == 0

    @classmethod
    def get_resource_record_by_resourceId(self, resourceId):
        '''
        @rtype: list
        '''

        assert isinstance(resourceId, int)
        sql_statement = "select * from Resource where Resource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resourceId))
        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        for row in result:
            tmp = list()
            for col in row:
                tmp.append(col)
            rsp.append(tmp)

        return rsp

    @classmethod
    def get_resource_record_by_owner(self, owner):
        '''
        @rtype: list
        '''

        assert isinstance(owner, str)
        sql_statement = "select * from Resource where Resource.Owner='{0}';"
        sql_statement = sql_statement.format(owner)
        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        for row in result:
            tmp = list()
            for col in row:
                tmp.append(col)
            rsp.append(tmp)

        return rsp

    @classmethod
    def get_all_resource(self):
        '''
        @rtype: list
        '''

        sql_statement = "select * from Resource;"

        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        for row in result:
            tmp = list()
            for col in row:
                tmp.append(col)
            rsp.append(tmp)

        return rsp

    @classmethod
    def get_count_as_int(self):
        '''
        @rtype: int
        '''

        sql_statement = "select count(*) from Resource;"

        result = run_sql_string_statement(sql_statement)

        return int(result[0][0])

    def get_resourceId_lists_by_keyword_model_or_name(self, keyword):
        '''
        @rtype: list
        '''
        assert isinstance(keyword, str)

        sql_statement = "select ResourceID from Resource where Resource.ResourceName like lower('%{0}%') or Resource.model like lower('%{1}%');"

        sql_statement = sql_statement.format(keyword, keyword)
        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        for row in result:
            rsp.append(int(row[0]))

        return rsp

    def get_resource_lists_by_keyword_capabilities(self, keyword):
        '''
        @rtype: list
        '''
        assert isinstance(keyword, str)

        sql_statement = "select Capability.ResourceID from Capability where CapabilitiyStr like lower('%{0}%');"

        sql_statement = sql_statement.format(keyword)
        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        for row in result:
            rsp.append(int(row[0]))

        return rsp

        return rsp

    def get_resource_lists_by_keyword_esf(self, keyword):
        '''
        @rtype: list
        '''
        assert isinstance(keyword, str)

        sql_statement = "select Resource.ResourceID from Resource where Resource.EsfID in (select ESF.EsfID from ESF where ESF.item like lower('%{0}%'));"

        sql_statement = sql_statement.format(keyword)
        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        for row in result:
            rsp.append(int(row[0]))

        return rsp

    @classmethod
    def get_resource_position_by_resourceId(self, resId):
        '''
        @rtype: list
        '''

        assert isinstance(resId, int)
        sql_statement = "select Resource.Latitude, Resource.Longitude from Resource where Resource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resId))
        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        rsp.append(result[0][0])
        rsp.append(result[0][1])

        return rsp

    def get_resource_lists_by_primary_esf(self, esf_id):
        '''
        @rtype: list
        '''
        assert isinstance(esf_id, int)

        sql_statement = "select Resource.ResourceID from Resource where Resource.EsfID={0};"

        sql_statement = sql_statement.format(esf_id)
        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        for row in result:
            rsp.append(int(row[0]))

        return rsp

    def get_resource_lists_by_additional_esf(self, esf_id):
        '''
        @rtype: list
        '''
        assert isinstance(esf_id, int)

        sql_statement = "select Additional.ResourceID from Additional where Additional.EsfID={0};"

        sql_statement = sql_statement.format(esf_id)
        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        for row in result:
            rsp.append(int(row[0]))

        return rsp

    @classmethod
    def get_resource_costtext_by_resourceId(self, resId):
        '''
        @rtype: str
        '''

        assert isinstance(resId, int)
        sql_statement = "select Resource.CostUnit, Resource.CostPerValue from Resource where Resource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resId))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        value = result[0][1]
        unit = result[0][0]

        return str(value) + "/" + str(unit)

    @classmethod
    def get_resource_owner_by_resourceId(self, resId):
        '''
        @rtype: str
        '''

        assert isinstance(resId, int)
        sql_statement = "select Resource.Owner from Resource where Resource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resId))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return result[0][0]

    @classmethod
    def get_resource_status_by_resourceId(self, resId):
        '''
        @rtype: str
        '''

        assert isinstance(resId, int)
        sql_statement = "select Resource.CurrentStatus from Resource where Resource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resId))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return result[0][0]

    @classmethod
    def get_all_resource_id(self):
        '''
        @rtype: list
        '''

        sql_statement = "select Resource.ResourceID from Resource;"

        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        rsp = list()
        for row in result:
            rsp.append(int(row[0]))

        return rsp

    @classmethod
    def update_status_resource_id(self, resId, newstatus):

        assert isinstance(resId, int)
        assert isinstance(newstatus, str)

        sql_statement = "update Resource set CurrentStatus='{0}' where ResourceID={1};"
        sql_statement = sql_statement.format(newstatus, str(resId))
        result = run_sql_string_statement(sql_statement)

    @classmethod
    def get_duedate_by_resourceId(self, resId):
        '''
        @rtype: str
        '''

        assert isinstance(resId, int)
        sql_statement = "select Resource.DueDate from Resource where Resource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resId))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return str(result[0][0])

    @classmethod
    def update_all_resource_id(self, newstatus, sd, ed, user, resid):

        sql_statement = "update Resource set Resource.CurrentStatus='{0}', Resource.StartDate='{1}', Resource.DueDate='{2}', Resource.CurrentUser='{3}' where Resource.ResourceID={4};"
        sql_statement = sql_statement.format(newstatus, sd, ed, user, resid)
        result = run_sql_string_statement(sql_statement)

    @classmethod
    def get_resname_by_resourceId(self, resId):
        '''
        @rtype: str
        '''

        assert isinstance(resId, int)
        sql_statement = "select Resource.ResourceName from Resource where Resource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resId))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return str(result[0][0])
