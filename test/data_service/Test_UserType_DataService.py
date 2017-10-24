from src.data_service.UserType_DataService import UserType_DataService

ut = UserType_DataService()
print ut.get_title_info("muni1")

ut = UserType_DataService()
print ut.get_title_info("tomgov1")

ut = UserType_DataService()
print ut.get_title_info("tomcompany1")

ut = UserType_DataService()
print ut.get_title_info("tomindi1")
