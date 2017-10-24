import unittest
from src.dao.SearchResource_DAO import SearchResource_DAO
from src.dao.db_utils import run_sql_string_statement


class Test_SearchResource_DAO(unittest.TestCase):
    def test_insert(self):
        srd = SearchResource_DAO()
        count = srd.get_count()

        print count

        # srd.insert_record(5, 3)
        print srd.get_all_records()
        print srd.get_inciId_by_resourceId(1)


if __name__ == '__main__':
    unittest.main()
