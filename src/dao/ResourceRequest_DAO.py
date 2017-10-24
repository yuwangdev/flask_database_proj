import logging

from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class ResourceRequest_DAO:
    def __init__(self):
        logging.info("construct the ResourceRequest_DAO class")

    @classmethod
    def insert_record(self, incid, reqid, expectedReturnDate, resid):
        '''
        @rtype: bool
        '''
        assert isinstance(resid, int)
        assert isinstance(incid, int)
        assert isinstance(reqid, int)
        assert isinstance(expectedReturnDate, str)

        sql_statement = "insert ERMS.ResourceRequest values({0},{1},'{2}',{3});"
        sql_statement = sql_statement.format(incid, reqid, expectedReturnDate, resid)
        result = run_sql_string_statement(sql_statement)
        print result
        return len(result) == 0

    @classmethod
    def get_all_records(self):
        '''
        @rtype: list
        '''
        sql_statement = "select * from ERMS.ResourceRequest;"
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
    def get_expectedreturndate_by_resourceId(self, resid):
        '''
        @rtype: str
        '''
        assert isinstance(resid, int)
        sql_statement = "SELECT ERMS.ResourceRequest.ExpectedReturnDate FROM ERMS.ResourceRequest where ERMS.ResourceRequest.ResourceID={0};"
        sql_statement = sql_statement.format(str(resid))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return str(result[0][0])

    @classmethod
    def get_count(self):
        '''
        @rtype: int
        '''

        sql_statement = "SELECT COUNT(*) FROM ERMS.ResourceRequest;"

        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return 0

        return int(result[0][0])

    @classmethod
    def get_expectedreturndate_by_resIdAndInciId(self, resid, incid):
        '''
        @rtype: str
        '''
        assert isinstance(resid, int)
        assert isinstance(incid, int)
        sql_statement = "SELECT ERMS.ResourceRequest.ExpectedReturnDate FROM ERMS.ResourceRequest where ERMS.ResourceRequest.ResourceID={0} and ERMS.ResourceRequest.IncidentID={1};"
        sql_statement = sql_statement.format(str(resid), str(incid))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return str(result[0][0])

    @classmethod
    def delete_by_resIdAndInciId(self, resid, incid):
        '''
        @rtype: str
        '''
        assert isinstance(resid, int)
        assert isinstance(incid, int)
        sql_statement = "delete from ERMS.ResourceRequest where ERMS.ResourceRequest.ResourceID={0} and ERMS.ResourceRequest.IncidentID={1};"
        sql_statement = sql_statement.format(str(resid), str(incid))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return str(result[0][0])
