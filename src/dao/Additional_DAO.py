import logging

from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Additional_DAO:
    resourceId = None

    def __init__(self, resourceId):
        assert isinstance(resourceId, int)
        logging.info("construct the Additional_DAO class with the Resource ID of " + str(resourceId))
        self.resourceId = resourceId

    def insert_additional_esf_list(self, additional_esf_list):
        '''
        @rtype: bool
        '''
        assert isinstance(additional_esf_list, list)

        if len(additional_esf_list) == 0:
            return False

        for item in additional_esf_list:
            sql_statement = "insert Additional values({0}, {1});".format(self.resourceId, str(item))
            rsp = run_sql_string_statement(sql_statement)

        return True

    def get_all_additional_under_resourceID(self):
        '''
        @rtype: list
        '''
        sql_statement = "select Additional.EsfID from Additional where Additional.ResourceID={0};".format(
                str(self.resourceId))

        result = run_sql_string_statement(sql_statement)

        resp = list()
        for row in result:
            resp.append(row[0])

        return resp
