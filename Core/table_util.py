from Core.file_manager import *
import json


class TableUtil:

    @staticmethod
    def getConfigInfo():
        """
        @summary: 根据输入的表名字符串，获取对应的表信息数组
        @param names: 输入的表名字符串
        @return: list 对应的表信息数组
        """

        f = file_manager("tableinfo.json")
        c = f.read()
        f.close()
        c = ''.join(c)
        d = json.loads(c)

        return d

    @staticmethod
    def getTableInfoWidthNames(names):
        """
        @summary: 根据输入的表名字符串，获取对应的表信息数组
        @param names: 输入的表名字符串
        @return: list 对应的表信息数组
        """

        f = file_manager("tableinfo.json")
        c = f.read()
        f.close()
        c = ''.join(c)
        d = json.loads(c)

        tableInfoList = []
        nameList = names.split(",")

        if names == "-all":
            nameList = []

        # 获取数据表列表
        tableList = d["tableList"]
        for tableInfo in tableList:
            if len(nameList) == 0:
                tableInfoList.append(tableInfo)
            else:
                if tableInfo["name"] in nameList:
                    tableInfoList.append(tableInfo)

        return tableInfoList

    @staticmethod
    def className(name=""):
        """
        @summary: 根据下划线或中划线返回驼峰字符串
        @param name: 使用下划线或中划线拼接的字符串
        @return: string 驼峰字符串
        """

        name.replace("-", "_")
        namelist = name.split("_")
        newList = []
        for s in namelist:
            s = s.capitalize()
            newList.append(s)

        camelString = "".join(newList)
        return camelString

    @staticmethod
    def instanceName(name):
        """
        @summary: 根据下划线或中划线返回驼峰字符串并且首字母为小写
        @param name: 使用下划线或中划线拼接的字符串
        @return: string 驼峰字符串并且首字母为小写
        """

        className = TableUtil.className(name)
        return className[:1].lower() + className[1:]
    
    @staticmethod
    def addModelDefaultProperty(columns) :
        """
        @summary: 对表添加 createTime updateTime deleteTime等信息
        @param columns: 表字段列表
        """

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
    def uncamelize(name):
        Log.error("TableUtil", "未实现的方法: uncamelize")

    @staticmethod
    def replaceUnValidJsonValueWithKey(source, key, value) :
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
    def replaceValidJsonValueWithKey(source, key, value) :
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