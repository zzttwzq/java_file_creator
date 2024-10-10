import json
import os
import sys

#添加上级目录
sys.path.append("..//")
from Utils.mysql_util import MySqlUtil
from Utils.log_util import Log
from Utils.create_util import CreateUtil
from Utils.datetime_util import DateTimeUtil

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
        mysqlConfig=CreateUtil.get_mysql_config(info)
        dbCreator.sqlConnection = MySqlUtil(mysqlConfig)

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

    @staticmethod
    def schema(info, projectEnvPath):
        schemas = info["db"]["tableSchema"]
        liKeys = schemas.keys()
        tableList = []

        for key in liKeys:
            tableProps = schemas[key]
            tableTitle = key.split(":")
                
            if tableTitle[0][0:1] == "*":
                Log.info("schema", "自动跳过：{0}".format(tableTitle))
            else: 
                colums = [{
                    "name": "id",
                    "des": "记录id",
                    "columnProperty": "INT NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "formType": "number",
                    "showTime": 0,
                    "showInSearch": 0,
                    "showInForm": 0,
                    "required": 0,
                    "sort": "up",
                    "align": "center",
                    "width": 100,
                }]
                
                for li in tableProps:
                    columInfo = li.split(":")

                    width = 100
                    showInSearch = 1
                    showInForm = 1
                    required = 0
                    formType = "text"
                    columnProperty = columInfo[2]

                    coulumTypeTemp = {
                        "REAL": "number",
                        "TINYINT": "number",
                        "SMALLINT": "number",
                        "MEDIUMINT": "number",
                        "INT": "number",
                        "BIGINT": "number",
                        "FLOAT": "number",
                        "DOUBLE": "number",
                        "CHAR": "text",
                        "VARCHAR": "text",
                        "TINYTEXT": "textArea",
                        "TEXT": "textArea",
                        "MEDIUMTEXT": "textArea",
                        "LONGTEXT": "textArea",
                        "BOOL": "number",
                        "BOOLEAN": "number",
                        "DATETIME": "time",
                        "DATE": "time",
                        "TIME": "time",
                        "TIMESTAMP": "time",
                    }
                    columnProperty = columnProperty.split("(")[0].upper()
                    if columnProperty in coulumTypeTemp:
                        formType = coulumTypeTemp[columnProperty]
                    else:
                        formType = columnProperty

                    if len(columInfo) >= 4:
                        width = columInfo[3]

                    if len(columInfo) >= 5:
                        showInSearch = columInfo[4]

                    if len(columInfo) >= 6:
                        required = columInfo[5]

                    if len(columInfo) >= 7:
                        showInForm = columInfo[6]
                        
                    colums.append({
                        "name": CreateUtil.instance_name(columInfo[0]),
                        "des": columInfo[1],
                        "columnProperty": columInfo[2],
                        "formType": formType,
                        "showTime": 0,
                        "showInSearch": showInSearch,
                        "showInForm": showInForm,
                        "required": required,
                        "sort": "up",
                        "align": "left",
                        "width": width,
                    })

                colums.append({
                    "name": "createAt",
                    "des": "创建于",
                    "columnProperty": "DATETIME",
                    "formType": "date",
                    "showTime": 1,
                    "showInSearch": 1,
                    "showInForm": 0,
                    "required": 0,
                    "sort": "up",
                    "align": "center",
                    "width": 100,
                })
                colums.append({
                    "name": "updateAt",
                    "des": "更新于",
                    "columnProperty": "DATETIME",
                    "formType": "date",
                    "showTime": 1,
                    "showInSearch": 1,
                    "showInForm": 0,
                    "required": 0,
                    "sort": "up",
                    "align": "center",
                    "width": 100,
                })
                colums.append({
                    "name": "deleteAt",
                    "des": "删除于",
                    "columnProperty": "DATETIME",
                    "formType": "date",
                    "showTime": 1,
                    "showInSearch": 0,
                    "showInForm": 0,
                    "required": 0,
                    "sort": "up",
                    "align": "center",
                    "width": 100,
                })
        
                tableList.append({
                    "name": tableTitle[0],
                    "dbName": tableTitle[2],
                    "tableName": tableTitle[0],
                    "className": CreateUtil.camelize(tableTitle[0]),
                    "instanceName": CreateUtil.instance_name(tableTitle[0]),
                    "title": tableTitle[1],
                    "des": tableTitle[1],
                    "columns": colums
                })

        info["db"]["tableListOld"] = info["db"]["tableList"]
        info["db"]["tableList"] = tableList
            
        with open(projectEnvPath, "w") as f:
            json.dump(info, f, ensure_ascii=False)

        Log.success("schema", "tableList，生成成功")

    def create_db(self, dbNameList):
        Log.blank()
        Log.info(self.logPrefix,
                 "================ 正在生成数据库：`{0}` ================".format(dbNameList))
        
        for name in dbNameList:
            res = self.sqlConnection.create_db(name)
            if res == 0:
                Log.info(self.logPrefix, "数据库：'{0}' 已存在".format(name))
            elif res > 0:
                Log.success(self.logPrefix, "数据库：'{0}' 创建成功".format(name))
                
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
            res = self.sqlConnection.create_table_from_table_info(tableInfo)
            if res == 0:
                Log.info(self.logPrefix, "数据表：'{0}' 已存在".format(tableInfo["name"]))
            elif res > 0:
                Log.info(self.logPrefix, "数据表：'{0}' 创建成功".format(tableInfo["name"]))

    def create_seed(self, info, names):
        log_tag = "create_seed"
        
        Log.blank()
        Log.info(
            self.logPrefix, "================ 正在创建数据集 ================".format(names))
        
        tableList = tableList = CreateUtil.get_tables(info, names)
        tableInfoList = {}
        
        tableSeeds = info["db"]["tableSeed"]
        
        for it in tableList:
            if it["name"] in tableSeeds:
                tableInfoList[it["name"]] = it
                
        for key, value in tableSeeds.items():
            Log.blank()
            Log.info(log_tag, "新增seed：{}".format(key))
            
            for it in value:
                
                db_name = tableInfoList[key]["dbName"]
                table_name = tableInfoList[key]["name"]
                self.sqlConnection.use_db(db_name)
                
                it["createAt"] = DateTimeUtil.now_datetime()
                
                res = self.sqlConnection.insert(table_name, it)
                if res == 0:
                    Log.info(log_tag, "seed已存在：{}".format(it))
                elif res > 0:
                    Log.success(log_tag, "seed添加成功：{}".format(it))

    @staticmethod
    def _cmd_error():
        Log.info("db_create", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            db -all 生成所有的数据库，数据表，数据种子。\r\n \
            db -db [names] 生成新的数据库。\r\n \
            db -table [names] 生成新的表。\r\n \
            db -seed [names] 生成新的表。\r\n \
        ")