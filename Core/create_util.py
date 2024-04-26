import datetime
import os
import shutil
import json

from Core.file_manager import Log
from Core.mysql_config import MysqlConfig

class CreateUtil:
    
    @staticmethod
    def getConfigInfo(path="project.json"):
        """
        @summary: 根据输入的表名字符串，获取对应的表信息数组
        @param names: 输入的表名字符串
        @return: list 对应的表信息数组
        """

        f = open(path, encoding='utf-8')
        c = f.readlines()
        f.close()
        c = ''.join(c)
        d = json.loads(c)

        return d
    
    @staticmethod
    def getTableInfoWidthNames(tableInfo, names):
        """
        @summary: 根据输入的表名字符串，获取对应的表信息数组
        @param tableInfo: 配置信息
        @param names: 输入的表名字符串
        @return: list 对应的表信息数组
        """

        tableInfoList = []
        nameList = names.split(",")

        if names == "-all":
            nameList = []

        # 获取数据表列表
        tableList = tableInfo["db"]["tableList"]
        for tableInfo in tableList:
            if len(nameList) == 0:
                tableInfoList.append(tableInfo)
            else:
                if tableInfo["name"] in nameList:
                    tableInfoList.append(tableInfo)

        return tableInfoList
    
    @staticmethod
    def checkPath(path):
        """
        @summary: 检查文件或者文件夹路径是否存在，不存在会自动创建
        @param path: 文件或者文件夹路径
        """
        
        if os.path.exists(path) == False:
            if "." in path:
                f = open(path, encoding='utf-8')
                f.close()
            elif path[len(path) - 1: len(path)] == "/":
                os.makedirs(path)
    
    @staticmethod
    def pathExists(path):
        """
        @summary: 检查文件或者文件夹路径是否存在
        @param path: 文件或者文件夹路径
        """
        
        if os.path.exists(path):
            return True
        else:
            return False

    @staticmethod
    def getMysqlConfig(projectInfo):
        """
        @summary: 根据输入的表名字符串，获取对应的表信息数组
        @param projectInfo: 配置信息
        @return: mysql配置信息
        """
        
        config = MysqlConfig()
        config.DBHOST = projectInfo["db"]["host"]
        config.DBPORT = projectInfo["db"]["port"]
        config.DBUSER = projectInfo["db"]["user"]
        config.DBPWD = projectInfo["db"]["password"]
        config.DBCHAR = projectInfo["db"]["charSet"]
        
        return config
    
    @staticmethod
    def camelize(s):
        """
        @summary: 下划线转驼峰
        @param s: 字符串
        @return: 转后的字符串
        """
        
        s.replace("-", "_")
        namelist = s.split("_")
        newList = []
        for s in namelist:
            s = s.capitalize()
            newList.append(s)

        camelString = "".join(newList)
        return camelString

    @staticmethod
    def uncamelize(s):
        """
        @summary: 驼峰转下划线
        @param s: 字符串
        @return: 转后的字符串
        """
        
        result = []
        for c in s:
            if c.isupper():
                result.append('_')
                result.append(c.lower())
            else:
                result.append(c)
        return ''.join(result)

    @staticmethod
    def instanceName(s):
        """
        @summary: 返回实例对象名
        @param s: 字符串
        @return: 转后的字符串
        """

        className = CreateUtil.camelize(s)
        return className[:1].lower() + className[1:]

    @staticmethod
    def getTables(projectInfo, names):
        """
        @summary: 根据输入的表名字符串，获取对应的表信息数组
        @param tableInfo: 配置信息
        @param names: 输入的表名字符串
        @return: list 对应的表信息数组
        """

        tableInfoList = []
        nameList = names.split(",")

        if names == "-all":
            nameList = []

        # 获取数据表列表
        tableList = projectInfo["db"]["tableList"]
        for t in tableList:
            if len(nameList) == 0:
                tableInfoList.append(t)
            else:
                if t["name"] in nameList:
                    tableInfoList.append(t)

        return tableInfoList

    @staticmethod
    def packDir(dirPath, storePath):
        # 检查路径
        CreateUtil.checkPath(storePath)
        
        # 压缩文件
        zip_name = shutil.make_archive(dirPath, f'zip', dirPath)
        # print(zip_name)  # 返回文件的最终路径
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H:%M:%S")
        names = zip_name.split("/")
        
        # 获取压缩文件名
        zip_name1 = formatted_datetime+"_"+names[len(names) - 1]
        
        # 重命名文件
        os.rename(zip_name, zip_name1)
        
        # 移动文件
        shutil.move(zip_name1, storePath)

    @staticmethod
    def addModelDefaultProperty(columns):
        """
        @summary: 对表添加 createTime updateTime deleteTime等信息
        @param columns: 表字段列表
        """

        hasId = False
        for it in columns:
            if it["name"] == "id":
                hasId = True

        if hasId == False:
            columns.insert(0, {
                "name": "id",
                "des": "记录id",
                "columnProperty": "int NOT NULL AUTO_INCREMENT PRIMARY KEY",
                "formType": "number",
                "showTime": 0,
                "showInSearch": 0,
                "required": 0,
                "sort": "up",
                "align": "center",
                "width": 100,
            })

        columns.append({
            "name": "create_at",
            "des": "创建于",
            "columnProperty": "DATETIME",
            "formType": "date",
            "showTime": 1,
            "showInSearch": 0,
            "required": 0,
            "sort": "up",
            "align": "center",
            "width": 100,
        })
        columns.append({
            "name": "update_at",
            "des": "更新于",
            "columnProperty": "DATETIME",
            "formType": "date",
            "showTime": 1,
            "showInSearch": 0,
            "required": 0,
            "sort": "up",
            "align": "center",
            "width": 100,
        })
        columns.append({
            "name": "delete_at",
            "des": "删除于",
            "columnProperty": "DATETIME",
            "formType": "date",
            "showTime": 1,
            "showInSearch": 0,
            "required": 0,
            "sort": "up",
            "align": "center",
            "width": 100,
        })

        return columns

    @staticmethod
    def replaceUnValidJsonValueWithKey(source, key, value):
        """
        @summary: 对于不标准的json字符串中替换key对应的value, key的冒号后面需要有一个空格
        @param source: json字符串
        @param key: json中的key
        @param value: 对应的value
        @return: string 替换好的字符串
        """
        # key = '"{0}":'.format(key)
        arr = source.split(key)
        # print(len(arr))
        # if len(arr) == 1:
        #     key = '"{0}" :'.format(key)
        #     arr = source.split(key)

        t1 = arr[1].split('"')
        t1[1] = value
        t1 = '"'.join(t1)

        arr[1] = t1
        d = key.join(arr)

        return d

    @staticmethod
    def replaceValidJsonValueWithKey(source, key, value):
        """
        @summary: 对于标准的json字符串中替换key对应的value, key的冒号后面需要有一个空格
        @param source: json字符串
        @param key: json中的key
        @param value: 对应的value
        @return: string 替换好的字符串
        """
        c = json.loads(source)

        c[key] = value

        return json.dumps(c)
