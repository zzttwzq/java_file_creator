import sys
import json

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

from Utils.log_util import Log
from Utils.create_util import CreateUtil

from Creator.db_creator import DBCreator
from Creator.java_creator import JavaCreator
from Creator.admin_creator import AdminCreator
from Creator.uni_creator import UniCreator

# 项目配置文件
projectEnvPath = "/Users/wuzhiqiang/Documents/GitHub/blog/project.json"
# projectEnvPath = "/Users/wuzhiqiang/Desktop/mock/project.json"
# projectEnvPath = "/Users/wuzhiqiang/Documents/GitHub/itest/project.json"

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
            DBCreator.schema(info, projectEnvPath)

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
