import unittest
import os
from src.daos.db_utils import split_sql_file


class Test_database_utils(unittest.TestCase):
    def test_split_complex_statement(self):
        result = split_sql_file("sss;sss1;sss2;")
        print result


if __name__ == '__main__':
    unittest.main()
