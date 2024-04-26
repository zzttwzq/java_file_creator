import os
import time
import sys
import traceback
import logging
import threading


class file_manager:
    f = ''

    @staticmethod
    def getBaseDir():
        return os.path.abspath('..')

    @staticmethod
    def getCurrentDir():
        return os.path.abspath('.')

    def __init__(self, path):
        file_path = path
        # print(file_path)
        self.f = open(file_path, 'w+', encoding='utf-8')

    def read(self):
        c = self.f.readlines()
        return c

    def write(self, string):
        self.f.write(string)

    def close(self):
        self.f.close()

    @staticmethod
    def checkFilePath(path):
        """
        @summary: 检查对应的文件是否存在
        @param path: 路径
        """

        return os.path.exists(path)

    @staticmethod
    def checkDirPath(path):
        """
        @summary: 检查对应的文件夹是否创建，如果未创建则创建之
        @param path: 路径
        """

        if not os.path.exists(path):
            os.makedirs(path)

class Log:

    @staticmethod
    def debug(title='', msg=''):
        Log.log("DEBUG", title, msg)

    @staticmethod
    def info(title='', msg=''):
        Log.log("INFO", title, msg)

    @staticmethod
    def success(title='', msg=''):
        Log.log("SUCCESS", title, msg)

    @staticmethod
    def warn(title='', msg=''):
        Log.log("WARN", title, msg)

    @staticmethod
    def error(title='', msg=''):
        Log.log("ERROR", title, msg)

    @staticmethod
    def blank():
        Log.log("BLANK", "", "")

    @staticmethod
    def log(types, title, msg):

        times = time.strftime("%Y-%m-%d %H:%M:%S")

        if len(title) == 0:
            title = types

        title = "  {0}  ".format(title)

        logStr = ""
        retStr = ""
        f = sys._getframe()
        f = f.f_back
        while hasattr(f, "f_code"):
            co = f.f_code
            retStr = "        %s(%s) -> %s " % (os.getcwd() + "/" + os.path.basename(co.co_filename),
                                                f.f_lineno,
                                                co.co_name) + "\r\n" + retStr
            f = f.f_back
            
        # l = retStr.split("\n")
        # l.pop(len(l) - 2)
        # retStr = "\n".join(l)

        if types == 'DEBUG':
            logStr = "[{0}] [{2}] [{3}] {4} \r\n    callpath: \r\n{1}\r\n".format(
                times, retStr, types, title, msg)
            print("\033[1;40;30m[{0}] \033[1;40;37m[{1}] {2} \033[1;40;36m\r\n    callpath: \r\n{3} \033[0m".format(
                times, title, msg, retStr))

        elif types == 'INFO':
            logStr = "[{0}] [{1}] [{2}] {3}\r\n".format(
                times, types, title, msg)
            print("\033[1;40;30m[{0}] \033[1;40;36m[{1}] {2} \033[0m".format(
                times, title, msg))

        elif types == "SUCCESS":
            logStr = "[{0}] [{1}] [{2}] {3}\r\n".format(
                times, types, title, msg)
            print("\033[1;40;30m[{0}] \033[1;42;37m[{1}] {2} \033[0m".format(
                times, title, msg))

        elif types == 'WARN':
            logStr = "[{0}] [{2}] [{3}] {4} \r\n    callpath: \r\n{1}\r\n".format(
                times, retStr, types, title, msg)
            print("\033[1;40;30m[{0}] \033[1;40;33m[{1}] {2} \033[1;40;33m\r\n    callpath: \r\n{3} \033[0m".format(
                times, title, msg, retStr))

        elif types == 'ERROR':
            logStr = "[{0}] [{2}] [{3}] {4} \r\n    callpath: \r\n{1}\r\n".format(
                times, retStr, types, title, msg)
            print("\033[1;40;30m[{0}] \033[1;40;31m[{1}] {2} \033[1;40;31m\r\n    callpath: \r\n{3} \033[0m".format(
                times, title, msg, retStr))

        elif types == 'BLANK':
            logStr = "[{0}] \r\n".format(times)
            print("\033[1;40;30m[{0}] \033[0m".format(times))
            

        log_path = file_manager.getCurrentDir()+"/Log/"
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        fileName = times.split(" ")[0]
        file_path = log_path + fileName + ".log"

        f = open(file_path, mode='a+', encoding='utf8')

        f.write(logStr)

        f.close()


class SqlLog:

    @staticmethod
    def record(sql, msg):

        date_time = time.strftime("%Y-%m-%d %H:%M:%S")

        file_path = file_manager.getCurrentDir()+"/Log/sql.sql"
        f = open(file_path, mode='a+', encoding='utf8')
        f.write("\r\n#[{0}] {1}\r\n {2}\r\n".format(date_time, msg, sql))
        f.close()
