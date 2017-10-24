from src.dao.User_DAO import User_DAO
from src.dao.UserType_DAO import UserType_DAO
from src.dao.Resource_DAO import Resource_DAO
from src.dao.CostUnit_DAO import CostUnit_DAO
from src.dao.Additional_DAO import Additional_DAO
from src.dao.Capability_DAO import Capability_DAO
from src.dao.Incident_DAO import Incident_DAO
from src.dao.ResourceRequest_DAO import ResourceRequest_DAO
from src.dao.RepairResource_DAO import RepairResource_DAO
from src.dao.SearchResource_DAO import SearchResource_DAO

print "-----------------------------------------------------"
print "runscript for inserting dummy data at dev environment"

for i in range(0, 50):
    User_DAO().insert("tomcompany" + str(i), "tomcompanyinfo" + str(i), "pass" + str(i))
    UserType_DAO.insert_record_to_company("tomcompany" + str(i), "tomcompany_headquater" + str(i))

for i in range(0, 50):
    User_DAO().insert("tomgov" + str(i), "tomgovinfo" + str(i), "pass" + str(i))
    UserType_DAO.insert_record_to_government("tomgov" + str(i), "tomgovjuris" + str(i))

for i in range(0, 50):
    User_DAO().insert("muni" + str(i), "muniinfo" + str(i), "pass" + str(i))
    UserType_DAO.insert_record_to_municipalities("muni" + str(i), 1000 + i)

for i in range(0, 50):
    User_DAO().insert("tomindi" + str(i), "tomindiinfo" + str(i), "pass" + str(i))
    UserType_DAO.insert_record_to_individual("tomindi" + str(i), "tomindijobtitle" + str(i), "2016-11-14")

for i in range(1, 50):
    usernmae = "tomcompany" + str(i)
    rsd = Resource_DAO()
    count = rsd.get_count_as_int() + 1

    if count / 3 == 0:
        status = "available"
        unit = "hour"
        addi = [1, 2, 3, 4, 5, 6, 7]
        cap = ["capa", "capb"]
    if count / 5 == 0:
        status = "in repair"
        unit = "time"
        addi = [14, 13, 5, 6, 7]
        cap = ["capa", "capb", "capc"]
    else:
        status = "not available"
        unit = "km"
        addi = [11, 12, 8]
        cap = ["capx"]

    rsd.insert_resource(count + 1, "ResName" + str(count), "dummymodel", status, 44.44, 55.55, usernmae, 250.24,
                        count % 14 + 1,
                        unit,
                        "tomcompany" + str(i - 1),
                        "2015-03-02", "2016-07-03")

    Additional_DAO(count + 1).insert_additional_esf_list(addi)
    Capability_DAO(count + 1).insert_capability(cap)

for i in range(1, 50):
    usernmae = "tomgov" + str(i)
    rsd = Resource_DAO()
    count = rsd.get_count_as_int() + 1

    if count / 3 == 0:
        status = "available"
        unit = "hour"
        addi = [1, 2, 3, 4, 5, 6, 7]
        cap = ["capa", "capb"]
    if count / 5 == 0:
        status = "in repair"
        unit = "time"
        addi = [14, 13, 5, 6, 7]
        cap = ["capa", "capb", "capc"]
    else:
        status = "not available"
        unit = "km"
        addi = [11, 12, 8]
        cap = ["capx"]

    rsd.insert_resource(count + 1, "ResName" + str(count), "dummymodel", status, 44.44, 55.55, usernmae, 250.24,
                        count % 14 + 1,
                        unit,
                        "tomgov" + str(i - 1),
                        "2015-03-02", "2016-07-03")
    Additional_DAO(count + 1).insert_additional_esf_list(addi)
    Capability_DAO(count + 1).insert_capability(cap)

for i in range(1, 50):
    usernmae = "muni" + str(i)
    rsd = Resource_DAO()
    count = rsd.get_count_as_int() + 1

    if count / 3 == 0:
        status = "available"
        unit = "hour"
        addi = [1, 2, 3, 4, 5, 6, 7]
        cap = ["capa", "capb"]
    if count / 5 == 0:
        status = "in repair"
        unit = "time"
        addi = [14, 13, 5, 6, 7]
        cap = ["capa", "capb", "capc"]
    else:
        status = "not available"
        unit = "km"
        addi = [11, 12, 8]
        cap = ["capx"]

    rsd.insert_resource(count + 1, "ResName" + str(count), "dummymodel", status, 44.44, 55.55, usernmae, 250.24,
                        count % 14 + 1,
                        unit,
                        "muni" + str(i - 1),
                        "2015-03-02", "2016-07-03")

    Additional_DAO(count + 1).insert_additional_esf_list(addi)
    Capability_DAO(count + 1).insert_capability(cap)

for i in range(1, 50):
    usernmae = "tomindi" + str(i)
    rsd = Resource_DAO()
    count = rsd.get_count_as_int() + 1

    if count / 3 == 0:
        status = "available"
        unit = "hour"
        addi = [1, 2, 3, 4, 5, 6, 7]
        cap = ["capa", "capb"]
    if count / 5 == 0:
        status = "in repair"
        unit = "time"
        addi = [14, 13, 5, 6, 7]
        cap = ["capa", "capb", "capc"]
    else:
        status = "not available"
        unit = "km"
        addi = [11, 12, 8]
        cap = ["capx"]

    rsd.insert_resource(count + 1, "ResName" + str(count), "dummymodel", status, 44.44, 55.55, usernmae, 250.24,
                        count % 14 + 1,
                        unit,
                        "tomindi" + str(i - 1),
                        "2015-03-02", "2016-07-03")

    Additional_DAO(count + 1).insert_additional_esf_list(addi)
    Capability_DAO(count + 1).insert_capability(cap)

CostUnit_DAO.insert_cost_unit("hr")
CostUnit_DAO.insert_cost_unit("hour")
CostUnit_DAO.insert_cost_unit("time")
CostUnit_DAO.insert_cost_unit("km")
CostUnit_DAO.insert_cost_unit("min")
#
for i in range(0, 50):
    count = Incident_DAO.get_count_as_int()
    Incident_DAO().insert_incident(count + 1, "2015-12-25", "dummyInci" + str(count + 1), 55.55, 22.22,
                                   "tomcompany" + str(i))

for i in range(0, 50):
    count = Incident_DAO.get_count_as_int()
    Incident_DAO().insert_incident(count + 1, "2015-12-25", "dummyInci" + str(count + 1), 55.55, 22.22,
                                   "tomgov" + str(i))

for i in range(0, 50):
    count = Incident_DAO.get_count_as_int()
    Incident_DAO().insert_incident(count + 1, "2015-12-25", "dummyInci" + str(count + 1), 55.55, 22.22,
                                   "muni" + str(i))

for i in range(0, 50):
    count = Incident_DAO.get_count_as_int()
    Incident_DAO().insert_incident(count + 1, "2015-12-25", "dummyInci" + str(count + 1), 55.55, 22.22,
                                   "tomindi" + str(i))
