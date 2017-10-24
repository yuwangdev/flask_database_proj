### only to prove the setup is okay


import os, logging
import MySQLdb as mdb
from db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def testing():
    logging.info("display MySQL version number")
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    file_path = os.path.join(SITE_ROOT, "sql_statement", "createTables.sql")
    db = mdb.connect('127.0.0.1', 'admin', 'admin', 'ERMS')
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchall()
    print "Database version : %s " % data
    db.close()


def testing2():
    logging.info("display MySQL version by my wrapper")
    sql = "SELECT VERSION()"
    result = run_sql_string_statement(sql)
    print len(result)
    print result


if __name__ == '__main__':
    testing()
    testing2()
