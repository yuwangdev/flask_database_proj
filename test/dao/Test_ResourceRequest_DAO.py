import unittest
from src.dao.ResourceRequest_DAO import ResourceRequest_DAO
from src.dao.db_utils import run_sql_string_statement


class Test_ResourceRequest_DAO(unittest.TestCase):
    def test_insert(self):
        rrd = ResourceRequest_DAO()
        count = rrd.get_count()

        print count

        rrd.insert_record(2, 2, "2016-03-03", 4)
        print rrd.get_all_records()
        print rrd.get_expectedreturndate_by_resourceId(3)

        assert isinstance(rrd.get_expectedreturndate_by_resourceId(3), str)


if __name__ == '__main__':
    unittest.main()
