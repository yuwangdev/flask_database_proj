import unittest

import datetime

from src.data_service.Add_Incident_Dataservice import Add_Incident_DataService
from src.dao.Incident_DAO import Incident_DAO


class Test_Login_DataService(unittest.TestCase):
    def test_get_new_generated_resource_id(self):
        aid = Add_Incident_DataService("james")
        print aid.get_new_generated_incident_id()
        assert isinstance(aid.get_new_generated_incident_id(), int)

    def test_submit_form_for_new_resource(self):
        aid = Add_Incident_DataService("james")

        icd = Incident_DAO()
        print "before: " + str(icd.get_count_as_int())

        aid.submit_form_for_new_incident("2000-04-03", "testinci", 1.1, 2.2)

        print "after : " + str(icd.get_count_as_int())


if __name__ == '__main__':
    unittest.main()
