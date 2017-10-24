import unittest
from src.dao.ResourceRequest_DAO import ResourceRequest_DAO
from src.dao.RepairResource_DAO import RepairResource_DAO
from src.dao.Resource_DAO import Resource_DAO

import datetime

from src.dao.db_utils import run_sql_string_statement
from src.data_service.Search_Result_Dataservice import Search_Result_DataService


class Test_Search_Result_DataService(unittest.TestCase):
    def test_get_resourceId_searched_by_keyword(self):
        srd = Search_Result_DataService()
        assert isinstance(srd.get_resourceId_searched_by_keyword("b"), list)
        print srd.get_resourceId_searched_by_keyword("b")

    def test_get_incident_position(self):
        srd = Search_Result_DataService()
        assert isinstance(srd.get_incident_position("(6) testinci"), list)
        print srd.get_incident_position("(6) testinci")

    def test_get_distance_between_res_inci(self):
        srd = Search_Result_DataService()
        assert isinstance(srd.get_distance_between_res_inci(1.1, 2.2, 4), float)
        print "______________________"
        print srd.get_distance_between_res_inci(1.1, 2.2, 4)

    def test_get_resIdDict_within_distance(self):
        srd = Search_Result_DataService()
        ma = srd.get_resIdDict_within_distance("(6) testinci", 10000000, srd.get_resourceId_searched_by_keyword("b"))
        assert isinstance(ma, dict)
        print ma

    def test_get_resIdDict_within(self):
        srd = Search_Result_DataService()
        ma = srd.get_esf_id("2# Communic cation")
        assert isinstance(ma, int)
        assert ma == 2

    def test_populate_table_data(self):
        srd = Search_Result_DataService()
        ma = srd.populate_table_data("a", "2# aaa", 1000000, "(6) testinci")
        assert isinstance(ma, list)
        print ma

        ma = srd.populate_table_data("", "2# aaa", 1000000, "(6) testinci")
        assert isinstance(ma, list)
        print ma

        ma = srd.populate_table_data("", "", 1000000, "(6) testinci")
        assert isinstance(ma, list)
        print ma

        ma = srd.populate_table_data("", "", 0, "")
        assert isinstance(ma, list)
        print ma

    def test_more(self):
        srd = Search_Result_DataService()
        resd = Resource_DAO()
        rep = RepairResource_DAO()
        reqeust = ResourceRequest_DAO()

        count_for_test = run_sql_string_statement("select count(*) from Resource")
        count = int(count_for_test[0][0])

        a = count + 1
        b = count + 2

        resd.insert_resource(a, "123Name", "dummy", "not available", 14.56, 33.12, "james", 120.4, 3, "hour", "tom",
                             "2015-03-02", "2016-07-03")

        resd.insert_resource(b, "123Name", "dummy", "in repair", 14.56, 33.12, "james", 120.4, 3, "hour", "tom",
                             "2015-03-02", "2016-07-03")

        rep.insert_records(b, rep.get_count() + 1, "james", "2015-03-02", "2016-07-03")
        reqeust.insert_record(1, reqeust.get_count() + 1, "2015-03-02", a)

        ma = srd.populate_table_data("a", "2# aaa", 1000000, "(6) testinci")
        assert isinstance(ma, list)
        print ma

    def test_action(self):
        srd = Search_Result_DataService()
        ma = srd.populate_table_data("a", "2# aaa", 1000000, "(6) testinci")
        print ma
        action = srd.populate_action_lists(ma, "james")
        print action

        srd = Search_Result_DataService()
        ma = srd.populate_table_data("", "2# aaa", 1000000, "(6) testinci")
        print ma
        action = srd.populate_action_lists(ma, "james")
        print action

        srd = Search_Result_DataService()
        ma = srd.populate_table_data("", "", 1000000, "(6) testinci")
        print ma
        action = srd.populate_action_lists(ma, "james")
        print action

        srd = Search_Result_DataService()
        ma = srd.populate_table_data("", "", 0, "")
        print ma
        action = srd.populate_action_lists(ma, "james")
        print action


if __name__ == '__main__':
    unittest.main()
