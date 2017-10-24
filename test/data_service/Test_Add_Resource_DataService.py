import unittest

import datetime

from src.data_service.Add_Resource_DataService import Add_Resource_DataService
from src.dao.Resource_DAO import Resource_DAO


class Test_Login_DataService(unittest.TestCase):
    def test_get_new_generated_resource_id(self):
        ard = Add_Resource_DataService("james")
        print ard.get_new_generated_resource_id()
        assert isinstance(ard.get_new_generated_resource_id(), int)

    def test_populate_owner_title(self):
        ard = Add_Resource_DataService("james")
        print ard.populate_owner_title()
        assert isinstance(ard.populate_owner_title(), str)

    def test_populate_esf_list(self):
        ard = Add_Resource_DataService("james")
        print ard.populate_esf_list()
        assert isinstance(ard.populate_esf_list(), dict)

    def test_submit_form_for_new_resource(self):
        ard = Add_Resource_DataService("james")

        rd = Resource_DAO()
        print "before: " + str(rd.get_count_as_int())

        ard.submit_form_for_new_resource("test", "testmodel", 1.1, 2.2, 3.5, 2, "hour", [3, 4, 5], ["aaa", "bbb"])

        print "after : " + str(rd.get_count_as_int())


if __name__ == '__main__':
    unittest.main()
