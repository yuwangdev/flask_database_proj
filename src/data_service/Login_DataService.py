import logging

from src.dao.User_DAO import User_DAO

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)



class Login_DataService():
    user_dao = None

    def __init__(self):
        logging.info("start the Login_service service")
        self.user_dao = User_DAO()

    def create_dummy_user_for_test(self, username, password, passwordinfo):
        '''
        @rtype: bool
        @type: username: str
        @type: password: str
        @type: passwordinfo: str
        '''

        assert isinstance(username, str)
        assert isinstance(password, str)
        assert isinstance(passwordinfo, str)
        logging.debug("insert a dummy user for testing purpose")
        status = self.user_dao.insert(username, password, passwordinfo)
        assert isinstance(status, bool)
        return status

    def login_check_credential(self, username_input, password_input):
        '''
        @rtype: bool
        @type: username_input: str
        @type: password_input: str
        '''

        assert isinstance(username_input, str)
        assert isinstance(password_input, str)

        logging.debug("login to check credential: username={0}, password={1}".format(username_input, password_input))

        result = tuple()

        result = self.user_dao.get_record_by_username(username_input)

        print result
        assert isinstance(result, tuple)

        logging.debug("result from user_dao.get_record_by_username: ")
        logging.debug(result)

        if len(result) == 0:
            return False

        first_row_data = result[0]
        assert isinstance(first_row_data, tuple)

        password_correct = first_row_data[2]

        return password_input == password_correct
