import unittest

import datetime

from src.data_service.Login_DataService import Login_DataService
from src.dao.User_DAO import User_DAO

dummy_name = "james" + str(datetime.datetime.now().time())


class Test_Login_DataService(unittest.TestCase):
    def test_create_dummy_user_for_test(self):
        global dummy_name
        print "test the create_dummy_user_for_test"

        print dummy_name

        lds = Login_DataService()

        rsp = lds.create_dummy_user_for_test(dummy_name, "pass", "dummy")
        print rsp

        userdao = User_DAO()
        result = userdao.get_record_by_username(dummy_name)
        print result

    def test_login_check_credential(self):

        lds = Login_DataService()
        rsp = lds.login_check_credential("tom", "passwordinfo")
        print "tom passwordinfo : "+str(rsp)

        rsp_error_password = lds.login_check_credential(dummy_name, "pass1")
        print rsp_error_password

        rsp_error_no_existed = lds.login_check_credential(dummy_name + "error", "pass1")
        print rsp_error_no_existed


if __name__ == '__main__':
    unittest.main()
