from src.data_service.ResourceStatus_Dataservice import ResourceStatus_DataService

rsd = ResourceStatus_DataService()

print rsd.populate_res_in_use_tabledata("james")

print rsd.return_button(4)

print rsd.cancel_button(44, 1)

print rsd.res_request_by_username("james")

print rsd.request_received_me("james")

print rsd.reject_button(42, 1)

print rsd.cancelrepair_button(3)

print rsd.deploy_button(4, '2018-03-02', "tom", 7)

print rsd.repairtable("james")
