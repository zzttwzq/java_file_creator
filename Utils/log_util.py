import os
import time
import sys

from Utils.file_util import FileUtil

class Log:

    @staticmethod
    def debug(title='', msg='', show=True):
        Log.log("DEBUG", title, msg, show)

    @staticmethod
    def info(title='', msg='', show=True):
        Log.log("INFO", title, msg, show)

    @staticmethod
    def success(title='', msg='', show=True):
        Log.log("SUCCESS", title, msg, show)

    @staticmethod
    def warn(title='', msg='', show=True):
        Log.log("WARN", title, msg, show)

    @staticmethod
    def error(title='', msg='', show=True):
        Log.log("ERROR", title, msg, show)

    @staticmethod
    def blank():
        Log.log("BLANK", "", "", True)

    @staticmethod
    def log(types, title, msg, show):

        times = time.strftime("%Y-%m-%d %H:%M:%S")

        if len(title) == 0:
            title = types

        title = "  {0}  ".format(title)

        logStr = ""
        console_str = ""
        retStr = ""
        f = sys._getframe()
        f = f.f_back
        while hasattr(f, "f_code"):
            co = f.f_code
            retStr = "        %s(%s) -> %s " % (os.getcwd() + "/" + os.path.basename(co.co_filename),
                                                f.f_lineno,
                                                co.co_name) + "\r\n" + retStr
            f = f.f_back

        if types == 'DEBUG':
            logStr = "[{0}] [{2}] [{3}] {4} \r\n    callpath: \r\n{1}\r\n".format(
                times, retStr, types, title, msg)
            console_str = "\033[1;30m[{0}] \033[1;37m[{1}] {2} \033[1;36m\r\n    callpath: \r\n{3} \033[0m".format(
                times, title, msg, retStr)

        elif types == 'INFO':
            logStr = "[{0}] [{1}] [{2}] {3}\r\n".format(
                times, types, title, msg)
            console_str = "\033[1;30m[{0}] \033[1;36m[{1}] {2} \033[0m".format(
                times, title, msg)

        elif types == "SUCCESS":
            logStr = "[{0}] [{1}] [{2}] {3}\r\n".format(
                times, types, title, msg)
            console_str = "\033[1;30m[{0}] \033[1;32m[{1}] {2} \033[0m".format(
                times, title, msg)

        elif types == 'WARN':
            logStr = "[{0}] [{2}] [{3}] {4} \r\n    callpath: \r\n{1}\r\n".format(
                times, retStr, types, title, msg)
            console_str = "\033[1;30m[{0}] \033[1;33m[{1}] {2} \033[0m".format(
                times, title, msg, retStr)

        elif types == 'ERROR':
            logStr = "[{0}] [{2}] [{3}] {4} \r\n    callpath: \r\n{1}\r\n".format(
                times, retStr, types, title, msg)
            console_str = "\033[1;30m[{0}] \033[1;31m[{1}] {2} \033[1;33m\r\n    callpath: \r\n{3} \033[0m".format(
                times, title, msg, retStr)

        elif types == 'BLANK':
            logStr = "[{0}] \r\n".format(times)
            console_str = "\033[1;30m[{0}] \033[0m".format(times)
            
        if show:
            print(console_str)

        log_path = FileUtil.getCurrentDir()+"/Log/"
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        fileName = times.split(" ")[0]
        file_path = log_path + fileName + ".log"

        f = open(file_path, mode='a+', encoding='utf8')
        f.write(logStr)
        f.close()

class SqlLog:

    @staticmethod
    def record(sql, msg=""):
        date_time = time.strftime("%Y-%m-%d %H:%M:%S")

        file_path = FileUtil.getCurrentDir()+"/Log/{}.sql".format(date_time.split(" ")[0])
        f = open(file_path, mode='a+', encoding='utf8')
        
        message = "\033[1;30m[{}] \033[1;33m[ SQL ] {} \033[1;31m{} \033[0m".format(date_time, sql, msg)
        # print(message)
        
        content = "[{}] {}\r\n".format(date_time, sql, msg)
        f.write(content)
        
        f.close()