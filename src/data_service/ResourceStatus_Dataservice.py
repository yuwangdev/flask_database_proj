import logging

import datetime

from src.dao.db_utils import run_sql_string_statement
from src.dao.User_DAO import User_DAO
from src.dao.Incident_DAO import Incident_DAO
from src.dao.ResourceRequest_DAO import ResourceRequest_DAO
from src.dao.Resource_DAO import Resource_DAO
from src.dao.RepairResource_DAO import RepairResource_DAO

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class ResourceStatus_DataService():
    def __init__(self):
        logging.debug("start the ResourceStatus_DataService()")
        self.userdao = User_DAO()
        self.incidao = Incident_DAO()
        self.resreqdao = ResourceRequest_DAO()
        self.resdao = Resource_DAO()
        self.repairResourcedao = RepairResource_DAO()

    def populate_res_in_use_tabledata(self, username):
        assert isinstance(username, str)
        sql = "SELECT ResourceID, ResourceName, owner, startDate, CurrentUser FROM Resource WHERE ResourceID in (SELECT ResourceID FROM Resource WHERE CurrentUser ='{0}');"
        sql = sql.format(username)
        result = run_sql_string_statement(sql)

        fr = list()

        if len(result) == 0 or len(result[0]) == 0:
            return fr

        for row in result:
            tmp = list()
            tmp.append(row[0])
            tmp.append(row[1])
            tmp.append(self.userdao.get_nameinfo_by_username(row[2]))
            tmp.append(str(row[3]))
            tmp.append(self.userdao.get_nameinfo_by_username(row[4]))

            fr.append(tmp)

        return fr

    def return_button(self, resId):
        assert isinstance(resId, int)
        sql = "UPDATE Resource SET startDate =NULL, DueDate = NULL, CurrentUser = NULL, CurrentStatus ='available' WHERE ResourceID = {0};"
        sql = sql.format(resId)
        result = run_sql_string_statement(sql)

    def res_request_by_username(self, username):

        assert isinstance(username, str)

        finalresult = list()

        sql = "SELECT ResourceID, IncidentID FROM ResourceRequest WHERE IncidentID in (SELECT IncidentID FROM Incident WHERE Incident.username ='{0}');"

        sql = sql.format(username)
        temp_result = run_sql_string_statement(sql)

        if len(temp_result) == 0 or len(temp_result[0]) == 0:
            return finalresult

        templist = list()

        for row in temp_result:

            rowtemp = list()
            resid = int(row[0])
            incid = int(row[1])

            sql = "SELECT ResourceName, Owner, DueDate FROM Resource WHERE ResourceID = {0};".format(resid)
            t1 = run_sql_string_statement(sql)

            if len(t1) == 0 or len(t1[0]) == 0:
                rowtemp.append(resid)
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")


            else:
                rowtemp.append(resid)
                rowtemp.append(t1[0][0])
                rowtemp.append(self.incidao.get_incident_description_by_incidentId(incid))
                rowtemp.append(self.userdao.get_nameinfo_by_username(t1[0][1]))
                rowtemp.append(str(t1[0][2]))
                rowtemp.append(incid)

            finalresult.append(rowtemp)

        return finalresult

    def cancel_button(self, resid, incid):
        assert isinstance(resid, int)
        assert isinstance(incid, int)
        self.resreqdao.delete_by_resIdAndInciId(resid, incid)

    def request_received_me(self, username):
        assert isinstance(username, str)

        finalresult = list()

        sql = "SELECT ResourceID, RequestID, ExpectedReturnDate, IncidentID FROM ResourceRequest WHERE ResourceID in (SELECT ResourceID from Resource WHERE Resource.Owner ='{0}');"

        sql = sql.format(username)
        temp_result = run_sql_string_statement(sql)

        if len(temp_result) == 0 or len(temp_result[0]) == 0:
            return finalresult

        templist = list()

        for row in temp_result:
            resid = row[0]
            erd = row[2]
            incid = row[3]
            reqid = row[1]

            t = run_sql_string_statement(
                    "SELECT CurrentStatus, ResourceName, DueDate FROM Resource WHERE ResourceID = {0};".format(
                            int(row[0])))

            templist.append(resid)
            templist.append(self.resdao.get_resname_by_resourceId(int(resid)))
            templist.append(self.incidao.get_incident_description_by_incidentId(int(incid)))
            templist.append(self.userdao.get_nameinfo_by_username(username))
            templist.append(str(erd))

            status = t[0][0]

            if status != "available":
                templist.append("reject")
            else:
                if self.repairResourcedao.get_count_by_resId(resid) == 0:
                    templist.append("cancelrepair")
                else:
                    templist.append("deploy-reject")

            templist.append(incid)
            finalresult.append(templist)

        return finalresult

    def reject_button(self, resid, incid):
        assert isinstance(resid, int)
        assert isinstance(incid, int)
        self.resreqdao.delete_by_resIdAndInciId(resid, incid)

    def cancelrepair_button(self, resid):
        assert isinstance(resid, int)
        self.repairResourcedao.delete_by_resId(resid)

    def deploy_button(self, resid, erd, username, inciid):
        assert isinstance(resid, int)
        assert isinstance(inciid, int)

        today = str(datetime.datetime.today().date())
        sql = "UPDATE Resource SET startDate ='{0}', DueDate = '{1}', CurrentStatus = 'not available', CurrentUser = '{2}' WHERE ResourceID = {3};"
        run_sql_string_statement(sql.format(today, str(erd), username, resid))
        self.resreqdao.delete_by_resIdAndInciId(resid, inciid)

    def repairtable(self, username):
        assert isinstance(username, str)

        sql = "SELECT ResourceID, repairID, startDate, endDate FROM RepairResource WHERE ResourceID in (SELECT ResourceID FROM Resource WHERE Owner ='{0}')";
        tempresult = run_sql_string_statement(sql.format(username))

        finalre = list()

        if len(tempresult) == 0 or len(tempresult[0]) == 0:
            return finalre

        for row in tempresult:
            resid = int(row[0])
            tm = list()
            tm.append(resid)
            tm.append(self.resdao.get_resname_by_resourceId(resid))
            tm.append(str(row[2]))
            tm.append(str(row[3]))
            finalre.append(tm)
        return finalre
