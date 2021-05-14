import sqlite3
from sqlite3 import Error
from os import path
import time
import sys

DB_FILE_NAME = '\\restdb.db'

class Database:
    __conn = None
    def __new__(cls):
        HERE = str(path.abspath(path.dirname(__file__)))
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
            try:
                cls.__conn = sqlite3.connect(HERE + DB_FILE_NAME)
            except Exception as ex:
                raise ValueError(f"Can't create db connection: {ex}")
        return cls.__conn
    def __del__(self):
        if self.__conn:
            self.__conn.close()

class DBTool:
    __conn = None

    def __init__(self):
        self.__conn = Database()
        self.__db_init()

    def __del__(self):
        if self.__conn:
            self.__conn.close()

    def __db_init(self):
        sql_for_requests_table = """
            create table if not exists requests (
                rqst_id integer primary key autoincrement,
                state text,
                date real
            )
        """
        self.execute_sql(sql_for_requests_table)
    
    def execute_sql(self, sqls):
        result = None
        try:
            result = self.__conn.execute(sqls)
            self.__conn.commit()
        except Exception as ex:
            print(ex)
            sys.exit(-1)
        return result

    def select_sql(self, sql, condition=''):
        data = None
        try:
            data = self.__conn.execute(sql + ' ' + condition).fetchall()
        except Exception as ex:
            print(ex)
            sys.exit(-1)
        return data
            


# if __name__ == '__main__':
    
#     dbtool = DBTool()
    
#     dbtool.execute_sql(sqls='drop table requests')
#     dbtool.db_init()
    
#     insert_sql = f"""insert into requests (state, date) values('new', {time.time()})"""
#     dbtool.execute_sql(sqls =insert_sql)
#     time.sleep(1)
#     dbtool.execute_sql(insert_sql)
#     time.sleep(1)
#     dbtool.execute_sql(insert_sql)
#     time.sleep(1)
#     dbtool.execute_sql(insert_sql)
    
#     data = dbtool.select_sql('select * from requests')
#     for row in data:
#         print(row)
    # #create_connection(DB_FILE_NAME)
