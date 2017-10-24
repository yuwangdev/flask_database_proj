import logging

from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class ESF_DAO:
    def __init__(self):
        logging.info("construct the ESF_DAO class")

    @classmethod
    def get_all_esf_records(self):
        '''
        @rtype: dict
        '''
        sql_statement = "select * from ERMS.ESF;"
        result = run_sql_string_statement(sql_statement)

        resp = dict()
        for row in result:
            resp[row[0]] = row[1]

        return resp

    @classmethod
    def get_record_by_esfId(self, esfId):
        '''
        @rtype: str
        @param esfId: int
        '''
        assert isinstance(esfId, int)
        sql_statement = "select ESF.item from ERMS.ESF where EsfID={0};"
        sql_statement = sql_statement.format(esfId)
        result = run_sql_string_statement(sql_statement)

        return result[0][0] if len(result) == 1  else "";
