import datetime

from src.dao.User_DAO import User_DAO
from src.dao.UserType_DAO import UserType_DAO

dummy_company = "tom" + "_company_" + str(datetime.datetime.now().time())
dummy_individual = "tom" + "_individual_" + str(datetime.datetime.now().time())
dummy_government = "tom" + "_government_" + str(datetime.datetime.now().time())
dummy_municipal = "tom" + "_municipal_" + str(datetime.datetime.now().time())

MUNICIPALITIES = "municipalities"
GOVERNMENT_AGENCIES = "government_agencies"
COMPANIES = "companies"
INDIVIDUALS = "individuals"


def insert_dummy_data():
    global MUNICIPALITIES, GOVERNMENT_AGENCIES, COMPANIES, INDIVIDUALS
    global dummy_company, dummy_government, dummy_individual, dummy_municipal

    user_dao = User_DAO()
    utd = UserType_DAO()

    print user_dao.insert(dummy_company, COMPANIES, "pass")
    print user_dao.insert(dummy_individual, INDIVIDUALS, "pass")
    print user_dao.insert(dummy_government, GOVERNMENT_AGENCIES, "pass")
    print user_dao.insert(dummy_municipal, MUNICIPALITIES, "pass")

    print utd.insert_record_to_company(dummy_company, "newyork")
    print utd.insert_record_to_individual(dummy_individual, "programmer", "2015:04:12")
    print utd.insert_record_to_government(dummy_government, "state_gov")
    print utd.insert_record_to_municipalities(dummy_municipal, 888)


def test_get_user_type_info():
    global MUNICIPALITIES, GOVERNMENT_AGENCIES, COMPANIES, INDIVIDUALS
    global dummy_company, dummy_government, dummy_individual, dummy_municipal

    utd = UserType_DAO()

    print utd.get_user_type_by_username(dummy_municipal)
    print utd.get_user_type_by_username(dummy_company)
    print utd.get_user_type_by_username(dummy_government)
    print utd.get_user_type_by_username(dummy_individual)

    print utd.get_title_info_from_municipalities(dummy_municipal)
    print utd.get_title_info_from_government(dummy_government)
    print utd.get_title_info_from_individuals(dummy_individual)
    print utd.get_title_info_from_company(dummy_company)


if __name__ == '__main__':
    insert_dummy_data()
    test_get_user_type_info()
