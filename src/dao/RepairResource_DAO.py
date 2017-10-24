import logging

from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class RepairResource_DAO:
    def __init__(self):
        logging.info("construct the RepairResource_DAO class")

    @classmethod
    def insert_records(self, resId, repId, username, sd, ed):
        '''
        @rtype: bool
        '''
        assert isinstance(resId, int)
        assert isinstance(repId, int)
        assert isinstance(username, str)
        assert isinstance(sd, str)
        assert isinstance(ed, str)
        sql_statement = "insert ERMS.RepairResource values({0},{1},'{2}','{3}','{4}');"
        sql_statement = sql_statement.format(resId, repId, username, sd, ed)
        result = run_sql_string_statement(sql_statement)
        print result
        return len(result) == 0

    @classmethod
    def get_all_repair_resource_lists(self):
        '''
        @rtype: list
        '''
        sql_statement = "SELECT * FROM ERMS.RepairResource;"
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
    def get_all_repair_resource_lists_by_resourceID(self, resid):
        '''
        @rtype: list
        '''
        assert isinstance(resid, int)
        sql_statement = "SELECT * FROM ERMS.RepairResource where ERMS.RepairResource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resid))
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
    def get_all_repair_resource_lists_by_repairId(self, resid):
        '''
        @rtype: list
        '''
        assert isinstance(resid, int)
        sql_statement = "SELECT * FROM ERMS.RepairResource where ERMS.RepairResource.repairID={0};"
        sql_statement = sql_statement.format(str(resid))
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
    def get_enddate_by_resourceId(self, resid):
        '''
        @rtype: str
        '''
        assert isinstance(resid, int)
        sql_statement = "SELECT ERMS.RepairResource.endDate FROM ERMS.RepairResource where ERMS.RepairResource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resid))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return str(result[0][0])

    @classmethod
    def get_startdate_by_resourceId(self, resid):
        '''

        '''
        assert isinstance(resid, int)
        sql_statement = "SELECT ERMS.RepairResource.startDate FROM ERMS.RepairResource where ERMS.RepairResource.ResourceID={0};"
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

        sql_statement = "SELECT COUNT(*) FROM ERMS.RepairResource;"

        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return 0

        return int(result[0][0])

    @classmethod
    def get_count_by_resId(self, resid):
        '''
        @rtype: int
        '''

        sql_statement = "SELECT COUNT(*) FROM ERMS.RepairResource where ERMS.RepairResource.ResourceID={0};".format(
                str(resid))

        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return 0

        return int(result[0][0])

    @classmethod
    def delete_by_resId(self, resid):
        '''
        @rtype: str
        '''
        assert isinstance(resid, int)

        sql_statement = "delete from ERMS.RepairResource where ERMS.RepairResource.ResourceID={0};"
        sql_statement = sql_statement.format(str(resid))
        result = run_sql_string_statement(sql_statement)

        if len(result) == 0 or len(result[0]) == 0:
            return ""

        return str(result[0][0])
