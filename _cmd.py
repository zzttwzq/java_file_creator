import sys
import os
import json
from Core.fileparser import *
from Core.file_manager import *
from Core.table_util import *
from Core.mysql import MySqlConn

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

from Creator.java_creator import *
from Creator.admin_creator import *
from Creator.uni_creator import *
from Creator.db_creator import *

# 项目配置文件
infoPath = "/Users/mac/Desktop/myblog/tableinfo.json"


class cmds:

    @staticmethod
    def checkCMD():
        if len(sys.argv) == 1:
            cmds.cmdError("")
            return

        info = TableUtil.getConfigInfo(path=infoPath)
        cmd = sys.argv[1]

        if cmd == "-all":
            TableCreator.create(info, "-db", info["dbName"])
            TableCreator.create(info, "-table", "-all")
            JavaCreator.create(info, "-all")
            AdminCreator.create(info, "-all")
            # UniCreator.create(info, "-all")

        elif cmd == "db":
            if len(sys.argv) > 2:
                mode = sys.argv[2]
                names = "-all"
                if len(sys.argv) > 3:
                    names = sys.argv[3]

                DBCreator.create(info, mode, names)
            else:
                DBCreator.cmdError()

        elif cmd == "schema":
            schemas = info["tableSchema"]
            liKeys = schemas.keys()
            tableList = []

            for key in liKeys:
                data = schemas[key]
                tableInfo = key.split("^")

                colums = []

                for li in data:
                    columInfo = li.split("^")

                    showInSearch = 0
                    required = 0
                    formType = "text"
                    columnProperty = columInfo[2]

                    if len(columInfo) >= 4:
                        formType = columInfo[3]
                    else:
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
                        formType = coulumTypeTemp[columnProperty]

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
                        "width": 100,
                        "formType": formType,
                        "showInSearch": showInSearch,
                        "required": required,
                    })

                tableList.append({
                    "name": tableInfo[0],
                    "des": tableInfo[1],
                    "title": tableInfo[2],
                    "columns": colums
                })

            info["tableList"] = tableList

            with open(infoPath, "w") as f:
                json.dump(info, f, ensure_ascii=False)

            Log.success("schema", "生成成功")

        elif cmd == "java":
            if len(sys.argv) > 2:
                mode = sys.argv[2]
                names = "-all"
                if len(sys.argv) > 3:
                    names = sys.argv[3]

                JavaCreator.create(info, mode, names)
            else:
                JavaCreator.cmdError()

        elif cmd == "admin":
            if len(sys.argv) > 2:
                mode = sys.argv[2]
                names = "-all"
                if len(sys.argv) > 3:
                    names = sys.argv[3]

                AdminCreator.create(info, mode, names)
            else:
                AdminCreator.cmdError()

        elif cmd == "uni":
            if len(sys.argv) > 2:
                mode = sys.argv[2]
                names = "-all"
                if len(sys.argv) > 3:
                    names = sys.argv[3]

                UniCreator.create(info, mode, names)
            else:
                UniCreator.cmdError()
        else:
            cmds.cmdError(cmd)

    @staticmethod
    def cmdError(cmd):
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
    try:
        cmds.checkCMD()
    except Exception as e:
        print(e)


__main__()
