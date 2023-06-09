# 导入pymysql模块
import pymysql
from dbutils.pooled_db import PooledDB
from pymysql.cursors import DictCursor
from Core.file_manager import *
from Core.table_util import *

# 配置信息请核对清楚，一定不要在生产环境使用表生成工具！！！
class Config:
    DBHOST = "localhost"
    DBPORT = 3306
    DBUSER = "root"
    DBPWD = "123"
    DBNAME = "cleaner"
    DBCHAR = "utf8"


class MySqlConn:
    _conn = None
    _cursor = None
    __pool = None

    def __init__(self):
        # 从连接池中获取连接
        self._conn = MySqlConn.__getConn()
        self._cursor = self._conn.cursor()

    @staticmethod
    def __getConn():

        mysql_config = Config()

        if MySqlConn.__pool is None:
            MySqlConn.__pool = PooledDB(creator=pymysql, mincached=1, maxcached=20,
                                        host=mysql_config.DBHOST, port=mysql_config.DBPORT, user=mysql_config.DBUSER, passwd=mysql_config.DBPWD,
                                        db=mysql_config.DBNAME, use_unicode=False, charset=mysql_config.DBCHAR, cursorclass=DictCursor)
        return MySqlConn.__pool.connection()

    def getAll(self, sql, param=None):
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
            result = False
        return result

    def getOne(self, sql, param=None):
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

    def getMany(self, sql, num, param=None):
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

    def insertOne(self, sql, value):
        """
        @summary: 向数据表插入一条记录
        @param sql:要插入的ＳＱＬ格式
        @param value:要插入的记录数据tuple/list
        @return: insertId 受影响的行数
        """

        self._cursor.execute(sql, value)
        return self.__getInsertId()

    def execSql(self, sql):
        """
        @summary: 执行sql操作
        @param sql: sql
        @return: count 受影响的行数
        """
        count = self._cursor.execute(sql)
        return count

    def insertMany(self, sql, values):
        """
        @summary: 向数据表插入多条记录
        @param sql:要插入的ＳＱＬ格式
        @param values:要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        count = self._cursor.executemany(sql, values)
        return count

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

    def createTable(self, tableInfo):
        """
        @summary: 创建新的表
        @param info: 表信息
        """

        values = ""
        dbName = tableInfo["dbName"]
        tableName = tableInfo["name"]
        columnList = tableInfo["columns"]

        Log.info("Table", "开始创建数据表: {0}".format(tableName))

        for columnInfo in columnList:
            cName = TableUtil.instanceName(columnInfo["name"])
            cProperty = columnInfo["columnProperty"]
            cDes = columnInfo["des"]
            values += "{0} {1} COMMENT '{2}', ".format(cName, cProperty, cDes)

        values = values[0: len(values) - 2]
        str = "CREATE TABLE {0}.{1} ({2}) ENGINE=InnoDB DEFAULT CHARSET='utf8'".format(
            dbName, tableName, values)

        i = self.execSql(str)
        if i >= 0:
            Log.success("Table", "{0} 创建成功！".format(tableName))

    def createDB(self, dbName):
        Log.info("DB", "开始创建数据库：{0}".format(dbName))

        self.execSql(
            "CREATE DATABASE {0} CHARACTER SET utf8 COLLATE utf8_general_ci".format(dbName))
