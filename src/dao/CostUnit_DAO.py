import logging

from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class CostUnit_DAO:
    def __init__(self):
        logging.info("construct the CostUnit_DAO class")

    @classmethod
    def insert_cost_unit(self, cost_unit):
        '''
        @rtype: bool
        '''
        assert isinstance(cost_unit, str)
        sql_statement = "insert CostUnit values('{0}');".format(cost_unit)
        result = run_sql_string_statement(sql_statement)
        print result
        return len(result) == 0

    @classmethod
    def get_all_CostUnits(self):
        '''
        @rtype: list
        '''
        sql_statement = "select CostUnit.CostUnit from CostUnit;"
        result = run_sql_string_statement(sql_statement)

        resp = list()
        if len(result) == 0 or len(result[0]) == 0:
            return resp

        for row in result:
            resp.append(row[0])

        return resp

    @classmethod
    def ckeck_if_in_all_costunits(self, cost_unit):
        '''
        @rtype: bool
        '''
        assert isinstance(cost_unit, str)
        return CostUnit_DAO.get_all_CostUnits().count(cost_unit) > 0
