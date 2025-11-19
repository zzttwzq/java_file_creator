# 导入pymysql模块
import pymysql
from dbutils.pooled_db import PooledDB
from pymysql.cursors import DictCursor
from Utils.log_util import Log, SqlLog

class MySqlConfig:
    host = "127.0.0.1"
    port = 3306
    user = ""
    passwd = ""
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

    def exec_sql(self, sql, value_list=()):
        """
        @summary: 执行sql操作
        @param sql: sql
        @return: count 受影响的行数
        """
        
        err = ""
        try:
            if len(value_list) > 0:
                count = self._cursor.execute(sql, value_list)
            else:
                count = self._cursor.execute(sql)
                
        except Exception as e:
            
            err = str(e)
            if "Duplicate entry" in err:
                count = 0
                Log.warn("DB", "\r\n    -> " + sql + "\r\n    -> " + str(value_list) + "\r\n    -> " +err)
            else:
                count = -1
                Log.error("DB", "\r\n    -> " + sql + "\r\n    -> " + str(value_list) + "\r\n    -> " +err)
            
        
        SqlLog.record("\r\n    -> " + sql + "\r\n    -> " + str(value_list) + "\r\n    -> " +err)
            
        return count

    #-------- 现成方法
    
    def create_db(self, name) -> int:
        """
        创建新的数据库
        
        参数:
            name(string): 数据库名称
        
        返回:
            int: 影响行数
        
        引发:
        """
        
        sql = "CREATE DATABASE IF NOT EXISTS `{}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci".format(name)
        res = self.exec_sql(sql)
        return res

    def use_db(self, name) -> int:
        """
        使用数据库
        
        参数:
            db_name(string): 数据库名称
        
        返回:
            int: 影响行数
        
        引发:
        """
        
        sql = "USE {}".format(name)
        res = self.exec_sql(sql)
        return res
        
    def create_table_from_dict(self, db_name, table_name, dict_data) -> int:
        """
        创建新的表
        
        参数:
            db_name(string): 数据库名称
            table_name(string): 数据表
            dict_data(string): 带有数据表信息的dict
        
        返回:
            int: 影响行数
        
        引发:
        """

        values = ""
        for key in dict_data:
            p_name = key
            p_value = dict_data[key]
            p_des = ""
            arr = p_name.split("#")
            if "#" in key and len(arr) == 2:
                p_name = arr[0]
                p_des = arr[1]
                
            values += "{0} {1} COMMENT '{2}', ".format(p_name, p_value, p_des)

        values = values[0: len(values) - 2]
        sql = "CREATE TABLE IF NOT EXISTS `{0}`.`{1}` ( {2} ) ENGINE=InnoDB DEFAULT CHARSET='utf8mb4'".format(
            db_name, table_name, values)
        
        return self.exec_sql(sql)

    def create_table_from_table_info(self, table_info)-> int:
        """
        创建新的表；使用project.json里面的配置
        
        参数:
            table_info(string): 数据表信息的dict
        
        返回:
            int: 影响行数
        
        引发:
        """

        values = ""
        dbName = table_info["dbName"]
        tableName = table_info["name"]
        columnList = table_info["columns"]

        for columnInfo in columnList:
            cName = columnInfo["name"]
            cProperty = columnInfo["columnProperty"]
            cDes = columnInfo["des"]
            if cName == "create_at":
                values += "{0} {1} DEFAULT CURRENT_TIMESTAMP COMMENT '{2}', ".format(cName, cProperty, cDes)
            elif cName == "update_at":
                values += "{0} {1} DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '{2}', ".format(cName, cProperty, cDes)
            else:
                values += "{0} {1} COMMENT '{2}', ".format(cName, cProperty, cDes)

        values = values[0: len(values) - 2]
        sql = "CREATE TABLE IF NOT EXISTS `{0}`.`{1}` ({2}) ENGINE=InnoDB DEFAULT CHARSET='utf8mb4'".format(
            dbName, tableName, values)
        
        return self.exec_sql(sql)

    def begin(self):
        """
        开启事务
        """
        
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """
        结束事务
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()
    
    def get_all(self, sql, param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """

        errorString = ""
        try:
            if param is None:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, param)
            if count > 0:
                result = self._cursor.fetchall()
            else:
                result = []
                
        except Exception as e:
            result = []
            errorString = str(e)
            Log.error("DB", "\r\n    -> " + sql + "\r\n    -> " + str(param) + "\r\n    -> " +errorString)
            
        SqlLog.record("\r\n    -> " + sql + "\r\n    -> " + str(param) + "\r\n    -> " +errorString)

        return result
    
    def get_many(self, table_name, condition="", value_list=[], columns = "*", num=0):
        """
        @summary: 执行查询，并取出num条结果
        @param table_name: 表名称
        @param condition: ＳＱＬ格式及条件，使用(%s,%s)；比如：id = %s
        @param value_list: 条件值对应的数组；比如：[10]
        @param columns: 对应的字段；比如：name, age
        @return: result list/boolean 查询到的结果集
        """
        
        sql = ""        
        if len(condition) == 0:
            sql = "SELECT {} FROM {};".format(columns, table_name)
        else:
            sql = "SELECT {} FROM {} {};".format(columns, table_name, condition)
        self.exec_sql(sql, value_list)
            
        result = []
        if num == 0:
            result = self._cursor.fetchall()
        else:
            result = self._cursor.fetchmany(num)
                
        return result
    
    def __getInsertId(self):
        """
        获取当前连接最后一次插入操作生成的id,如果没有则为０
        """
        
        self._cursor.execute("SELECT @@IDENTITY AS id")
        result = self._cursor.fetchall()
        return result[0]['id']
    
    def insert(self, table_name, dict) -> int:
        """
        @summary: 插入数据表记录
        @param table_name: 表名称
        @param dict: 键值对
        @return: id值
        """
        
        keys = "" 
        values = ""
        param_list = []
        for k in dict:
            keys += "{}, ".format(k)
            values += "{}, ".format("%s")
            param_list.append(dict[k])
                    
        keys = keys[0: len(keys) - 2]
        values = values[0: len(values) - 2]
        sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name, keys, values)
        
        res = self.exec_sql(sql, param_list) >= 0
        if res:
            return self.__getInsertId()
        else:
            return -1
    
    def update(self, table_name, dict, condition, value_list) -> bool:
        """
        @summary: 更新数据表记录
        @param table_name: 表名称
        @param dict: 键值对
        @param condition: WHERE 后面的ＳＱＬ格式及条件，使用(%s,%s)；比如：id = %s
        @param value_list: 条件值对应的数组；比如：[10]
        @return: 是否成功
        """
        
        kvs = ""
        param_list = []
        for k in dict:
            kvs += "{} = %s, ".format(k)
            param_list.append(dict[k])
            
        for it in value_list:
            param_list.append(it)
                    
        kvs = kvs[0: len(kvs) - 2]
        sql = "UPDATE {} SET {} WHERE {}".format(table_name, kvs, condition)
        
        res = self.exec_sql(sql, param_list) >= 0
        return res

    def delete(self, table_name, condition, value_list) -> bool:
        """
        @summary: 删除数据表记录
        @param table_name: 表名称
        @param condition: WHERE 后面的ＳＱＬ格式及条件，使用(%s,%s)；比如：id = %s
        @param value_list: 条件值对应的数组；比如：[10]
        @return: 是否成功
        """
        
        param_list = value_list
                    
        kvs = kvs[0: len(kvs) - 2]
        values1 = values1[0: len(values1) - 2]
        sql = "DELETE FROM {} WHERE {}".format(table_name, condition)
        
        res = self.exec_sql(sql, param_list) >= 0
        return res
