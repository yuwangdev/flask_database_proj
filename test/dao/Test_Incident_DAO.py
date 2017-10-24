import unittest
from src.dao.Incident_DAO import Incident_DAO
from src.dao.db_utils import run_sql_string_statement


class Test_Incident_DAO(unittest.TestCase):
    def test_insert_incident(self):
        icd = Incident_DAO()

        count_for_test = icd.get_count_as_int()
        print count_for_test

        icd.insert_incident(count_for_test + 1, "2016-07-03", "dummy", 14.56, 33.12, "james")

        print icd.get_count_as_int()

    def test_get_all_records(self):
        icd = Incident_DAO()
        result = icd.get_all_incidents()
        for row in result:
            print row

    def test_get_record_by_owner(self):
        icd = Incident_DAO()
        result = icd.get_incident_record_by_username("james")
        for row in result:
            print row

    def test_get_record_by_inciId(self):
        icd = Incident_DAO()
        result = icd.get_incident_record_by_incidentId(1)
        for row in result:
            print row


    def test_get_incident_position_by_incidentId(self):
        icd = Incident_DAO()
        result = icd.get_incident_position_by_incidentId(3)
        for row in result:
            print row





if __name__ == '__main__':
    unittest.main()
