import copy

import os
from Core.file_manager import *
from Core.table_util import *
import shutil


class UniCreator:
    def test():
        print('1')

    @staticmethod
    def cmdError():
        Log.info("uni_create", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            uni -page [names] 生成页面\r\n \
            uni -router [names] 生成路由\r\n \
            uni -api [names] 生成api\r\n \
            uni -request [names] 生成request\r\n \
        ")
