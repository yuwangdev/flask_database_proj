import logging

from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class User_DAO:
    def __init__(self):
        logging.info("construct the UserDAO class")

    @classmethod
    def get_all_records(self):
        '''
        @rtype: tuple
        '''
        sql_statement = "select * from ERMS.Usertable;"
        result = run_sql_string_statement(sql_statement)
        return result

    @classmethod
    def get_record_by_username(self, username):
        '''
        @rtype: tuple
        '''
        sql_statement = "select * from ERMS.Usertable as t1 where t1.username='{0}';"
        sql_statement = sql_statement.format(username)
        result = run_sql_string_statement(sql_statement)
        assert isinstance(result, tuple)
        return result

    @classmethod
    def insert(self, username, nameinfo, passwordinfo):
        '''
        @rtype: bool
        '''
        sql_statement = "insert Usertable(Usertable.username, Usertable.nameInfo, Usertable.passwordInfo) values('{0}', '{1}', '{2}');"
        sql_statement = sql_statement.format(username, nameinfo, passwordinfo)
        result = run_sql_string_statement(sql_statement)
        return True if len(result) == 0 else False

    @classmethod
    def update_by_username(self, username, nameinfo, passwordinfo):
        sql_statement = "update Usertable set Usertable.nameInfo='{0}', Usertable.passwordInfo='{1}' where Usertable.username='{2}';"
        sql_statement = sql_statement.format(nameinfo, passwordinfo, username)
        run_sql_string_statement(sql_statement)

    @classmethod
    def delete_by_username(self, username):
        sql_statement = "delete from Usertable where Usertable.username='{0}';"
        sql_statement = sql_statement.format(username)
        run_sql_string_statement(sql_statement)

    def get_nameinfo_by_username(self, username):
        sql_statement = "select Usertable.nameInfo from Usertable where Usertable.username='{0}';"
        sql_statement = sql_statement.format(username)
        result = run_sql_string_statement(sql_statement)
        if len(result) == 0 or len(result[0]) == 0:
            return ""
        return result[0][0]
