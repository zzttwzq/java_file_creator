# 导入pymysql模块
import pymysql
from dbutils.pooled_db import PooledDB
from pymysql.cursors import DictCursor
from Utils.log_util import Log, SqlLog

class MySqlConfig:
    host = "localhost"
    port = 3306
    user = "root"
    passwd = "123"
    name = ""
    char_set = "utf8"
 
class MySqlUtil:
    _conn = None
    _cursor = None
    __pool = None

    def __init__(self, mysqlConfig):
        # 从连接池中获取连接
        self._conn = MySqlUtil.__getConn(mysqlConfig)
        self._cursor = self._conn.cursor()

    @staticmethod
    def __getConn(mysqlConfig):

        if MySqlUtil.__pool is None:
            MySqlUtil.__pool = PooledDB(creator=pymysql, 
                                        mincached=1, 
                                        maxcached=30,
                                        host=mysqlConfig.host, 
                                        port=mysqlConfig.port, 
                                        user=mysqlConfig.user, 
                                        passwd=mysqlConfig.passwd,
                                        db=mysqlConfig.name, 
                                        use_unicode=False, 
                                        charset=mysqlConfig.char_set, 
                                        cursorclass=DictCursor, 
                                    )
        return MySqlUtil.__pool.connection()
    
    def dispose(self, isEnd=1):
        """
        @summary: 释放连接池资源
        """
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()

    def __getInsertId(self):
        """
        获取当前连接最后一次插入操作生成的id,如果没有则为０
        """
        self._cursor.execute("SELECT @@IDENTITY AS id")
        result = self._cursor.fetchall()
        return result[0]['id']

    def __query(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        return count

    def exec_sql(self, sql):
        """
        @summary: 执行sql操作
        @param sql: sql
        @return: count 受影响的行数
        """
        
        try:
            count = self._cursor.execute(sql)
            err = ""
        except Exception as e:
            count = -1
            Log.error("exec_sql", "{}".format(str(e)))
            err = str(e)
        
        SqlLog.record(sql, msg=err)
            
        return count

    def begin(self):
        """
        @summary: 开启事务
        """
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()
    
    def use_db(self, name):
        sql = "USE {}".format(name)
        self.exec_sql(sql=sql)
        
    def create_table_from_dict(self, db_name, table_name, dictData):
        """
        @summary: 创建新的表；字段直接用内部的
        @param db_name: 数据库名称
        @param dict: 表字段信息
        """

        values = ""

        Log.info("create_table_from_dict", "开始创建数据表: {0}".format(table_name))

        for key in dictData:
            p_name = key
            p_value = dictData[key]
            p_des = ""
            arr = p_name.split("#")
            if "#" in key and len(arr) == 2:
                p_name = arr[0]
                p_des = arr[1]
                
            values += "{0} {1} COMMENT '{2}', ".format(p_name, p_value, p_des)

        values = values[0: len(values) - 2]
        sql = "CREATE TABLE IF NOT EXISTS {0}.{1} ( {2} ) ENGINE=InnoDB DEFAULT CHARSET='utf8'".format(
            db_name, table_name, values)
        
        i = self.exec_sql(sql)
        if i >= 0:
            Log.success("create_table_from_dict", "{0} 创建成功！".format(table_name))

    def create_table_from_table_info(self, tableInfo):
        """
        @summary: 创建新的表；注意，字段会改成驼峰，首字母小写
        @param info: 表信息
        """

        values = ""
        dbName = tableInfo["dbName"]
        tableName = tableInfo["name"]
        columnList = tableInfo["columns"]

        for columnInfo in columnList:
            cName = columnInfo["name"]
            cProperty = columnInfo["columnProperty"]
            cDes = columnInfo["des"]
            values += "{0} {1} COMMENT '{2}', ".format(cName, cProperty, cDes)

        values = values[0: len(values) - 2]
        sql = "CREATE TABLE IF NOT EXISTS {0}.{1} ({2}) ENGINE=InnoDB DEFAULT CHARSET='utf8'".format(
            dbName, tableName, values)
        
        return self.exec_sql(sql)

    def create_db(self, dbName):
        return self.exec_sql(
            "CREATE DATABASE IF NOT EXISTS {0} CHARACTER SET utf8 COLLATE utf8_general_ci".format(dbName))

    #-------- 后期使用
    def get_all(self, sql, param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = []
        return result

    def get_one(self, sql, param=None):
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def get_many(self, sql, num, param=None):
        """
        @summary: 执行查询，并取出num条结果
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
            
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    def insert_one(self, sql):
        """
        @summary: 向数据表插入一条记录
        @param sql:要插入的ＳＱＬ格式
        @param value:要插入的记录数据tuple/list
        @return: insertId 受影响的行数
        """
        
        self._cursor.execute(sql)
        return self.__getInsertId()

    def insert_many(self, sql, values):
        """
        @summary: 向数据表插入多条记录
        @param sql:要插入的ＳＱＬ格式
        @param values:要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        count = self._cursor.executemany(sql, values)
        return count

    def update(self, sql, param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    def delete(self, sql, param=None):
        """
        @summary: 删除数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要删除的条件 值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)
