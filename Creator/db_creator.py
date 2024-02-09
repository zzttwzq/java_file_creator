import os
from Core.file_manager import *
from Core.table_util import *
from Core.mysql import MySqlConn


class DBCreator:
    dirs = ["back"]
    logPath = os.getcwd()+"/Log/"
    pathPrefix = os.getcwd()+"/dist/table/"
    logPrefix = "DB"

    @staticmethod
    def create(info, mode, names):

        dbCreator = DBCreator()

        # ------------ 执行操作
        if mode == "-db":
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "未指定数据库名！")
            else:
                dbCreator.createDB(names)

        elif mode == "-table":
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "创建数据表时未指定表名！")
            else:
                dbCreator.createOrUpdateTable(info, names)

        elif mode == "-seed":
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "创建数据集时未指定表名！")
            else:
                dbCreator.createSeed(info, names)

        elif mode == "-all":
            dbName = info["dbName"]
            dbCreator.createDB(dbName)
            dbCreator.createOrUpdateTable(info, "-all")
            dbCreator.createSeed(info, "-all")

    def createDB(self, dbName):
        Log.blank()
        Log.info(self.logPrefix,
                 "================ 正在生成数据库：`{0}` ================".format(dbName))
        my = MySqlConn()
        try:
            my.createDB(dbName)
            Log.success(self.logPrefix, "数据库：`{0}`创建成功".format(dbName))

        except Exception as e:
            Log.error(self.logPrefix, str(e))

        my.dispose()

    def createOrUpdateTable(self, info, names):
        Log.blank()
        Log.info(
            self.logPrefix, "================ 正在生成数据表 ================".format(names))

        my = MySqlConn()
        tableList = TableUtil.getTableInfoWidthNames(info, names)
        if len(tableList) == 0:
            Log.error(self.logPrefix,
                      "{0} 在tableinfo.json 中未找到！".format(names))
            return
        
        for tableInfo in tableList:
            tableInfo["dbName"] = info["dbName"]
            tableInfo["columns"] = TableUtil.addModelDefaultProperty(
                tableInfo["columns"])

            try:
                my.createTable(tableInfo)
                Log.success(
                    self.pathPrefix, "数据表：`{0}`创建成功".format(tableInfo["name"]))

            except Exception as e:
                Log.error(self.logPrefix, str(e))

        my.dispose()

    def createSeed(self, info, names):
        Log.blank()
        Log.info(
            self.logPrefix, "================ 正在创建数据集 ================".format(names))

        # my = MySqlConn()
        # tableList = TableUtil.getTableInfoWidthNames(info, names)
        # if len(tableList) == 0:
        #     Log.error(self.logPrefix,
        #               "{0} 在tableinfo.json 中未找到！".format(names))
        #     return
        
        # for seed in info["dbSeeds"]:
        #     try:
        #         my.insertOne(seed)
        #         Log.success(
        #             self.pathPrefix, "数据集：`{0}`创建成功".format(tableInfo["name"]))

        #     except Exception as e:
        #         Log.error(self.logPrefix, str(e))

        # my.dispose()

    @staticmethod
    def cmdError():
        Log.info("db_create", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            db -db [names] 生成新的数据库。\r\n \
            db -table [names] 生成新的表。\r\n \
            db -seed [names] 生成新的表。\r\n \
        ")
