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

from Creator.java_creator import *
from Creator.admin_creator import *
from Creator.uni_creator import *
from Creator.table_creator import *

class cmds:

    @staticmethod
    def checkCMD() :
        c = cmds()

        cmd = sys.argv[1]

        if cmd == "-all":
            JavaCreator.create("-all")
            AdminCreator.create("-all")
            UniCreator.create("-all")

        elif cmd == "table":

            if len(sys.argv) > 2:
                mode = sys.argv[2]

            if len(sys.argv) > 3:
                param = sys.argv[3]

            TableCreator.create(mode, param)

        elif cmd == "java":
            mode = sys.argv[2]
            if len(sys.argv) > 3 or mode == "-all":
                if mode == "-all":
                    JavaCreator.create("-all")
                elif mode == "-n":
                    names = sys.argv[3]
                    JavaCreator.create(names)
                elif mode == "-d":
                    JavaCreator.create("-d")
            else:
                Log.error("错误", "命令错误！")

        elif cmd == "admin":
            mode = sys.argv[2]
            if len(sys.argv) > 3 or mode == "-all":
                if mode == "-all":
                    AdminCreator.create("-all")
                elif mode == "-n":
                    names = sys.argv[3]
                    AdminCreator.create(names)
                elif mode == "-d":
                    AdminCreator.create("-d")
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

def __main__() :
    cmds.checkCMD()

__main__()