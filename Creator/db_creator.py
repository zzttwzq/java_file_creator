import os
from Core.file_manager import *
from Core.mysql import MySqlConn

from Core.create_util import *

class DBCreator:
    dirs = ["back"]
    logPath = os.getcwd()+"/Log/"
    pathPrefix = os.getcwd()+"/dist/table/"
    logPrefix = "DB"
    
    sqlConnection = ""

    @staticmethod
    def create(info, mode, names):
        dbCreator = DBCreator()
        # 数据库
        dbCreator.sqlConnection = MySqlConn(config= CreateUtil.getMysqlConfig(info))

        # 执行操作
        # 数据库
        if mode == "-db":
            print(names)
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "未指定数据库名！")
            elif names == "-all":
                dbCreator.createDB(info["db"]["dbNames"])
            else:
                dbCreator.createDB([names])
        # 数据表
        elif mode == "-table":
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "创建数据表时未指定表名！")
            else:
                dbCreator.createOrUpdateTable(info, names)
        # 数据种子
        elif mode == "-seed":
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "创建数据集时未指定表名！")
            else:
                dbCreator.createSeed(info, names)
        # 创建所有
        elif mode == "-all":
            dbCreator.createDB()
            dbCreator.createOrUpdateTable(info, "-all")
            dbCreator.createSeed(info, "-all")
        # 命令错误
        else:
            DBCreator.cmdError()
            
        dbCreator.sqlConnection.dispose()

    def createDB(self, dbNameList):
        Log.blank()
        Log.info(self.logPrefix,
                 "================ 正在生成数据库：`{0}` ================".format(dbNameList))
        try:
            for name in dbNameList:
                self.sqlConnection.createDB(name)
                Log.success(self.logPrefix, "数据库：`{0}`创建成功".format(name))
        except Exception as e:
            Log.error(self.logPrefix, "数据库：`{0}`创建失败：${1}".format(name, str(e)))

    def createOrUpdateTable(self, info, names):
        Log.blank()
        Log.info(
            self.logPrefix, "================ 正在生成数据表 ================".format(names))
        
        tableList = CreateUtil.getTables(info, names)
        if len(tableList) == 0:
            Log.error(self.logPrefix,
                      "{0} 在tableinfo.json 中未找到！".format(names))
            return
        
        for tableInfo in tableList:
            tableInfo["columns"] = CreateUtil.addModelDefaultProperty(
                tableInfo["columns"])

            try:
                self.sqlConnection.createTable(tableInfo)

            except Exception as e:
                Log.error(self.logPrefix, "数据表：`{0}`创建失败：".format(tableInfo["name"], str(e)))

    def createSeed(self, info, names):
        Log.blank()
        Log.info(
            self.logPrefix, "================ 正在创建数据集 ================".format(names))

        # my = MySqlConn(config= CreateUtil.getMysqlConfig())
        # tableList = CreateUtil.getTableInfoWidthNames(info, names)
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
            db -all 生成所有的数据库，数据表，数据种子。\r\n \
            db -db [names] 生成新的数据库。\r\n \
            db -table [names] 生成新的表。\r\n \
            db -seed [names] 生成新的表。\r\n \
        ")