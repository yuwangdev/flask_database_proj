import unittest
from src.dao.Capability_DAO import Capability_DAO
from src.dao.db_utils import run_sql_string_statement


class Test_Capability_DAO(unittest.TestCase):
    def test(self):
        print "test the Capability DAO"
        cpd = Capability_DAO(123)

        count_for_test = run_sql_string_statement("select count(*) from Capability")
        count = int(count_for_test[0][0])

        dummy = list()
        dummy.append("cap123-" + str(count + 1))
        dummy.append("cap123-" + str(count + 2))
        print cpd.insert_capability(dummy)
        rsp = cpd.get_all_capabilities_under_resourceID()
        assert isinstance(rsp, list)
        for item in rsp:
            print item


if __name__ == '__main__':
    unittest.main()
