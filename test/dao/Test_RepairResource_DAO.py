import unittest
from src.dao.RepairResource_DAO import RepairResource_DAO
from src.dao.db_utils import run_sql_string_statement


class Test_RepairResource_DAO(unittest.TestCase):
    def test_insert(self):
        rrd = RepairResource_DAO()
        count = rrd.get_count()

        print count

        # rrd.insert_records(count + 1, count + 1, "james", "2015-03-03", "2016-03-03")
        print rrd.get_all_repair_resource_lists()
        print rrd.get_all_repair_resource_lists_by_repairId(3)
        print rrd.get_all_repair_resource_lists_by_resourceID(4)

        print rrd.get_enddate_by_resourceId(3)

        assert isinstance(rrd.get_enddate_by_resourceId(3), str)


if __name__ == '__main__':
    unittest.main()
