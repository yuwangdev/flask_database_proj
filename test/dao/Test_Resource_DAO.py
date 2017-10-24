import unittest
from src.dao.Resource_DAO import Resource_DAO
from src.dao.db_utils import run_sql_string_statement


class Test_Resource_DAO(unittest.TestCase):
    def test_insert_record(self):
        rsd = Resource_DAO()

        count_for_test = run_sql_string_statement("select count(*) from Resource")
        count = int(count_for_test[0][0])

        rsd.insert_resource(count + 1, "123Name", "dummy", "available", 14.56, 33.12, "james", 120.4, 3, "hour", "tom",
                            "2015-03-02", "2016-07-03")

    def test_get_all_records(self):
        rsd = Resource_DAO()
        result = rsd.get_all_resource()
        for row in result:
            print row

    def test_get_record_by_owner(self):
        rsd = Resource_DAO()
        result = rsd.get_resource_record_by_owner("james")
        for row in result:
            print row

    def test_get_record_by_resId(self):
        rsd = Resource_DAO()
        result = rsd.get_resource_record_by_resourceId(4)
        for row in result:
            print row

    def test_get_count(self):
        rsd = Resource_DAO()
        result = rsd.get_count_as_int()
        print result
        assert isinstance(result, int)

    def test_get_resource_lists_by_keyword_capabilities(self):
        rsd = Resource_DAO()
        result = rsd.get_resource_lists_by_keyword_capabilities("cap")
        print result

    def test_get_resourceId_lists_by_keyword_model_or_name(self):
        rsd = Resource_DAO()
        result = rsd.get_resourceId_lists_by_keyword_model_or_name("test")
        print result

    def get_resource_lists_by_keyword_esf(self):
        rsd = Resource_DAO()
        result = rsd.get_resource_lists_by_keyword_esf("gen")
        print result

    def get_resource_list(self):
        rsd = Resource_DAO()
        result = rsd.get_resource_costtext_by_resourceId(3)
        print result

    def get_all_resid(self):
        rsd = Resource_DAO()
        result = rsd.get_all_resource_id()

        rsd.update_status_resource_id(3, "in repair")
        print result


if __name__ == '__main__':
    unittest.main()
