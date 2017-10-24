import unittest
from src.dao.ESF_DAO import ESF_DAO


class Test_ESF_DAO(unittest.TestCase):
    def test_get_all(self):
        esf_dao = ESF_DAO()
        result = esf_dao.get_all_esf_records()

        assert isinstance(result, dict)
        for k, v in result.iteritems():
            print str(k) + "->" + v

    def test_get_item_by_id(self):
        esf_dao = ESF_DAO()

        print esf_dao.get_record_by_esfId(1)
        print esf_dao.get_record_by_esfId(10)


if __name__ == '__main__':
    unittest.main()
