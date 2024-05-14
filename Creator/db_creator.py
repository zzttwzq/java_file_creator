import os
from Core.file_manager import Log
from Core.mysql import MySqlConn

from Core.create_util import CreateUtil

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
        dbCreator.sqlConnection = MySqlConn(config= CreateUtil.get_mysql_config(info))

        # 执行操作
        # 数据库
        if mode == "-db":
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "未指定数据库名！")
            elif names == "-all":
                dbCreator.create_db(info["db"]["dbNames"])
            else:
                dbCreator.create_db([names])
        # 数据表
        elif mode == "-table":
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "创建数据表时未指定表名！")
            else:
                dbCreator.create_or_update_table(info, names)
        # 数据种子
        elif mode == "-seed":
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "创建数据集时未指定表名！")
            else:
                dbCreator.create_seed(info, names)
        # 创建所有
        elif mode == "-all":
            dbCreator.create_db()
            dbCreator.create_or_update_table(info, "-all")
            dbCreator.create_seed(info, "-all")
        # 命令错误
        else:
            DBCreator._cmd_error()
            
        dbCreator.sqlConnection.dispose()

    def create_db(self, dbNameList):
        Log.blank()
        Log.info(self.logPrefix,
                 "================ 正在生成数据库：`{0}` ================".format(dbNameList))
        
        for name in dbNameList:
            res = self.sqlConnection.create_db(name)
            if res:
                Log.success(self.logPrefix, "数据库：`{0}`创建成功".format(name))
            else:
                Log.error(self.logPrefix, "数据库：`{0}`创建失败".format(name))
                
    def create_or_update_table(self, info, names):
        Log.blank()
        Log.info(
            self.logPrefix, "================ 正在生成数据表 ================".format(names))
        
        tableList = CreateUtil.get_tables(info, names)
        if len(tableList) == 0:
            Log.error(self.logPrefix,
                      "{0} 在tableinfo.json 中未找到！".format(names))
            return
        
        for tableInfo in tableList:
            tableInfo["columns"] = CreateUtil.add_model_default_property(
                tableInfo["columns"])
            
            res = self.sqlConnection.create_table(tableInfo)
            
            if res:
                Log.success(self.logPrefix, "数据表：`{0}`创建成功".format(tableInfo["name"]))
            else:
                Log.error(self.logPrefix, "数据表：`{0}`创建失败".format(tableInfo["name"]))

    def create_seed(self, info, names):
        Log.blank()
        Log.info(
            self.logPrefix, "================ 正在创建数据集 ================".format(names))

        # my = MySqlConn(config= CreateUtil.get_mysql_config())
        # tableList = CreateUtil.get_tableInfo_width_names(info, names)
        # if len(tableList) == 0:
        #     Log.error(self.logPrefix,
        #               "{0} 在tableinfo.json 中未找到！".format(names))
        #     return
        
        # for seed in info["dbSeeds"]:
        #     try:
        #         my.insert_one(seed)
        #         Log.success(
        #             self.pathPrefix, "数据集：`{0}`创建成功".format(tableInfo["name"]))

        #     except Exception as e:
        #         Log.error(self.logPrefix, str(e))

        # my.dispose()

    @staticmethod
    def _cmd_error():
        Log.info("db_create", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            db -all 生成所有的数据库，数据表，数据种子。\r\n \
            db -db [names] 生成新的数据库。\r\n \
            db -table [names] 生成新的表。\r\n \
            db -seed [names] 生成新的表。\r\n \
        ")