import logging

from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class SearchResource_DAO:
    def __init__(self):
        logging.info("construct the SearchResource_DAO class")

    @classmethod
    def insert_record(self, resid, incid):
        '''
        @rtype: bool
        '''
        assert isinstance(resid, int)
        assert isinstance(incid, int)

        sql_statement = "insert ERMS.SearchResource values({0},{1});"
        sql_statement = sql_statement.format(resid, incid)
        result = run_sql_string_statement(sql_statement)
        print result
        return len(result) == 0

    @classmethod
    def get_all_records(self):
        '''
        @rtype: list
        '''
        sql_statement = "select * from ERMS.SearchResource;"
        result = run_sql_string_statement(sql_statement)

        resp = list()

        if len(result) == 0 or len(result[0]) == 0:
            return resp

        for row in result:
            temp = list()
            for col in row:
                temp.append(col)
            resp.append(temp)
        return resp

    @classmethod
    def get_inciId_by_resourceId(self, resid):
        '''
        @rtype: int
        '''
        assert isinstance(resid, int)
        sql_statement = "SELECT ERMS.SearchResource.IncidentID FROM ERMS.SearchResource where ERMS.SearchResource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resid))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return result[0][0]

    @classmethod
    def get_count(self):
        '''
        @rtype: int
        '''

        sql_statement = "SELECT COUNT(*) FROM ERMS.SearchResource;"

        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return 0

        return int(result[0][0])
