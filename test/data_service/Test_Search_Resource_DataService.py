import unittest

import datetime

from src.data_service.Search_Resource_Dataservice import Search_Resource_DataService


class Test_Login_DataService(unittest.TestCase):
    def test(self):
        srd = Search_Resource_DataService("james")
        assert isinstance(srd.get_esf_lists(), list)
        print srd.get_esf_lists()

        assert isinstance(srd.get_incidents_of_this_user_lists(), list)
        print srd.get_incidents_of_this_user_lists()


if __name__ == '__main__':
    unittest.main()
