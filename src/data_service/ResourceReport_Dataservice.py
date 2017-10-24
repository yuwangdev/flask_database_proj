import logging

from src.dao.db_utils import run_sql_string_statement

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class ResourceReport_DataService():
    def __init__(self):
        logging.debug("start the ResourceReport_DataService()")

    def totaldata(self):

        sql = "select Resource.EsfID, ESF.item, count(*) from Resource inner join ESF on ESF.EsfID = Resource.EsfID group by Resource.EsfID order by Resource.EsfID;";
        result = run_sql_string_statement(sql)

        fr = list()

        if len(result) == 0 or len(result[0]) == 0:
            return fr

        for row in result:
            tep = list()
            tep.append(row[0])
            tep.append(row[1])
            tep.append(row[2])

            fr.append(tep)
        return fr

    def usedata(self):

        sql = "select Resource.EsfID, ESF.item, count(*) from Resource inner join ESF on ESF.EsfID = Resource.EsfID where Resource.CurrentStatus='not available' group by Resource.EsfID order by Resource.EsfID;"
        result = run_sql_string_statement(sql)

        fr = list()

        if len(result) == 0 or len(result[0]) == 0:
            return fr

        for row in result:
            tep = list()
            tep.append(row[0])
            tep.append(row[1])
            tep.append(row[2])

            fr.append(tep)
        return fr
