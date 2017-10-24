import logging

import time

from src.dao.Incident_DAO import Incident_DAO

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Add_Incident_DataService():
    def __init__(self, username):
        logging.info("start the Add_Incident_DataService")
        self.incident_dao = Incident_DAO()
        self.new_generated_incident_id = self.incident_dao.get_count_as_int() + 1000000
        self.username = username

    def get_new_generated_incident_id(self):
        '''
        @rtype: int
        '''
        return self.new_generated_incident_id

    def submit_form_for_new_incident(self, IncidentDate, Desciption, Latitude, Longitude):
        '''
        @rtype: bool
        '''

        assert isinstance(self.new_generated_incident_id, int)
        assert isinstance(Desciption, str)
        assert isinstance(Latitude, float)
        assert isinstance(Longitude, float)

        # insert into the resource table

        self.incident_dao.insert_incident(self.new_generated_incident_id,
                                          IncidentDate,
                                          Desciption,
                                          Latitude,
                                          Longitude,
                                          self.username)
