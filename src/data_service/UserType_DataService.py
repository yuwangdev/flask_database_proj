import logging

import datetime

from src.dao.UserType_DAO import UserType_DAO
from src.dao.User_DAO import User_DAO

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

MUNICIPALITIES = "municipalities"
GOVERNMENT_AGENCIES = "government_agencies"
COMPANIES = "companies"
INDIVIDUALS = "individuals"


def get_user_type(username):
    '''
    @rtype: str
    '''
    assert isinstance(username, str)
    utd = UserType_DAO()
    user_type = utd.get_user_type_by_username(username)
    assert isinstance(user_type, str)
    return user_type


class UserType_DataService():
    def __init__(self):
        logging.debug("start the UserType_DataService()")

    def get_title_info(self, username):

        assert isinstance(username, str)

        utd = UserType_DAO()

        user_type = get_user_type(username)

        print user_type

        if user_type.__contains__("muni"):
            result = utd.get_title_info_from_municipalities(username)
            print result
            assert isinstance(result, str)
            return result

        if user_type.__contains__("com"):
            result = utd.get_title_info_from_company(username)
            assert isinstance(result, str)
            return result

        if user_type.__contains__("gov"):
            result = utd.get_title_info_from_government(username)
            assert isinstance(result, str)
            return result

        if user_type.__contains__("indi"):
            result = utd.get_title_info_from_individuals(username)
            assert isinstance(result, list)
            return result
