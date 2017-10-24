#######################
# in order to resolve the id conflict issue when adding new resource, the generated res id is added by 100000
#######################

import logging

import time

from  src.dao.Additional_DAO import Additional_DAO
from src.dao.Capability_DAO import Capability_DAO
from src.dao.Resource_DAO import Resource_DAO
from src.dao.ESF_DAO import ESF_DAO
from src.dao.CostUnit_DAO import CostUnit_DAO
from src.dao.UserType_DAO import UserType_DAO

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Add_Resource_DataService():
    def __init__(self, username):
        logging.info("start the Add_Resource_DataService")
        self.resource_dao = Resource_DAO()
        self.new_generated_resource_id = self.resource_dao.get_count_as_int() + 100000
        self.capability_dao = Capability_DAO(self.new_generated_resource_id)
        self.additional_esf_dao = Additional_DAO(self.new_generated_resource_id)
        self.username = username
        self.esf_list_dao = ESF_DAO()
        self.usertype_dao = UserType_DAO()
        self.costunitdao = CostUnit_DAO()

    def get_new_generated_resource_id(self):
        '''
        @rtype: int
        '''
        return self.new_generated_resource_id

    def submit_form_for_new_resource(self, ResourceName, model, Latitude, Longitude,
                                     CostPerValue, EsfID, CostUnit, additionalESFList, capabilitiesList):
        '''
        @rtype: bool
        '''

        assert isinstance(self.new_generated_resource_id, int)
        assert isinstance(ResourceName, str)
        assert isinstance(model, str)
        # assert isinstance(CurrentStatus, str)
        assert isinstance(Latitude, float)
        assert isinstance(Longitude, float)
        # assert isinstance(Owner, str)
        assert isinstance(CostPerValue, float)
        assert isinstance(EsfID, int)
        assert isinstance(CostUnit, str)
        # assert isinstance(CurrentUser, str)
        # assert isinstance(StartDate, str)
        # assert isinstance(DueDate, str)

        assert isinstance(additionalESFList, list)
        assert isinstance(capabilitiesList, list)

        STATUS = ["available", "not available", "in repair"]

        # insert into the resource table
        self.resource_dao.insert_resource(self.new_generated_resource_id,
                                          ResourceName,
                                          model,
                                          STATUS[0],
                                          Latitude,
                                          Longitude,
                                          self.username,
                                          CostPerValue,
                                          EsfID,
                                          CostUnit,
                                          self.username,
                                          time.strftime("%y-%m-%d"),
                                          time.strftime("%y-%m-%d"))

        # insert into the additional esf table
        add_esf_dao = Additional_DAO(self.new_generated_resource_id)
        add_esf_dao.insert_additional_esf_list(additionalESFList)

        # insert into the cap table
        capdao = Capability_DAO(self.new_generated_resource_id)
        capdao.insert_capability(capabilitiesList)

    def populate_owner_title(self):
        '''
        @rtype: str
        '''
        usertype = self.usertype_dao.get_user_type_by_username(self.username)

        MUNICIPALITIES = "municipalities"
        GOVERNMENT_AGENCIES = "government_agencies"
        COMPANIES = "companies"
        INDIVIDUALS = "individuals"

        if usertype == MUNICIPALITIES:
            return self.usertype_dao.get_title_info_from_municipalities(self.username)

        if usertype == GOVERNMENT_AGENCIES:
            return self.usertype_dao.get_title_info_from_government(self.username)

        if usertype == COMPANIES:
            return self.usertype_dao.get_title_info_from_company(self.username)

        if usertype == INDIVIDUALS:
            return self.usertype_dao.get_title_info_from_individuals(self.username)[0]

        return ""

    def populate_esf_list(self):
        '''
        @rtype: dict
        '''
        return self.esf_list_dao.get_all_esf_records()

    def populate_costunit_list(self):
        return self.costunitdao.get_all_CostUnits()
