import unittest
from src.dao.Additional_DAO import Additional_DAO
from src.dao.db_utils import run_sql_string_statement


class Test_Additional_DAO(unittest.TestCase):
    def test(self):
        print "test the Additional DAO"
        cpd = Additional_DAO(123)

        count_for_test = run_sql_string_statement("select count(*) from Additional")
        count = int(count_for_test[0][0])
        print "count==" + str(count)

        print cpd.insert_additional_esf_list([3, 4])

        rsp = cpd.get_all_additional_under_resourceID()
        assert isinstance(rsp, list)
        for item in rsp:
            print item


if __name__ == '__main__':
    unittest.main()
