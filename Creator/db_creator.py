import os
from Core.file_manager import *
from Core.table_util import *
from Core.mysql import MySqlConn


class DBCreator:
    dirs = ["back"]
    logPath = os.getcwd()+"/Log/"
    pathPrefix = os.getcwd()+"/dist/table/"

    @staticmethod
    def create(info, mode, names):

        dbCreator = DBCreator()

        # ------------ 执行操作
        if mode == "-table":
            if len(names) == 0:
                Log.error("db", "未指定表名！")
            else:
                dbCreator.createTable(info, names)

        elif mode == "-db":
            if len(names) == 0:
                Log.error("db", "未指定数据库名！")
            else:
                dbCreator.createDB(names)
        elif mode == "-seed":
            dbCreator.createSeed(info)

    def createTable(self, info, names):
        Log.blank()
        Log.info(
            "table_create", "================ 正在为`{0}`生成table ================".format(names))

        my = MySqlConn()
        tableList = TableUtil.getTableInfoWidthNames(info, names)
        if len(tableList) == 0:
            Log.error("Table", "{0} 在tableinfo.json 中未找到！".format(names))
        for tableInfo in tableList:
            tableInfo["dbName"] = info["dbName"]
            tableInfo["columns"] = TableUtil.addModelDefaultProperty(
                tableInfo["columns"])
            my.createTable(tableInfo)
            Log.success(
                "table_create", "生成数据表：`{0}`成功".format(tableInfo["name"]))

    def createDB(self, dbName):
        Log.blank()
        Log.info(
            "table_create", "================ 正在生成数据库：`{0}` ================".format(dbName))
        my = MySqlConn()
        my.createDB(dbName)
        Log.success(
            "table_create", "生成数据库：`{0}`成功".format(dbName))

    def createSeed(self, info):
        print("not found!")

    @staticmethod
    def cmdError():
        Log.info("db_create", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            db -db [names] 生成新的数据库。\r\n \
            db -table [names] 生成新的表。\r\n \
        ")
