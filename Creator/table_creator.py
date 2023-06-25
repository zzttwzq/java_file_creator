import os
from Core.file_manager import *
from Core.table_util import *
from Core.mysql import MySqlConn

class TableCreator:
    dirs = ["back"]
    logPath = os.getcwd()+"/Log/"
    pathPrefix = os.getcwd()+"/dist/table/"

    @staticmethod
    def create(info, cmd, param):

        tableCreator = TableCreator()
        
        # 创建 文件夹
        tableCreator.checkFolder()

        if cmd == "-table":
            Log.blank()
            Log.info(
                "table_create", "================ 正在为`{0}`生成table ================".format(param))

            my = MySqlConn()
            if len(param) == 0:
                Log.error("Table", "未指定表名！")
            else:
                tableList = TableUtil.getTableInfoWidthNames(info, param)
                if len(tableList) == 0:
                    Log.error("Table", "{0} 在tableinfo.json 中未找到！".format(param))
                for tableInfo in tableList:
                    tableInfo["dbName"] = info["dbName"]
                    tableInfo["columns"] = TableUtil.addModelDefaultProperty(tableInfo["columns"])
                    my.createTable(tableInfo)
            
        elif cmd == "-db":
            Log.blank()
            Log.info(
                "table_create", "================ 正在生成数据库：`{0}` ================".format(param))
            
            if len(param) != 0:     
                my = MySqlConn()
                my.createDB(param)
            else:
                Log.error("错误", "未指定dbname")

    def checkFolder(self):
        """
        @summary: 检查对应的文件夹是否创建，如果未创建则创建之
        """

        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)

        for name in self.dirs:
            filepath = self.pathPrefix+name+"/"
            if not os.path.exists(filepath):
                os.makedirs(filepath)
