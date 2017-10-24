import logging
import MySQLdb as mdb

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

connection = mdb.connect('127.0.0.1', 'admin', 'admin', 'ERMS')


def split_sql_file(complex_sql_string):
    '''
    @rtype: list
    @:param: str
    '''
    assert isinstance(complex_sql_string, str)
    result = list()
    result = complex_sql_string.split(";")
    assert isinstance(result, list)
    return result


def run_sql_file(filename):
    global connection
    assert isinstance(connection, mdb.connections.Connection)
    file = open(filename, 'r')
    sql = " ".join(file.readlines())
    logging.debug("sql statement: " + sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()


def run_sql_string_statement(statement):
    '''
    @rtype: tuple
    '''
    global connection
    assert isinstance(connection, mdb.connections.Connection)
    logging.debug("sql statement: " + statement)
    assert isinstance(statement, str)
    cursor = connection.cursor()
    assert isinstance(cursor, mdb.cursors.Cursor)
    cursor.execute(statement)
    data=cursor.fetchall()
    connection.commit()
    cursor.close()
    return data
