from src.dao.CostUnit_DAO import CostUnit_DAO


def insert_dummy_data():
    print "testing insert dummy data"
    cud = CostUnit_DAO()
    print cud.insert_cost_unit("hour")
    print cud.insert_cost_unit("minute")
    print cud.insert_cost_unit("day")
    print cud.insert_cost_unit("time")
    print cud.insert_cost_unit("km")


def test_get_all():
    print "testing get all cost units"
    cud = CostUnit_DAO()
    result = cud.get_all_CostUnits()

    assert isinstance(result, list)

    assert isinstance(result, list)
    for item in result:
        print item


if __name__ == '__main__':
    # insert_dummy_data()
    test_get_all()
