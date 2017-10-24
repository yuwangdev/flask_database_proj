import logging

from db_utils import run_sql_string_statement
from src.dao.ESF_DAO import ESF_DAO

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
STATUS = ["available", "not available", "in repair"]


class Incident_DAO:
    def __init__(self):
        logging.info("construct the Incident_DAO class")

    @classmethod
    def get_count_as_int(self):
        '''
        @rtype: int
        '''

        sql_statement = "select count(*) from Incident;"

        result = run_sql_string_statement(sql_statement)

        return int(result[0][0])

    @classmethod
    def get_all_incidents(self):
        '''
        @rtype: list
        '''

        sql_statement = "select * from Incident;"

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
    def get_incident_record_by_username(self, username):
        '''
        @rtype: list
        '''

        assert isinstance(username, str)
        sql_statement = "select * from Incident where Incident.username='{0}';"
        sql_statement = sql_statement.format(username)
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
    def insert_incident(self, IncidentID, IncidentDate, Description, Latitude, Longitude, username):
        '''
        @rtype: bool
        '''

        assert isinstance(IncidentID, int)
        assert isinstance(IncidentDate, str)
        assert isinstance(Description, str)
        assert isinstance(Latitude, float)
        assert isinstance(Longitude, float)
        assert isinstance(username, str)

        sql_statement = "insert Incident values({0}, '{1}', '{2}', {3}, {4}, '{5}');"
        sql_statement = sql_statement.format(str(IncidentID), IncidentDate, Description, str(Latitude),
                                             str(Longitude), username)

        result = run_sql_string_statement(sql_statement)

        return len(result) == 0

    @classmethod
    def get_incident_record_by_incidentId(self, incidentId):
        '''
        @rtype: list
        '''

        assert isinstance(incidentId, int)
        sql_statement = "select * from Incident where Incident.IncidentID={0};"
        sql_statement = sql_statement.format(str(incidentId))
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
    def get_incident_position_by_incidentId(self, incidentId):
        '''
        @rtype: list
        '''

        assert isinstance(incidentId, int)
        sql_statement = "select Incident.Latitude, Incident.Longitude from Incident where Incident.IncidentID={0};"
        sql_statement = sql_statement.format(str(incidentId))
        result = run_sql_string_statement(sql_statement)

        rsp = list()

        if len(result) == 0:
            return rsp

        rsp.append(result[0][0])
        rsp.append(result[0][1])

        return rsp

    @classmethod
    def get_incident_description_by_incidentId(self, incidentId):
        '''
        @rtype: str
        '''

        assert isinstance(incidentId, int)
        sql_statement = "select Incident.Description from Incident where Incident.IncidentID={0};"
        sql_statement = sql_statement.format(str(incidentId))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return str(result[0][0])

    @classmethod
    def get_username_by_incidentId(self, incidentId):
        '''
        @rtype: str
        '''

        assert isinstance(incidentId, int)
        sql_statement = "select Incident.username from Incident where Incident.IncidentID={0};"
        sql_statement = sql_statement.format(str(incidentId))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return str(result[0][0])
