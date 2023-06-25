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
from Creator.table_creator import *

# 项目配置文件
infoPath = "/Users/mac/Desktop/myblog/tableinfo.json"


class cmds:

    @staticmethod
    def checkCMD():

        if len(sys.argv) == 1:
            Log.error("cmd", "请输入命令！")
            return

        info = TableUtil.getConfigInfo(path=infoPath)
        cmd = sys.argv[1]
        # cmd2 = sys.argv[1]

        if cmd == "-all":
            JavaCreator.create("-all")
            AdminCreator.create("-all")
            UniCreator.create("-all")

        elif cmd == "table":

            if len(sys.argv) > 2:
                mode = sys.argv[2]

            if len(sys.argv) > 3:
                param = sys.argv[3]

            TableCreator.create(info, mode, param)

        elif cmd == "schema":

            # if "tableSchema" in info.keys() == False:
            #     Log.error("cmd", "不存在 tableSchema")
            #     return

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
                    else :
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
            mode = sys.argv[2]
            if len(sys.argv) > 3 or mode == "-all":
                if mode == "-all":
                    JavaCreator.create(info, "-all")
                elif mode == "-d":
                    JavaCreator.create(info, "-d")
                else:
                    names = sys.argv[3]
                    JavaCreator.create(info, names)
            else:
                Log.error("错误", "命令错误！")

        elif cmd == "admin":
            mode = sys.argv[2]
            if len(sys.argv) > 3 or mode == "-all":
                if mode == "-all":
                    AdminCreator.create(info, "-all")
                elif mode == "-d":
                    AdminCreator.create(info, "-d")
                else:
                    names = sys.argv[3]
                    AdminCreator.create(info, names)
            else:
                Log.error("错误", "命令错误！")

        elif cmd == "uni":
            mode = sys.argv[2]
            if len(sys.argv) > 3 or mode == "-all":
                if mode == "-all":
                    UniCreator.create("-all")
                elif mode == "-n":
                    names = sys.argv[3]
                    UniCreator.create(names)
                elif mode == "-d":
                    UniCreator.create("-d")
            else:
                Log.error("错误", "命令错误！")

        if cmd == "":
            Log.error("错误", "未知命令")


def __main__():
    cmds.checkCMD()


__main__()
