from src.data_service.ActionButton_Dataservice import ActionButton_Dataservice
from src.dao.ResourceRequest_DAO import ResourceRequest_DAO

abd = ActionButton_Dataservice()
abd.request_function(4, "2016-12-12", 4)

rr = ResourceRequest_DAO()

print rr.get_expectedreturndate_by_resIdAndInciId(4, 4)

abd.repair_function(5, "james", 45)
abd.repair_function(36, "james", 45)

abd.deploy_function(4, 4, "james")
