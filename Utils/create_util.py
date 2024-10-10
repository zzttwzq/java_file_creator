import json

from Utils.mysql_util import MySqlConfig

class CreateUtil:
    
    @staticmethod
    def get_config_info(path="project.json"):
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
    def get_tableInfo_width_names(tableInfo, names):
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
    def get_mysql_config(projectInfo):
        """
        @summary: 根据输入的表名字符串，获取对应的表信息数组
        @param projectInfo: 配置信息
        @return: mysql配置信息
        """
        
        config = MySqlConfig()
        config.host = projectInfo["db"]["host"]
        config.port = projectInfo["db"]["port"]
        config.user = projectInfo["db"]["user"]
        config.passwd = projectInfo["db"]["password"]
        config.char_set = projectInfo["db"]["charSet"]
        
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
    def instance_name(s):
        """
        @summary: 返回实例对象名
        @param s: 字符串
        @return: 转后的字符串
        """

        className = CreateUtil.camelize(s)
        return className[:1].lower() + className[1:]

    @staticmethod
    def get_tables(projectInfo, names):
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
            if names == "-all":
                tableInfoList.append(t)
            else:
                if t["name"] in nameList:
                    tableInfoList.append(t)

        return tableInfoList

    @staticmethod
    def modify_config_file_key_value(filePath, key, value):
        f1 = open(filePath, "r")
        content = f1.readlines()
        content = "".join(content)
        content = content.split(key)
        
        if len(content) == 2:
            d1 = content[1]
            d2 = d1.split("\n")
            # d2[0] = "="
        
    @staticmethod
    def replace_unvalid_json_value_with_key(source, key, value):
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
    def replace_valid_json_value_with_key(source, key, value):
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
