import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
from src.dao.ESF_DAO import ESF_DAO
from src.dao.Incident_DAO import Incident_DAO


class Search_Resource_DataService():
    def __init__(self, username):
        assert isinstance(username, str)
        logging.debug("start the Search_Resource_DataService()")
        self.username = username

    def get_esf_lists(self):
        '''
        @rtype: list
        '''
        ed = ESF_DAO()
        result = list()
        mapper = ed.get_all_esf_records()
        print mapper
        for k, v in mapper.iteritems():
            result.append(str(int(k)) + "# " + str(v))
        return result

    def get_incidents_of_this_user_lists(self):
        '''
        @rtype: list
        '''
        icd = Incident_DAO()
        temp = icd.get_incident_record_by_username(self.username)
        result = list()
        for item in temp:
            result.append("(" + str(item[0]) + ") " + str(item[2]))
        return result
