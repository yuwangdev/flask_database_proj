import unittest
from src.dao.User_DAO import User_DAO


class Test_User_DAO(unittest.TestCase):
    def test(self):
        print "test the User DAO"
        userDao = User_DAO()
        data = userDao.get_all_records()
        for row in data:
            for column in row:
                print column

        new_username = "tom" + str(len(data) + 1)
        userDao.insert(new_username, "tom2info", "passwordinfo")

        data = userDao.get_record_by_username(new_username)
        for row in data:
            for column in row:
                print column
        assert len(data) == 1

        userDao.update_by_username(new_username, "newNameInfo", "newPassword")
        data = userDao.get_record_by_username(new_username)
        for row in data:
            for column in row:
                print column
        assert len(data) == 1

        userDao.delete_by_username(new_username)
        data = userDao.get_all_records()
        for row in data:
            for column in row:
                print column

        print userDao.get_nameinfo_by_username("tom")


if __name__ == '__main__':
    unittest.main()
