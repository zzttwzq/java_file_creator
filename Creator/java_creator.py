import copy
import os
import sys

#添加上级目录
sys.path.append("..//")
from Utils.log_util import Log
from Utils.file_util import FileUtil
from Utils.create_util import CreateUtil

class JavaCreator:
    java_temp_path = os.getcwd()+"/dist/java/"
    package_path = ""
    package_name = ""
    split_string = "// ############ 自动生成 ############"

    @staticmethod
    def create(talbe_info, mode, names):
        javaCreator = JavaCreator()

        # ------------ 准备路径信息
        javaCreator.package_name = talbe_info["java"]["packageName"]
        javaCreator.package_path = talbe_info["path"] + talbe_info["java"]["packagePath"]

        if not FileUtil.path_exists(javaCreator.package_path):
            Log.error("java_creator", "源目录不存在，请指定源目录")
            return 0

        Log.blank()
        Log.info(
            "java", "================ 正在为`{0}`生成java文件 ================".format(names))

        # 备份目录
        FileUtil.pack_dir(javaCreator.package_path, talbe_info["java"]["backupPath"])

        # ------------ 执行操作
        tableList = CreateUtil.get_tableInfo_width_names(talbe_info, names)
        if len(tableList) == 0:
            Log.error(
                "java", "字段 `{0}` 不存在".format(names))
            return 0
        
        if len(names) == 0:
            JavaCreator.__cmd_error()
        elif mode == "-d":
            javaCreator.clearDir()
        elif mode == "-all":
            javaCreator.create_model(tableList)
            javaCreator.create_mapper(tableList)
            javaCreator.create_provider(tableList)
            javaCreator.create_service(tableList)
            javaCreator.create_controller(tableList)
        elif mode == "-util":
            javaCreator.CreateUtil()
        else:
            if "model" in mode:
                javaCreator.create_model(tableList)
            if "mapper" in mode:
                javaCreator.create_mapper(tableList)
            if "provider" in mode:
                javaCreator.create_provider(tableList)
            if "service" in mode:
                javaCreator.create_service(tableList)
            if "controller" in mode:
                javaCreator.create_controller(tableList)

    def create_model(self, table_info_list):
        """
        @summary: 创建model实体类
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建model实体类 ================")

        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]
            
            # 产生的类名称
            className = CreateUtil.camelize(tableName)
            
            # 产生的实例名称
            instance_name = CreateUtil.instance_name(tableName)
            
            # 字段属性列表
            columns = copy.deepcopy(tableInfo["columns"])
            
            # 文件信息
            string = self.split_string+ "\r\n"
            string += "package " + self.package_name + "." + className + ";\r\n\r\n"
            string += "import java.util.Map;\r\n"
            string += "import java.sql.Timestamp;\r\n\r\n"
            string += "import lombok.Getter;\r\n"
            string += "import lombok.Setter;\r\n\r\n"
            string += "@Getter\r\n"
            string += "@Setter\r\n"
            string += "public class " + className + " {\r\n\r\n"

            prop_string = ""
            json_string = "    public void fromMap(Map<String, Object> map) {\r\n"
            const_string = "\r\n    public " + className + "("
            const_string2 = ""
            const_string3 = "    public " + className + "() {} \r\n\r\n"
            tostring_string = "    public String toString() {\r\n\r\n        return \" <" + className + "> {"

            count = 0
            for columnInfo in columns:

                # 字段名称
                propertyName = columnInfo["name"]

                # 字段描述
                des = columnInfo["des"]

                # 字段类型
                columType = columnInfo["columnProperty"].split('(')[0]
                columType = columType.strip()
                columType = columType.upper()

                parseMap = {
                    "REAL": "Long.parseLong",
                    "TINYINT": "Integer.parseInt",
                    "SMALLINT": "Integer.parseInt",
                    "MEDIUMINT": "Integer.parseInt",
                    "TIMESTAMP": "Integer.parseInt",
                    "INT": "Integer.parseInt",
                    'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Long.parseLong",
                    "BIGINT": "Integer.parseInt",
                    "FLOAT": "Float.parseFloat",
                    "DOUBLE": "Double.parseDouble",
                    "CHAR": "new String",
                    "VARCHAR": "new String",
                    "TINYTEXT": "new String",
                    "TEXT": "new String",
                    "MEDIUMTEXT": "new String",
                    "LONGTEXT": "new String",
                    "BOOL": "Boolean.parseBoolean",
                    "BOOLEAN": "Boolean.parseBoolean",
                    "TIMESTAMP": "Timestamp.valueOf",
                    "DATETIME": "Timestamp.valueOf",
                    "DATE": "Timestamp.valueOf",
                    "TIME": "Timestamp.valueOf",
                }

                if count == 0:
                    tostring_string += propertyName + " = \" + " + propertyName + " + \", \" +\r\n"
                else:
                    tostring_string += "                \"" + propertyName +         " = \" + " + propertyName + " + \", \" +\r\n"

                coulumTypeTemp = {
                    "REAL": "Long",
                    "TINYINT": "Integer",
                    "SMALLINT": "Integer",
                    "MEDIUMINT": "Integer",
                    "INT": "Integer",
                    'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Integer",
                    "BIGINT": "Integer",
                    "CHAR": "String",
                    "VARCHAR": "String",
                    "TINYTEXT": "String",
                    "TEXT": "String",
                    "MEDIUMTEXT": "String",
                    "LONGTEXT": "String",
                    "FLOAT": "Float",
                    "DOUBLE": "Double",
                    "BOOLEAN": "Boolean",
                    "BOOL": "Boolean",
                    "DATETIME": "Timestamp",
                    "DATE": "Timestamp",
                    "TIME": "Timestamp",
                    "TIMESTAMP": "Timestamp",
                }

                dataType = coulumTypeTemp[columType]
                if propertyName == "id":
                    dataType = "Long"

                prop_string += "    private {0} {1}; //{2} \r\n".format(
                    dataType, propertyName, des)
                const_string += "{0} {1},".format(dataType, propertyName)

                json_string += "        if (map.get(\"" +     propertyName + "\") != null) {\r\n"
                json_string += "            " + propertyName + " = " +     parseMap[columType] +     "((String) map.get(\"" + propertyName + "\"));\r\n"
                json_string += "        }\r\n\r\n"

                const_string2 += "        this." + propertyName + "=" + propertyName + ";\r\n"
                count = count + 1

            const_string = const_string[0:len(const_string)-1]
            const_string += ") {\r\n"
            json_string += "    }\r\n\r\n"
            const_string = const_string + const_string2 + "    }\r\n\r\n"

            tostring_string = tostring_string[0:len(tostring_string)-2]
            tostring_string = ""+tostring_string
            tostring_string += " \"}\";\r\n    }"

            string += prop_string + const_string + const_string3 + json_string + tostring_string
            string += "\r\n"
            string += "}\r\n"
            string += self.split_string + "\r\n"

            # 生成文件
            self._generate_file(tableName, className+".java", string, force=True)

    def create_mapper(self, table_info_list):
        """
        @summary: 创建Mapper
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建Mapper ================")
        
        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]
            
            # 产生的类名称
            className = CreateUtil.camelize(tableName)
            
            # 对应的实例名称
            instance_name = CreateUtil.instance_name(tableName)     

            # 登录功能
            addUserLogin = tableName.find("user") > -1 or tableName.find("User") > -1  

            string = self.split_string+ "\r\n"
            string += "package " + self.package_name + "." + className + ";\r\n"
            string += "import java.util.List;\r\n"
            string += "import org.apache.ibatis.annotations.*;\r\n"
            string += "\r\n"
            string += "import org.springframework.stereotype.Component;\r\n"
            string += "\r\n"
            string += "import com.qlzw.smartwc.Utils.CustomCount;\r\n"
            string += "\r\n"
            string += "@Component(value = \"Api" + className + "Mapper\")\r\n"
            string += "@Mapper\r\n"
            string += "public interface Api" + className + "Mapper {\r\n"
            
            contentString = ""
            if addUserLogin:
                contentString += "\r\n"
                contentString += '    @SelectProvider(type = {}Provider.class, method = "getUserByName")\r\n'.format("Api"+className)
                contentString += '    public List<{}> getUserByName(@Param("name") String name, @Param("password") String password);\r\n'.format(className)
                
            contentString += "\r\n"
            contentString += "    @SelectProvider(type = Api" + className + "Provider.class, method = \"getCount\")\r\n"
            contentString += "    public List<CustomCount> getCount();\r\n"
            contentString += "\r\n"
            contentString += "    @SelectProvider(type = Api" + className + "Provider.class, method = \"selectAll\")\r\n"
            contentString += "    public List<" + className + "> list(@Param(\"page\") Integer page, @Param(\"size\") Integer size);\r\n"
            contentString += "\r\n"
            contentString += "    @SelectProvider(type = Api" + className + "Provider.class, method = \"selectOne\")\r\n"
            contentString += "    public " + className + " show(@Param(\"id\") Long id);\r\n"
            contentString += "\r\n"
            contentString += "    @InsertProvider(type = Api" + className + "Provider.class, method = \"insertOne\")\r\n"
            contentString += "    @Options(useGeneratedKeys = true, keyProperty = \"id\", keyColumn = \"id\")//加入该注解可以保持对象后，查看对象插入id\r\n"
            contentString += "    public Boolean insert(" + className + " " + instance_name + ");\r\n"
            contentString += "\r\n"
            contentString += "    @DeleteProvider(type = Api" + className + "Provider.class, method = \"deleteOne\")\r\n"
            contentString += "    public Boolean delete(@Param(\"id\") Long id);\r\n"
            contentString += "\r\n"
            contentString += "    @UpdateProvider(type = Api" + className + "Provider.class, method = \"updateOne\")\r\n"
            contentString += "    public Boolean update(" + className + " " + instance_name + ");\r\n"
            contentString += "\r\n"
            
            string += contentString
            string += "}\r\n"
            string += "{0}\r\n".format(self.split_string)
            
            string2 = "package " + self.package_name + "." + className + ";\r\n"
            string2 += "import org.apache.ibatis.annotations.*;\r\n\r\n"
            string2 += "import org.springframework.stereotype.Component;\r\n\r\n"
            string2 += "@Component(value = \"Custom" + className + "Mapper\")\r\n"
            string2 += "@Mapper\r\n"
            string2 += "public interface Custom" + className + "Mapper {\r\n\r\n"
            string2 += "}\r\n"
            
            # 生成文件
            self._generate_file(tableName, "Api" + className + "Mapper.java", string, force=True)
            self._generate_file(tableName, "Custom" + className + "Mapper.java", string2)

    def create_provider(self, table_info_list):
        """
        @summary: 创建Provider
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建Provider ================")
        
        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的实例名称
            instance_name = CreateUtil.instance_name(tableName)

            # 登录功能
            addUserLogin = tableName.find("user") > -1 or tableName.find("User") > -1 

            # 字段属性列表
            columns = tableInfo["columns"] 

            string = self.split_string+ "\r\n"
            string += "package " + self.package_name + "." + className + ";\r\n"
            string += "\r\n"
            string += "import java.util.Map;\r\n"
            string += "\r\n"
            string += "public class Api" + className + "Provider {\r\n"
            string += "\r\n"
            string += self.split_string

            if_string = ""
            insert_string = "        String key = \"\";\r\n        String value = \"\";\r\n"
            update_string = "        String sql = \"\";\r\n"

            colum_string = ""
            for columnInfo in columns:
                # 字段名称
                propertyName = columnInfo["name"]
                propInstanceName = propertyName
                propClassName = propertyName[:1].upper() + propertyName[1:]

                # 字段类型
                columType = columnInfo["columnProperty"].split('(')[0]
                columType = columType.strip()
                columType = columType.upper()

                if (propertyName == 'id' or columType == 'REAL'):
                    if_string = "        if (" + instance_name + ".get" + propClassName +         "() != null && " + instance_name +         ".get" + propClassName + "() > 0) {\r\n"

                elif (columType == 'TINYINT' or
                    columType == 'SMALLINT' or
                    columType == 'MEDIUMINT' or
                    columType == 'INT' or
                    columType == 'BIGINT' or
                    columType == 'TIMESTAMP'):
                    if_string = "        if (" + instance_name + ".get" + propClassName +         "() != null && " + instance_name +         ".get" + propClassName + "() >= 0) {\r\n"

                elif (columType == 'CHAR' or
                    columType == 'VARCHAR' or
                    columType == 'TINYTEXT' or
                    columType == 'TEXT' or
                    columType == 'MEDIUMTEXT' or
                    columType == 'LONGTEXT'):
                    if_string = "        if (" + instance_name + ".get" + propClassName +         "() != null && !" + instance_name + ".get" +         propClassName + "().isEmpty()) {\r\n"

                elif (columType == 'FLOAT'):
                    if_string = "        if (" + instance_name + ".get" + propClassName +         "() != null && " + instance_name +         ".get" + propClassName + "() > 0) {\r\n"

                elif (columType == 'DOUBLE'):
                    if_string = "        if (" + instance_name + ".get" + propClassName +         "() != null && " + instance_name +         ".get" + propClassName + "() > 0) {\r\n"

                elif (columType == 'BOOLEAN'):
                    if_string = "        if (" + instance_name + ".get" + propClassName +         "() != null && " + instance_name + ".get" +         propClassName + "() == true) {\r\n"

                elif (columType == 'DATETIME' or
                    columType == 'DATE' or
                    columType == 'TIME'):
                    if_string = "        if (" + instance_name +         ".get" + propClassName + "() != null) {\r\n"

                else:
                    Log.info("pojo", "未知字段类型: " + columType)
                    pass

                colum_string += " " + tableName + "." + propInstanceName + ","

                insert_string += if_string
                insert_string += "           key += \"" + propInstanceName + ",\";\r\n"
                insert_string += "           value += \"#{" +     propInstanceName + "},\";\r\n"
                insert_string += "        }\r\n\r\n"

                update_string += if_string
                update_string += "           sql += \"" +     propInstanceName + " = #{" + propInstanceName + "},\";\r\n"
                update_string += "        }\r\n\r\n"

            colum_string = colum_string[0:len(colum_string)-1]

            contentString = "\r\n"
            if addUserLogin:
                contentString += "\r\n"
                contentString += "    public String getUserByName() {\r\n"
                contentString += "\r\n"
                contentString += '        return "select ' + colum_string + ' from ' + tableName + ' where ' + tableName + '.name=#{name} and ' + tableName + '.password=#{password}";\r\n'
                contentString += "    }\r\n"
                contentString += "\r\n"
            
            contentString += "    public String getCount() {\r\n"
            contentString += "\r\n"
            contentString += '        return "SELECT COUNT(*) from {}";\r\n'.format(tableName)
            contentString += "    }\r\n"
            contentString += "\r\n"           
            contentString += "    public String selectAll(Map<String, Object> parm) {\r\n"
            contentString += "\r\n"
            contentString += "        return \"select" + colum_string + " from " + tableName + " limit #{page},#{size}\";\r\n"
            contentString += "    }\r\n"
            contentString += "\r\n"
            contentString += "    public String selectOne() {\r\n"
            contentString += "\r\n"
            contentString += "        return \"select" + colum_string + " from " + tableName + " where " + tableName + ".id=#{id}\";\r\n"
            contentString += "    }\r\n"
            contentString += "\r\n"
            contentString += "    public String deleteOne() {\r\n"
            contentString += "\r\n"
            contentString += "        return \"delete from " + tableName + " where id = #{id}\";\r\n"
            contentString += "    }\r\n"
            contentString += "\r\n"
            contentString += "    public String insertOne(" + className + " " + instance_name + ") {\r\n"
            contentString += "\r\n"
            contentString += insert_string
            contentString += "        key = key.substring(0,key.length()-1);\r\n"
            contentString += "        value = value.substring(0,value.length()-1);\r\n"
            contentString += "\r\n"
            contentString += "        return \"insert into " + tableName + " (\" + key + \") values (\" + value + \")\";\r\n"
            contentString += "    }\r\n"
            contentString += "\r\n"
            contentString += "    public String updateOne(" + className + " " + instance_name + ") {\r\n"
            contentString += "\r\n"
            contentString += update_string
            contentString += "        sql = sql.substring(0,sql.length()-1);\r\n"
            contentString += "\r\n"
            contentString += "        return \"update " + tableName + " set \" + sql + \" where id = #{id}\";\r\n"
            contentString += "    }\r\n"
            
            string += contentString
            string += "}\r\n"
            string += "{0}\r\n".format(self.split_string)
            
            string2 = "package " + self.package_name + "." + className + ";\r\n"
            string2 += "\r\n"
            string2 += "public class Custom" + className + "Provider {\r\n"
            string2 += "\r\n"
            string2 += "}\r\n"
            
            # 生成文件
            self._generate_file(tableName, "Api" + className + "Provider.java", string, force=True)
            self._generate_file(tableName, "Custom" + className + "Provider.java", string2)

    def create_service(self, table_info_list):
        """
        @summary: 创建Service
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建Service ================")
        
        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的实例名称
            instance_name = CreateUtil.instance_name(tableName)      

            # 登录功能
            addUserLogin = tableName.find("user") > -1 or tableName.find("User") > -1

            string = self.split_string+ "\r\n"
            string += "package " + self.package_name + "." + className + ";\r\n"
            string += "\r\n"
            string += "import java.sql.Timestamp;\r\n"
            string += "import java.util.*;\r\n"
            string += "import org.springframework.beans.factory.annotation.Autowired;\r\n"
            string += "import org.springframework.validation.annotation.Validated;\r\n"
            string += "import org.springframework.web.bind.annotation.*;\r\n"
            string += "import org.springframework.stereotype.Service;\r\n"
            string += "\r\n"
            if addUserLogin:
                string += "import " + self.package_name + ".Utils.JWTUtils;\r\n"
            string += "import " + self.package_name + ".DBUtil.DbService;\r\n"
            string += "import " + self.package_name + ".Utils.JWTUtils;\r\n"
            string += "import " + self.package_name + ".Utils.CustomCount;\r\n"
            string += "import " + self.package_name + ".Utils.ResponseService;\r\n"
            string += "import " + self.package_name + ".Utils.ResponseStatus;\r\n"
            string += "@Service\r\n"
            string += "public class Api" + className + "Service {\r\n"
            string += "\r\n"
            string += "    @Autowired\r\n"
            string += "    private DbService dbService; \r\n"
            string += "\r\n"
            string += "    @Autowired\r\n"
            string += "    private Api" + className + "Mapper api" + className + "Mapper; \r\n"
            string += "\r\n"
            string += "    @Autowired\r\n"
            string += "    private ResponseService responseService; \r\n"
            
            contentString = ""
            if addUserLogin:
                contentString += "    // 登录接口\r\n"
                contentString += "    public HashMap<String, Object> login(" + className + " " + instance_name + ") {\r\n"
                contentString += "        List<{}> findUsers = {}Mapper.getUserByName({}.getName(), {}.getPassword());\r\n".format(className, "api" + className, instance_name, instance_name)
                contentString += "\r\n"
                contentString += "        if (findUsers.size() == 0) {\r\n"
                contentString += "            ResponseService responseService = new ResponseService();\r\n"
                contentString += "            HashMap<String, Object> map = responseService.getReturnResponse(ResponseStatus.error, null);\r\n"
                contentString += '            map.put("msg", "用户名或密码错误！");\r\n'
                contentString += "\r\n"
                contentString += "            return map;\r\n"
                contentString += "        } else {\r\n"
                contentString += "\r\n"
                contentString += "            {} findUser = findUsers.get(0);\r\n".format(className)
                contentString += "\r\n"
                contentString += "            // 更新用户\r\n"
                contentString += "            Timestamp t = new Timestamp((new Date()).getTime());\r\n"
                contentString += "            String token = JWTUtils.getToken(findUser.getId(), findUser.getName(), findUser.getPassword());\r\n"
                contentString += "\r\n"
                contentString += "            findUser.setToken(token);\r\n"
                contentString += "            findUser.setUpdateAt(t);\r\n"
                contentString += "            Boolean status = {}Mapper.update(findUser);\r\n".format("api" + className)
                contentString += "            findUser.setPassword(null);\r\n"
                contentString += "\r\n"
                contentString += "            HashMap<String, Object> map = responseService.getReturnResponse(status ? ResponseStatus.success : ResponseStatus.error, findUser);\r\n"
                contentString += "            return map;\r\n"
                contentString += "        }\r\n"
                contentString += "    }\r\n"
                contentString += "\r\n"
                
            contentString += "\r\n    // 获取列表\r\n"
            contentString += "    public HashMap<String, Object> list(Map<String, Object> param) {\r\n"
            contentString += "        \r\n"
            contentString += "        // 获取总数量\r\n"
            contentString += "        int total = 0;\r\n"
            contentString += "        List<CustomCount> ll = api{}Mapper.getCount();\r\n".format(className)
            contentString += "        if (ll.size() > 0) {\r\n"
            contentString += "            CustomCount customCount = ll.get(0);\r\n"
            contentString += "            total = customCount.getCount();\r\n"
            contentString += "        }\r\n"
            contentString += "        \r\n"
            contentString += "        int page = 0;\r\n"
            contentString += "        int size = 10;\r\n"
            contentString += "        if (param.get(\"page\") != null) {\r\n"
            contentString += "            page = Integer.parseInt((String) param.get(\"page\"));\r\n"
            contentString += "            page = page - 1;\r\n"
            contentString += "            if (page < 0) {\r\n"
            contentString += "                page = 0;\r\n"
            contentString += "            }\r\n"
            contentString += "        }\r\n"
            contentString += "        if (param.get(\"size\") != null) {\r\n"
            contentString += "            size = Integer.parseInt((String) param.get(\"size\"));\r\n"
            contentString += "        }\r\n"
            contentString += "        page = page * size;\r\n"
            contentString += "        \r\n"
            contentString += "        " + className + " " + instance_name + " = new " + className + "();\r\n"
            contentString += "        " + instance_name + ".fromMap(param);\r\n"
            contentString += "        \r\n"
            contentString += "        List<" + className + "> list = api" + className + "Mapper.list(page, size);\r\n"
            contentString += "        HashMap<String, Object> map = responseService.getReturnResponse(ResponseStatus.success, list, total);\r\n"
            contentString += "        return map;\r\n"
            contentString += "    }\r\n"
            contentString += "\r\n"
            contentString += "    // 删除\r\n"
            contentString += "    public HashMap<String, Object> delete(@PathVariable(\"id\") Long id) {\r\n"
            contentString += "        \r\n"
            contentString += "        Boolean status = api" + className + "Mapper.delete(id);\r\n"
            contentString += "        \r\n"
            contentString += "        HashMap<String, Object> map = responseService.getReturnResponse(status ? ResponseStatus.success : ResponseStatus.error, null);\r\n"
            contentString += "        return map;\r\n"
            contentString += "    }\r\n"
            contentString += "\r\n"
            contentString += "    // 查看详情\r\n"
            contentString += "    public HashMap<String, Object> show(@PathVariable(\"id\") Long id) {\r\n"
            contentString += "        \r\n"
            contentString += "        " + className + " " + instance_name + " = api" + className + "Mapper.show(id);\r\n"
            contentString += "        \r\n"
            contentString += "        HashMap<String, Object> map = responseService.getReturnResponse(ResponseStatus.success, " + instance_name + ");\r\n"
            contentString += "        return map;\r\n"
            contentString += "    }\r\n"
            contentString += "\r\n"
            contentString += "    // 插入，保存\r\n"
            contentString += "    public HashMap<String, Object> store(@Validated " + className + " " + instance_name + ") {\r\n"
            contentString += "        \r\n"
            contentString += "        Long id = " + instance_name + ".getId();\r\n"
            contentString += "        Timestamp t = new Timestamp((new Date()).getTime());\r\n"
            contentString += "        \r\n"
            contentString += "        Boolean status = true;\r\n"
            contentString += "        if (id != null && id > 0) {\r\n"
            contentString += "            // * 修改 */\r\n"
            contentString += "            " + instance_name + ".setUpdateAt(t);\r\n"
            contentString += "            status = api" + className + "Mapper.update(" + instance_name + ");\r\n"
            contentString += "        } else {\r\n"
            contentString += "            // * 添加 */\r\n"
            contentString += "            " + instance_name + ".setCreateAt(t);\r\n"
            contentString += "            status = api" + className + "Mapper.insert(" + instance_name + ");\r\n"
            contentString += "        }\r\n"
            contentString += "        \r\n"
            contentString += "        HashMap<String, Object> map = responseService.getReturnResponse(status ? ResponseStatus.success : ResponseStatus.error," + instance_name + ");\r\n"
            contentString += "        return map;\r\n"
            contentString += "    }\r\n"
            contentString += "\r\n"
            
            string += contentString
            string += "}\r\n"
            string += "{0}\r\n".format(self.split_string)
            
            string2 = "package " + self.package_name + "." + className + ";\r\n"
            string2 += "\r\n"
            string2 += "import java.sql.Timestamp;\r\n"
            string2 += "import java.util.*;\r\n"
            string2 += "import org.springframework.beans.factory.annotation.Autowired;\r\n"
            string2 += "import org.springframework.validation.annotation.Validated;\r\n"
            string2 += "import org.springframework.web.bind.annotation.*;\r\n"
            string2 += "import org.springframework.stereotype.Service;\r\n"
            string2 += "\r\n"
            string2 += "import " + self.package_name + ".Utils.ResponseService;\r\n"
            string2 += "import " + self.package_name + ".Utils.ResponseStatus;\r\n"
            string2 += "@Service\r\n"
            string2 += "public class Custom" + className + "Service {\r\n"
            string2 += "\r\n"
            string2 += "    @Autowired\r\n"
            string2 += "    private Custom" + className + "Mapper custom" + instance_name + "Mapper; \r\n"
            string2 += "\r\n"
            string2 += "    @Autowired\r\n"
            string2 += "    private ResponseService responseService; \r\n"
            string2 += "\r\n"
            string2 += "}\r\n"

            # 生成文件
            self._generate_file(tableName, "Api" + className + "Service.java", string, force=True)
            self._generate_file(tableName, "Custom" + className + "Service.java", string2)

    def create_controller(self, table_info_list):
        """
        @summary: 创建Controller
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建Controller ================")
        
        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的实例名称
            instance_name = CreateUtil.instance_name(tableName)    

            # 登录功能
            addUserLogin = tableName.find("user") > -1 or tableName.find("User") > -1

            string = "package " + self.package_name + "." + className + ";\r\n\r\n"
            string += "import java.util.*;\r\n"
            string += "\r\n"
            string += "import org.springframework.beans.factory.annotation.Autowired;\r\n"
            string += "import org.springframework.validation.annotation.Validated;\r\n"
            string += "import org.springframework.web.bind.annotation.*;\r\n"
            string += "\r\n"
            string += "@RequestMapping(\"/" + instance_name + "\")\r\n"
            string += "@RestController\r\n"
            string += "public class " + className + "Controller {\r\n"
            string += "\r\n"
            string += "    @Autowired\r\n"
            string += "    private Api" + className + "Service api" + className + "Service; \r\n"
            string += "\r\n"
            string += "    @Autowired\r\n"
            string += "    private Custom" + className + "Service custom" + className + "Service; \r\n"
            string += "\r\n"
            string += self.split_string
                
            contentString = ""
            if addUserLogin:
                contentString += "\r\n    // 登录接口\r\n"
                contentString += "    @PostMapping(\"/login\")\r\n"
                contentString += "    public HashMap<String, Object> login(@RequestBody " + className + " " + instance_name + ") {\r\n"
                contentString += "\r\n"
                contentString += "        HashMap<String, Object> map = api{}Service.login({});\r\n".format(className, instance_name)
                contentString += "        return map;\r\n"
                contentString += "    }\r\n"
                
            contentString += "\r\n    // 获取列表\r\n"
            contentString += "    @GetMapping\r\n"
            contentString += "    public HashMap<String, Object> list(@RequestParam Map<String, Object> param) {\r\n"
            contentString += "        \r\n"
            contentString += "        HashMap<String, Object> map = api" + className + "Service.list(param);\r\n"
            contentString += "        return map;\r\n"
            contentString += "    }\r\n\r\n"
            contentString += "    // 删除\r\n"
            contentString += "    @GetMapping(\"/delete/{id}\")\r\n"
            contentString += "    public HashMap<String, Object> delete(@PathVariable(\"id\") Long id) {\r\n"
            contentString += "        \r\n"
            contentString += "        HashMap<String, Object> map = api" + className + "Service.delete(id);\r\n"
            contentString += "        return map;\r\n"
            contentString += "    }\r\n\r\n"
            contentString += "    // 查看详情\r\n"
            contentString += "    @GetMapping(\"/{id}\")\r\n"
            contentString += "    public HashMap<String, Object> show(@PathVariable(\"id\") Long id) {\r\n"
            contentString += "        \r\n"
            contentString += "        HashMap<String, Object> map = api" + className + "Service.show(id);\r\n"
            contentString += "        return map;\r\n"
            contentString += "    }\r\n\r\n"
            contentString += "    // 插入，保存\r\n"
            contentString += "    @PostMapping\r\n"
            contentString += "    @Validated\r\n"
            contentString += "    public HashMap<String, Object> store(@RequestBody " + className + " " + instance_name + ") {\r\n"
            contentString += "        \r\n"
            contentString += "        HashMap<String, Object> map = api" + className + "Service.store(" + instance_name + ");\r\n"
            contentString += "        return map;\r\n"
            contentString += "    }\r\n"

            string += contentString
            string += "{0}\r\n\r\n".format(self.split_string)
            string += "}\r\n"
            
            # 生成文件
            self._generate_file1(tableName, "Controller.java", contentString, string)
            
    # 生成文件或替换文件内容
    def _generate_file(self, tableName, fileName, totalString, force=False):

        # 产生的类名称
        className = CreateUtil.camelize(tableName)
        # print(">>> {}".format(className))
        
        # 检查文件路径
        fileDir = self.package_path + className + "/"
        FileUtil.check_path(fileDir)
        filePath = fileDir + fileName
        
        # 创建文件
        if force:
            Log.info("java", "生成："+filePath)
            FileUtil.write_file(content=totalString, file_path=filePath)
        else:
            if FileUtil.path_exists(filePath) == False:
                Log.info("java", "生成："+filePath)
                FileUtil.write_file(content=totalString, file_path=filePath)
        
    # 生成文件或替换文件内容
    def _generate_file1(self, tableName, fileName, replaceString, totalString):
        
        # 产生的类名称
        className = CreateUtil.camelize(tableName)
        # 对应的实例名称
        instance_name = CreateUtil.instance_name(tableName)    
        
        # 检查文件路径
        fileDir = self.package_path + className + "/"
        FileUtil.check_path(fileDir)
        filePath = fileDir + className + fileName
        
        if FileUtil.path_exists(filePath) :
            content = FileUtil.read_file(filePath)
            content = "".join(content)
            content = content.split(self.split_string)
            if len(content) != 3:
                content = totalString
            else:
                content[1] = replaceString
                content = (self.split_string).join(content)
        else:
            content = totalString
                
        # 创建文件
        Log.info("java", "生成："+filePath)
        FileUtil.write_file(content=content, file_path=filePath)

    def CreateUtil(self):
        Log.blank()
        Log.info("CreateUtils", "生成 utils 文件")

        files = [self.pathPrefix+"utils/Pager.java",
                 self.pathPrefix+"utils/ResponseStatus.java",
                 self.pathPrefix+"service/ResponseService.java",
                 self.pathPrefix+"service/LoginService.java",
                 self.pathPrefix+"mapper/LoginMapper.java",
                 ]

        for file_path in files:

            Log.success("utils", "生成："+file_path)
            f = open(file_path, mode='w+')

            string = "package " + self.package_name + ".Utils;\r\n\r\n"
            if file_path.find("Pager.java") > 0:
                string += "public class Pager {\r\n"
                string += "\r\n"
                string += "    private Integer page;\r\n"
                string += "    private Integer size;\r\n"
                string += "\r\n"
                string += "    public Pager() {}\r\n"
                string += "\r\n"
                string += "    public Pager(Integer page, Integer size) {\r\n"
                string += "        this.page = page;\r\n"
                string += "        this.size = size;\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    public String toString() {\r\n"
                string += "\r\n"
                string += "        return \" <Pager> { page=\" + page + \" size=\" + size + \"}\";\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    public Integer getPage() {\r\n"
                string += "        return page;\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    public void setPage(Integer page) {\r\n"
                string += "        this.page = page;\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    public Integer getSize() {\r\n"
                string += "        return size;\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    public void setSize(Integer size) {\r\n"
                string += "        this.size = size;\r\n"
                string += "    }\r\n"
                string += "}\r\n"
                string += "\r\n"

            elif file_path.find("ResponseStatus.java") > 0:
                string += "public enum ResponseStatus {\r\n"
                string += "    success,\r\n"
                string += "    error,\r\n"
                string += "}\r\n"

            elif file_path.find("ResponseService.java") > 0:
                string = "package " + self.package_name + ".Service;\r\n\r\n"
                string += "\r\n"
                string += "import java.util.HashMap;\r\n"
                string += "import org.springframework.stereotype.Service;\r\n"
                string += "\r\n"
                string += "import " + self.package_name + ".Utils.ResponseStatus;\r\n"
                string += "\r\n"
                string += "@Service\r\n"
                string += "public class ResponseService {\r\n"
                string += "\r\n"
                string += "    public HashMap<String,Object> getReturnResponse(ResponseStatus status, Object data) {\r\n"
                string += "\r\n"
                string += "        HashMap<String, Object> map = new HashMap<>();\r\n"
                string += "        map.put(\"code\", this.getCode(status));\r\n"
                string += "        map.put(\"msg\", this.getMsg(status));\r\n"
                string += "        map.put(\"data\", data);\r\n"
                string += "        return map;\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    public Integer getCode(ResponseStatus status) {\r\n"
                string += "\r\n"
                string += "        if (status == ResponseStatus.success) {\r\n"
                string += "\r\n"
                string += "            return 200;\r\n"
                string += "        }\r\n"
                string += "        else if (status == ResponseStatus.error) {\r\n"
                string += "\r\n"
                string += "            return 500;\r\n"
                string += "        }\r\n"
                string += "\r\n"
                string += "        return 0;\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    public String getMsg(ResponseStatus status) {\r\n"
                string += "\r\n"
                string += "        if (status == ResponseStatus.success) {\r\n"
                string += "\r\n"
                string += "            return \"成功！\";\r\n"
                string += "        }\r\n"
                string += "        else if (status == ResponseStatus.error) {\r\n"
                string += "\r\n"
                string += "            return \"失败！\";\r\n"
                string += "        }\r\n"
                string += "\r\n"
                string += "        return \"\";\r\n"
                string += "    }\r\n"
                string += "}\r\n"

            elif file_path.find("LoginService.java") > 0:
                string = "package " + self.package_name + ".Service;\r\n\r\n"
                string += "\r\n"
                string += "import java.sql.Timestamp;\r\n"
                string += "import java.util.Calendar;\r\n"
                string += "import java.util.Date;\r\n"
                string += "import java.util.HashMap;\r\n"
                string += "\r\n"
                string += "import org.springframework.beans.factory.annotation.Autowired;\r\n"
                string += "import org.springframework.stereotype.Service;\r\n"
                string += "\r\n"
                string += "import com.alibaba.fastjson.JSON;\r\n"
                string += "import com.auth0.jwt.JWT;\r\n"
                string += "import com.auth0.jwt.algorithms.Algorithm;\r\n"
                string += "import com.auth0.jwt.interfaces.DecodedJWT;\r\n"
                string += "import com.blog.zz.mapper.AdminUserMapper;\r\n"
                string += "import com.blog.zz.mapper.LoginMapper;\r\n"
                string += "import com.blog.zz.model.AdminUser;\r\n"
                string += "import com.blog.zz.utils.ResponseStatus;\r\n"
                string += "\r\n"
                string += "import io.jsonwebtoken.Claims;\r\n"
                string += "import io.jsonwebtoken.Jws;\r\n"
                string += "import io.jsonwebtoken.JwtBuilder;\r\n"
                string += "import io.jsonwebtoken.JwtParser;\r\n"
                string += "import io.jsonwebtoken.Jwts;\r\n"
                string += "import io.jsonwebtoken.SignatureAlgorithm;\r\n"
                string += "\r\n"
                string += "@Service\r\n"
                string += "public class LoginService {\r\n"
                string += "    public static String secretKeString = \"secretKeString\";\r\n"
                string += "\r\n"
                string += "    // 过期时间:秒\r\n"
                string += "    public static final int EXPIRE = 60 * 60 * 24;\r\n"
                string += "\r\n"
                string += "    @Autowired\r\n"
                string += "    LoginMapper loginMapper;\r\n"
                string += "\r\n"
                string += "    @Autowired\r\n"
                string += "    AdminUserMapper adminUserMapper;\r\n"
                string += "\r\n"
                string += "    public String getUserByName() {\r\n"
                string += "        return \"select  admin_user.id, admin_user.token, admin_user.name, admin_user.nickName, admin_user.email, admin_user.avatar, admin_user.province, admin_user.city, admin_user.address, admin_user.ipAddress, admin_user.name as roleName, admin_user.updateAt from admin_user left join role as r on admin_user.roleId = r.id where admin_user.name = #{name} and admin_user.password = #{password}\";\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    // 插入，保存\r\n"
                string += "    public HashMap<String, Object> login(AdminUser adminUser) {\r\n"
                string += "\r\n"
                string += "        Timestamp t = new Timestamp((new Date()).getTime());\r\n"
                string += "\r\n"
                string += "        String token = LoginService.createToken(adminUser);\r\n"
                string += "\r\n"
                string += "        ResponseService responseService = new ResponseService();\r\n"
                string += "        HashMap<String, Object> findUser = loginMapper.getUserByName(adminUser.getName(), adminUser.getPassword());\r\n"
                string += "\r\n"
                string += "        System.out.print(\">>> \" + findUser);\r\n"
                string += "\r\n"
                string += "        if (findUser == null) {\r\n"
                string += "            HashMap<String, Object> map = responseService\r\n"
                string += "                    .getReturnResponse(ResponseStatus.error, null);\r\n"
                string += "            map.put(\"msg\", \"用户名或密码错误！\");\r\n"
                string += "\r\n"
                string += "            return map;\r\n"
                string += "        } else {\r\n"
                string += "            Long id = new Long(findUser.get(\"id\").toString());\r\n"
                string += "\r\n"
                string += "            // 更新数据\r\n"
                string += "            AdminUser user = new AdminUser();\r\n"
                string += "            user.setId(id);\r\n"
                string += "            user.setToken(token);\r\n"
                string += "            user.setUpdateAt(t);\r\n"
                string += "            Boolean status = adminUserMapper.update(user);\r\n"
                string += "            user.setName(findUser.get(\"name\").toString());\r\n"
                string += "\r\n"
                string += "            HashMap<String, Object> map = responseService\r\n"
                string += "                    .getReturnResponse(status ? ResponseStatus.success : ResponseStatus.error, user);\r\n"
                string += "            return map;\r\n"
                string += "        }\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    /// 生成用户token\r\n"
                string += "    public static String getUserToken(Object adminUser) {\r\n"
                string += "\r\n"
                string += "        String userJson = JSON.toJSONString(adminUser);// 序列化user\r\n"
                string += "        JwtBuilder jwtBuilder = Jwts.builder(); // 获得JWT构造器\r\n"
                string += "        HashMap<String, Object> map1 = new HashMap<>();\r\n"
                string += "        map1.put(\"key\", userJson);\r\n"
                string += "\r\n"
                string += "        String token = jwtBuilder\r\n"
                string += "                // .setSubject('hello') // 设置用户数据\r\n"
                string += "                .setIssuedAt(new Date()) // 设置jwt生成时间\r\n"
                string += "                .setId(\"1\") // 设置id为token id\r\n"
                string += "                .setClaims(map1) // 通过map传值\r\n"
                string += "                .setExpiration(new Date(System.currentTimeMillis() + 5000)) // 设置token有效期\r\n"
                string += "                .signWith(SignatureAlgorithm.HS256, secretKeString) // 设置token加密方式和密码\r\n"
                string += "                .compact(); // 生成token字符串\r\n"
                string += "\r\n"
                string += "        return token;\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    /// token获取用户信息 {\r\n"
                string += "    public static <T> T getUser(Class<T> clazz, String token) {\r\n"
                string += "\r\n"
                string += "        if (token != null) {\r\n"
                string += "            JwtParser jwtParser = Jwts.parser(); // 获取jwt解析器\r\n"
                string += "            jwtParser.setSigningKey(secretKeString);\r\n"
                string += "            try {\r\n"
                string += "                // 如果token正确(密码，有效期)则正常运行，否则抛出异常\r\n"
                string += "                Jws<Claims> claimsJws = jwtParser.parseClaimsJws(token);\r\n"
                string += "                Claims body = claimsJws.getBody();// 获取body\r\n"
                string += "                // String subject = body.getSubject();// 获取body中subject中的值\r\n"
                string += "\r\n"
                string += "                String key = body.get(\"key\", String.class);// 获取Claims中map的值\r\n"
                string += "                T user = JSON.parseObject(key, clazz);// 反序列化user\r\n"
                string += "\r\n"
                string += "                if (user == null) {\r\n"
                string += "                    System.out.print(\">>> error: user is null\");\r\n"
                string += "                }\r\n"
                string += "\r\n"
                string += "                return (T) user;\r\n"
                string += "            } catch (Exception e) {\r\n"
                string += "                e.printStackTrace();\r\n"
                string += "                return null;\r\n"
                string += "            }\r\n"
                string += "        } else {\r\n"
                string += "            return null;\r\n"
                string += "        }\r\n"
                string += "    }\r\n"
                string += "    \r\n"
                string += "    /**\r\n"
                string += "     * 生成Token\r\n"
                string += "     */\r\n"
                string += "    public static String createToken(AdminUser user){\r\n"
                string += "        Calendar nowTime = Calendar.getInstance();\r\n"
                string += "        //过期时间\r\n"
                string += "        nowTime.add(Calendar.SECOND, EXPIRE);\r\n"
                string += "\r\n"
                string += "        Date expireDate = nowTime.getTime();\r\n"
                string += "\r\n"
                string += "        // System.out.print('>>> expireDate' + expireDate.toString());\r\n"
                string += "\r\n"
                string += "        String token = JWT.create()\r\n"
                string += "        		//这是在设置第二部分信息，不要设置密码之类的，因为这些信息可以通过浏览器获取\r\n"
                string += "        		//用户id\r\n"
                string += "                .withClaim(\"id\", user.getId())\r\n"
                string += "                //用户名\r\n"
                string += "                .withClaim(\"username\",user.getName())\r\n"
                string += "                //创建token的时间\r\n"
                string += "                .withIssuedAt(new Date())//签名时间\r\n"
                string += "                //设置token的过期时间\r\n"
                string += "                .withExpiresAt(expireDate)//过期时间\r\n"
                string += "                //设置第一部分\r\n"
                string += "                .sign(Algorithm.HMAC256(secretKeString));//签名\r\n"
                string += "        return token;\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    /**\r\n"
                string += "     * 验证token\r\n"
                string += "     */\r\n"
                string += "    public static DecodedJWT verify(String token) {\r\n"
                string += "        // 如果有任何验证异常，此处都会抛出异常 我们需要在拦截器调用这个方法，捕获异常，然后返回错误信息给前端\r\n"
                string += "        DecodedJWT decodedJWT = JWT.require(Algorithm.HMAC256(secretKeString)).build().verify(token);\r\n"
                string += "        return decodedJWT;\r\n"
                string += "    }\r\n"
                string += "\r\n"
                string += "    /**\r\n"
                string += "     * 获取token中的 payload 也就是第二部分的信息\r\n"
                string += "     */\r\n"
                string += "    public static DecodedJWT getTokenInfo(String token) {\r\n"
                string += "        DecodedJWT decodedJWT = JWT.require(Algorithm.HMAC256(secretKeString)).build().verify(token);\r\n"
                string += "        // 使用 TokenUtils.getTokenInfo(token).getClaim('account').asString()\r\n"
                string += "        return decodedJWT;\r\n"
                string += "    }\r\n"
                string += "}\r\n"
                string += "\r\n"

            elif file_path.find("LoginMapper.java") > 0:
                string = "package " + self.package_name + ".Service;\r\n\r\n"
                string += "\r\n"
                string += "import org.apache.ibatis.annotations.*;\r\n"
                string += "\r\n"
                string += "import java.util.HashMap;\r\n"
                string += "import org.springframework.stereotype.Component;\r\n"
                string += "import " + self.package_name + ".Service.LoginService;\r\n"
                string += "\r\n"
                string += "@Component(value = \"LoginMapper\")\r\n"
                string += "@Mapper\r\n"
                string += "public interface LoginMapper {\r\n"
                string += "\r\n"
                string += "    @SelectProvider(type = LoginService.class, method = \"getUserByName\")\r\n"
                string += "    public HashMap<String, Object> getUserByName(@Param(\"name\") String name, @Param(\"password\") String password);\r\n"
                string += "}\r\n"

            f.write(string)
            f.close()

    def clear_table(self, table_info_list):
        Log.blank()
        Log.info("java", "正在删除")

        files = []
        for name in self.dirs:
            filepath = self.pathPrefix + name + "/"
            fs = os.listdir(filepath)

            for f in fs:
                files.append(filepath+f)

        for f in files:
            if f.find(".DS_Store") < 0:
                Log.info("java", "删除文件："+f)
                os.remove(f)

    @staticmethod
    def __cmd_error():
        Log.info("java", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            java -all [names] 生成所有内容。\r\n \
            java -model [names] 生成model文件。\r\n \
            java -mapper [names] 生成mapper文件。\r\n \
            java -provider [names] 生成provider文件。\r\n \
            java -service [names] 生成service文件。\r\n \
            java -controller [names] 生成controller文件。\r\n \
            java -util [names] 生成util文件。\r\n \
        ")
