import json
import os
import time
import sys

#添加上级目录
sys.path.append("..//")
from Utils.mysql_util import MySqlUtil
from Utils.log_util import Log
from Utils.create_util import CreateUtil
from Utils.datetime_util import DateTimeUtil
from Utils.file_util import FileUtil

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
        m = CreateUtil.get_work_config()
        # isLocal = m["dbSource"] == "local"
        Log.warn("db", f"<<<<<<<<<<<<<<<< 数据库环境：{m['dbSource']} >>>>>>>>>>>>>>>>")

        mysqlConfig=CreateUtil.get_mysql_config(info, m["dbSource"])
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
                dbCreator.create_table_struct(info, "-all")
        # 数据种子 
        elif mode == "-seed":
            if len(names) == 0:
                Log.error(dbCreator.logPrefix, "创建数据集时未指定表名！")
            else:
                dbCreator.create_seed(info, names)
        # 数据种子
        elif mode == "-sql":
            sql = ""
            dbCreator.run_sql()
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
    def schema(info, projectPath):
        Log.info("schema", "================ 开始生成schema内容 ================")

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
                    "columnProperty": "BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "formType": "number",
                    "showTime": 0,
                    "showInSearch": 0,
                    "showInForm": 0,
                    "required": 0,
                    "sort": "up",
                    "align": "center",
                    "width": 100,
                }]
                
                optionMap = "{\n"

                for li in tableProps:
                    columInfo = li.split(":")

                    width = "auto"
                    showInSearch = 1
                    showInForm = 1
                    required = 0
                    showTime = 0
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
                        "DATETIME": "date",
                        "DATE": "date",
                        "TIME": "time",
                        "TIMESTAMP": "time",
                    }
                    columnProperty = columnProperty.split("(")[0].upper()
                    if columnProperty in coulumTypeTemp:
                        formType = coulumTypeTemp[columnProperty]
                    else:
                        formType = columnProperty

                    options = "[\n"
                    isSelect = False
                    l = columInfo[1].split(" ")
                    if len(l) > 1 and "." in columInfo[1]:
                        l.pop(0)
                        isSelect = True

                        name = CreateUtil.instance_name(columInfo[0])
                        optionMap += f"        {name}Map: " + "{\n"
                        for it in l:
                            ss = it.split(".")
                            options += "            {\n"
                            options += f'              label: "{ss[1]}",\n'
                            options += f"              value: {ss[0]},\n"
                            options += "            },\n"

                            optionMap += f'          {ss[0]}: "{ss[1]}",\n'
                        optionMap += "        },\n"

                    options += "          ],\n"

                    if isSelect:
                        formType = "select"

                    if len(columInfo) >= 4:
                        width = columInfo[3]

                    if len(columInfo) >= 5:
                        showInSearch = columInfo[4]

                    if len(columInfo) >= 6:
                        required = columInfo[5]

                    if len(columInfo) >= 7:
                        showInForm = columInfo[6]
                        
                    if formType == "date" or formType == "time":
                        showTime = 1
                    
                    obj = {
                        "name": columInfo[0],
                        "des": columInfo[1],
                        "columnProperty": columInfo[2],
                        "formType": formType,
                        "showTime": showTime,
                        "showInSearch": showInSearch,
                        "showInForm": showInForm,
                        "required": required,
                        "sort": "up",
                        "align": "left",
                        "options": options,
                    }
                    if width != "auto":
                        obj["width"] = int(width)
                    else:
                        obj["width"] = width

                    colums.append(obj)

                colums.append({
                    "name": "create_at",
                    "des": "创建于",
                    "columnProperty": "DATETIME",
                    "formType": "date",
                    "showTime": 1,
                    "showInSearch": 1,
                    "showInForm": 0,
                    "required": 0,
                    "sort": "up",
                    "align": "center",
                    "width": "auto",
                })
                colums.append({
                    "name": "update_at",
                    "des": "更新于",
                    "columnProperty": "DATETIME",
                    "formType": "date",
                    "showTime": 1,
                    "showInSearch": 1,
                    "showInForm": 0,
                    "required": 0,
                    "sort": "up",
                    "align": "center",
                    "width": "auto",
                })
                colums.append({
                    "name": "delete_at",
                    "des": "删除于",
                    "columnProperty": "DATETIME",
                    "formType": "date",
                    "showTime": 1,
                    "showInSearch": 0,
                    "showInForm": 0,
                    "required": 0,
                    "sort": "up",
                    "align": "center",
                    "width": "auto",
                })
        
                if tableTitle[0][0:1] == "-":
                    tableTitle[0] = tableTitle[0].replace("-", "")
                if tableTitle[0][0:1] == "+":
                    tableTitle[0] = tableTitle[0].replace("+", "")

                optionMap += "      },\n"

                tableList.append({
                    "name": tableTitle[0],
                    "dbName": tableTitle[2],
                    "tableName": tableTitle[0],
                    "className": CreateUtil.camelize(tableTitle[0]),
                    "instanceName": CreateUtil.instance_name(tableTitle[0]),
                    "title": tableTitle[1],
                    "des": tableTitle[1],
                    # "admin_menu": admin_menu,
                    "showPage": "",
                    "optionMap": optionMap,
                    "columns": colums
                })

        # 写入到文件
        times = time.strftime("%Y-%m%d_%H_%M_%S")
        file_name_old = f"{projectPath}_Temp/tableList_{times}.json"
        file_name = f"{projectPath}_Temp/tableList.json"
        if os.path.exists(file_name):
            FileUtil.rename(file_name, file_name_old)

        with open(file_name, "w") as f:
            json.dump(tableList, f, indent=2, ensure_ascii=False)  # indent 实现格式化缩进

        Log.success("schema", "===============> 生成成功 ")

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
         
        tableList = CreateUtil.get_tableInfo_width_names(info, names)
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

    def create_table_struct(self, info, names):
        Log.blank()
        Log.info(
            self.logPrefix, "================ 正在生成数据表结构 ================".format(names))
        
        tableList = CreateUtil.get_tableInfo_width_names(info, names)
        
        sql1 = ""
        for tableInfo in tableList:
            tableInfo

            values = ""
            dbName = tableInfo["dbName"]
            tableName = tableInfo["name"]
            columnList = tableInfo["columns"]

            for columnInfo in columnList:
                cName = columnInfo["name"]
                cProperty = columnInfo["columnProperty"]
                cDes = columnInfo["des"]
                values += "\n  {0} {1}".format(cName, cProperty, cDes)

            # values = values[0: len(values) - 2]
            sql = f"\nTABLE `{dbName}`.`{tableName}` " + "{" + f"{values}" + "\n}"
            # Log.info("create_table_struct", sql)
            sql1 += sql; 

        projectPath = info["path"]
        p = f"{projectPath}_Temp/table.txt"
        Log.info(p)
        FileUtil.write_file(sql1, p);
    
    def create_seed(self, info, names):
        log_tag = "create_seed"
        
        Log.blank()
        Log.info(
            self.logPrefix, "================ 正在创建数据集 ================".format(names))
        
        tableList = CreateUtil.get_tableInfo_width_names(info, names)
        tableInfoList = {}
        
        tableSeeds = info["db"]["tableSeed"]
        
        for it in tableList:
            if it["name"] in tableSeeds:
                tableInfoList[it["name"]] = it
                
        for key, value in tableSeeds.items():
            Log.blank()
            Log.info(log_tag, "新增seed：{}".format(key))
            
            for it in value:
                # print(tableInfoList)
                # print(tableInfoList[key])
                db_name = tableInfoList[key]["dbName"]
                table_name = tableInfoList[key]["name"]
                self.sqlConnection.use_db(db_name)
                
                # if "create_at" in it.keys():
                it["create_at"] = DateTimeUtil.now_datetime()
                
                new_data = {}
                for k, v in it.items():
                    if k != "@":
                        new_data[k] = v
                
                res = self.sqlConnection.insert(table_name, new_data)
                if res == 0:
                    Log.info(log_tag, "seed已存在：{}".format(new_data))
                elif res > 0:
                    Log.success(log_tag, "seed添加成功：{}".format(new_data))

    def run_sql(self):
        dirPath = "/Users/wuzhiqiang/Desktop/生命涌 现/table/"
        
        # 获取目录下的所有文件
        file_list = []
        if os.path.exists(dirPath):
            for file_name in os.listdir(dirPath):
                file_path = os.path.join(dirPath, file_name)
                if os.path.isfile(file_path):
                    file_list.append(file_path)
        
        # 读取文件内容并通过INSERT分割字符串放到数组里
        sql_commands = []
        for file_path in file_list:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # 通过INSERT分割字符串
                    insert_statements = content.split('INSERT')
                    for stmt in insert_statements:
                        if stmt.strip():  # 跳过空字符串
                            sql_commands.append('INSERT' + stmt.strip())
            except Exception as e:
                Log.error(self.logPrefix, f"读取文件 {file_path} 失败: {e}")
        
        Log.blank()
        Log.info(self.logPrefix, f"找到 {len(file_list)} 个文件，提取出 {len(sql_commands)} 条SQL语句")
        
        # 执行所有SQL语句
        success_count = 0
        for sql in sql_commands:
            res = self.sqlConnection.exec_sql(sql)
            if res > 0:
                success_count += 1
                Log.info(self.logPrefix, f"SQL执行成功: {sql[:100]}...")
            else:
                Log.error(self.logPrefix, f"SQL执行失败: {sql[:100]}...")
        
        if success_count == len(sql_commands):
            Log.success(self.logPrefix, f"所有SQL执行成功，共 {success_count} 条")
        else:
            Log.error(self.logPrefix, f"SQL执行完成，成功 {success_count}/{len(sql_commands)} 条")

    @staticmethod
    def _cmd_error():
        Log.info("db_create", "命令错误：\r\n \
            尝试以下命令：\r\n \
            db -all 生成所有的数据库，数据表，数据种子。\r\n \
            db -db [names] 生成新的数据库。\r\n \
            db -table [names] 生成新的表。\r\n \
            db -seed [names] 生成新的表。\r\n \
        ")