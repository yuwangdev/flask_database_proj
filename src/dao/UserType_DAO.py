import logging

from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class UserType_DAO:
    def __init__(self):
        logging.info("construct the UserType_DAO class")

    @classmethod
    def get_user_type_by_username(self, username):
        '''
        @rtype: str
        @param username: str
        '''
        assert isinstance(username, str)
        sql_statement = "select nameinfo from Usertable where username='{0}';".format(username)
        result = run_sql_string_statement(sql_statement)
        assert isinstance(result, tuple)
        if len(result) == 1 and len(result[0]) == 1:
            return result[0][0]
        return ""

    @classmethod
    def get_title_info_from_company(self, username):
        '''
        @rtype: str
        @param username: str
        '''
        assert isinstance(username, str)
        sql_statement = "select headquarteres from Company where username='{0}';".format(username)
        result = run_sql_string_statement(sql_statement)
        assert isinstance(result, tuple)
        if len(result) == 1 and len(result[0]) == 1:
            return result[0][0]
        return ""

    @classmethod
    def get_title_info_from_government(self, username):
        '''
        @rtype: str
        @param username: str
        '''
        assert isinstance(username, str)
        sql_statement = "select jurisdiction from GovernmentAgencies where username='{0}';".format(username)
        result = run_sql_string_statement(sql_statement)
        assert isinstance(result, tuple)
        if len(result) == 1 and len(result[0]) == 1:
            return result[0][0]
        return ""

    @classmethod
    def get_title_info_from_municipalities(self, username):
        '''
        @rtype: str
        @param username: str
        '''
        assert isinstance(username, str)
        sql_statement = "select populationSize from Municipalities where username='{0}';".format(username)
        result = run_sql_string_statement(sql_statement)
        assert isinstance(result, tuple)
        if len(result) == 1 and len(result[0]) == 1:
            return str(result[0][0])
        return ""

    @classmethod
    def get_title_info_from_individuals(self, username):
        '''
        @rtype: list
        @param username: str
        '''
        assert isinstance(username, str)
        sql_statement = "select jobTitle, dateOfHired from Individuals where username='{0}'".format(username)
        result = run_sql_string_statement(sql_statement)
        assert isinstance(result, tuple)

        response = list()

        if len(result) == 1 and len(result[0]) == 2:
            response.append(result[0][0])
            response.append(str(result[0][1]))

        return response

    @classmethod
    def insert_record_to_company(self, username, headquaters):
        assert isinstance(username, str)
        assert isinstance(headquaters, str)
        sql_statement = "insert Company values('{0}', '{1}');"
        sql_statement = sql_statement.format(username, headquaters)
        result = run_sql_string_statement(sql_statement)
        return len(result) == 0

    @classmethod
    def insert_record_to_individual(self, username, jobtitle, dateOfHired):
        assert isinstance(username, str)
        assert isinstance(jobtitle, str)
        assert isinstance(dateOfHired, str)
        sql_statement = "insert Individuals values('{0}', '{1}', '{2}');"
        sql_statement = sql_statement.format(username, jobtitle, dateOfHired)
        result = run_sql_string_statement(sql_statement)
        return len(result) == 0

    @classmethod
    def insert_record_to_government(self, username, jurisdiction):
        assert isinstance(username, str)
        assert isinstance(jurisdiction, str)
        sql_statement = "insert GovernmentAgencies values('{0}', '{1}');"
        sql_statement = sql_statement.format(username, jurisdiction)
        result = run_sql_string_statement(sql_statement)
        return len(result) == 0

    @classmethod
    def insert_record_to_municipalities(self, username, population):
        assert isinstance(username, str)
        assert isinstance(population, int)
        sql_statement = "insert Municipalities values('{0}', {1});"
        sql_statement = sql_statement.format(username, population)
        result = run_sql_string_statement(sql_statement)
        return len(result) == 0
