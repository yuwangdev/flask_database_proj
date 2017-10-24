import logging

from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Capability_DAO:
    resourceID = None

    def __init__(self, resourceID):
        assert isinstance(resourceID, int)
        self.resourceID = resourceID
        logging.info("construct the Capability_DAO class with " + str(self.resourceID))

    def insert_capability(self, capability):
        '''
        @rtype: bool
        '''
        assert isinstance(capability, list)

        for item in capability:
            sql_statement = "insert Capability values({0}, '{1}');".format(self.resourceID, item)
            result = run_sql_string_statement(sql_statement)
        return True

    def get_all_capabilities_under_resourceID(self):
        '''
        @rtype: list
        '''
        sql_statement = "select Capability.CapabilitiyStr from Capability where Capability.ResourceID={0};".format(
                str(self.resourceID))

        result = run_sql_string_statement(sql_statement)

        resp = list()
        for row in result:
            resp.append(row[0])

        return resp
