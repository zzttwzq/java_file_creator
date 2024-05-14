import sys
import json
from Core.file_manager import Log

# colum_type_list = [
#     'TINYINT', 'SMALLINT', 'MEDIUMINT', 'INT', 'BIGINT',
#     'FLOAT', 'DOUBLE', 'DOUBLE PRECISION', 'REAL', 'DECIMAL',
#     'BIT', 'SERIAL', 'BOOL', 'BOOLEAN', 'DEC',
#     'FIXED', 'NUMERIC', 'CHAR', 'VARCHAR', 'TINYTEXT',
#     'TEXT', 'MEDIUMTEXT', 'LONGTEXT', 'TINYBLOB', 'MEDIUMBLOB',
#     'BLOB', 'LONGBLOB', 'BINARY', 'VARBINARY', 'ENUM',
#     'SET', 'DATE', 'DATETIME', 'TIMESTAMP', 'TIME',
#     'YEAR', 'GEOMETRY', 'POINT', 'LINESTRING', 'POLYGON',
#     'MULTIPOINT', 'MULTILINESTRING', 'MULTIPOLYGON', 'GEOMETRYCOLLECTION']

# colum_view_type = [
#     "text", *
#     "textArea", *
#     "number", * 
#     "numberRange",
#     "select",
#     "date", *
#     "time",
#     "dateRange",
#     "radioGroup",
#     "checkboxGroup",
# ]

from Creator.db_creator import DBCreator
from Creator.java_creator import JavaCreator
from Creator.admin_creator import AdminCreator
from Creator.uni_creator import UniCreator
from Core.create_util import CreateUtil

# 项目配置文件
projectEnvPath = "/Users/wuzhiqiang/Documents/GitHub/blog/project.json"

class cmds:

    @staticmethod
    def checkCMD():
        if len(sys.argv) == 1:
            cmds._cmd_error("")
            return

        info = CreateUtil.get_config_info(path=projectEnvPath)
        cmd = sys.argv[1]

        if cmd == "-all":
            DBCreator.create(info, "-all")
            JavaCreator.create(info, "-all")
            AdminCreator.create(info, "-all")
            UniCreator.create(info, "-all")

        elif cmd == "db":
            if len(sys.argv) > 2:
                mode = sys.argv[2]
                names = "-all"
                if len(sys.argv) > 3:
                    names = sys.argv[3]

                DBCreator.create(info, mode, names)
            else:
                DBCreator._cmd_error()

        elif cmd == "schema":
            schemas = info["db"]["tableSchema"]
            liKeys = schemas.keys()
            tableList = []

            for key in liKeys:
                tableProps = schemas[key]
                tableTitle = key.split(":")
                
                if tableTitle[0][0:1] == "*":
                    Log.info("schema", "自动跳过：{0}".format(tableTitle))
                else: 
                    colums = []
                    for li in tableProps:
                        columInfo = li.split(":")

                        width = 100
                        showInSearch = 1
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

                        colums.append({
                            "name": columInfo[0],
                            "des": columInfo[1],
                            "columnProperty": columInfo[2],
                            "sort": "up",
                            "align": "left",
                            "width": width,
                            "formType": formType,
                            "showInSearch": showInSearch,
                            "required": required,
                        })

                    tableList.append({
                        "name": tableTitle[0],
                        "title": tableTitle[1],
                        "des": tableTitle[1],
                        "dbName": tableTitle[2],
                        "columns": colums
                    })

            info["db"]["tableListOld"] = info["db"]["tableList"]
            info["db"]["tableList"] = tableList
            
            with open(projectEnvPath, "w") as f:
                json.dump(info, f, ensure_ascii=False)

            Log.success("schema", "tableList，生成成功")

        elif cmd == "java":
            if len(sys.argv) > 2:
                mode = sys.argv[2]
                names = "-all"
                if len(sys.argv) > 3:
                    names = sys.argv[3]

                JavaCreator.create(info, mode, names)
            else:
                JavaCreator._cmd_error()

        elif cmd == "admin":
            if len(sys.argv) > 2:
                mode = sys.argv[2]
                names = "-all"
                if len(sys.argv) > 3:
                    names = sys.argv[3]

                AdminCreator.create(info, mode, names)
            else:
                AdminCreator._cmd_error()

        elif cmd == "uni":
            if len(sys.argv) > 2:
                mode = sys.argv[2]
                names = "-all"
                if len(sys.argv) > 3:
                    names = sys.argv[3]

                UniCreator.create(info, mode, names)
            else:
                UniCreator._cmd_error()
        else:
            cmds._cmd_error(cmd)

    @staticmethod
    def _cmd_error(cmd):
        Log.info("_cmd", "命令错误 [{0}]：\r\n \
            尝试以下命令：、\r\n  \
            -all 生成所有内容。\r\n \
            db -[option] 数据库相关。\r\n \
            schema 根据tableinfo.json中的schema数组生成表和字段列表。\r\n \
            java -[option] 生成page文件。\r\n \
            admin -[option] 生成router路由。\r\n \
            uni -[option] 生成api信息。\r\n \
            java -request 生成request文件。\r\n \
        ".format(cmd))

def __main__():
    cmds.checkCMD()
    
__main__()
