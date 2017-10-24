import logging

from datetime import datetime, timedelta

from src.dao.ResourceRequest_DAO import ResourceRequest_DAO
from src.dao.RepairResource_DAO import RepairResource_DAO
from src.dao.Resource_DAO import Resource_DAO

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class ActionButton_Dataservice():
    def __init__(self):
        logging.info("start the ActionButton_Dataservice")
        self.resource_request_dao = ResourceRequest_DAO()
        self.repair_resource_dao = RepairResource_DAO()
        self.resource_dao = Resource_DAO()

    def request_function(self, resId, expDate, incid):
        assert isinstance(resId, int)
        assert isinstance(expDate, str)
        assert isinstance(incid, int)
        new_id = int(self.resource_request_dao.get_count()) + 1000
        self.resource_request_dao.insert_record(incid, new_id, expDate, resId)

    def repair_function(self, resId, username, duration):
        assert isinstance(resId, int)
        assert isinstance(username, str)
        assert isinstance(duration, int)
        repId = int(self.repair_resource_dao.get_count()) + 1

        currentStatus = self.resource_dao.get_resource_status_by_resourceId(resId)

        if currentStatus == "available":
            start = datetime.now()
            end = start + timedelta(days=duration)
            sd = datetime.strftime(start, "%Y-%m-%d")
            ed = datetime.strftime(end, "%Y-%m-%d")

            self.resource_dao.update_status_resource_id(resId, "in repair")
            self.repair_resource_dao.insert_records(resId, repId, username, sd, ed)

        if currentStatus == "not available":
            start = self.resource_dao.get_duedate_by_resourceId(resId)
            sd = datetime.strptime(start, "%Y-%m-%d")
            end = sd + timedelta(days=duration)
            sd = datetime.strftime(sd, "%Y-%m-%d")
            ed = datetime.strftime(end, "%Y-%m-%d")
            self.repair_resource_dao.insert_records(resId, repId, username, sd, ed)

    def deploy_function(self, incid, resid, username):
        assert isinstance(incid, int)
        assert isinstance(resid, int)
        assert isinstance(username, str)
        duedate = self.resource_request_dao.get_expectedreturndate_by_resIdAndInciId(resid, incid)
        start = datetime.now()
        sd = datetime.strftime(start, "%Y-%m-%d")
        logging.info(sd)
        end = start + timedelta(days=22)
        ed = datetime.strftime(end, "%Y-%m-%d")
        self.resource_dao.update_all_resource_id("not available", sd, ed, username, resid)
        self.resource_request_dao.delete_by_resIdAndInciId(resid, incid)
