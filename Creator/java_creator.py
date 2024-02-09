import copy

import os
from Core.file_manager import *
from Core.table_util import *
import shutil


class JavaCreator:
    javaTempPath = os.getcwd()+"/dist/java/"
    pathPrefix = ""
    packageName = ""

    @staticmethod
    def create(talbeInfo, mode, names):

        javaCreator = JavaCreator()

        # ------------ 准备路径信息
        javaCreator.packageName = talbeInfo["packageName"]
        packageName = talbeInfo["packageName"]
        packagePathName = packageName.replace(".", "/")
        # javaCreator.destinationDir = talbeInfo["appPath"] + \
        #     "src/main/java/" + packagePathName + "/"
        javaCreator.pathPrefix = talbeInfo["appPath"] + \
            "java/src/main/java/" + packagePathName + "/"

        # 检查源目录文件夹是否可用,不可用则不创建，担心直接替换文件的风险
        if not os.path.exists(javaCreator.pathPrefix):
            Log.error("java_creator", "源目录不存在，请指定源目录")
            return 0

        Log.blank()
        Log.info(
            "java_create", "================ 正在为`{0}`生成java文件 ================".format(names))

        # 备份目录
        TableUtil.packDir(javaCreator.pathPrefix, "dist/java/src/")

        # ------------ 执行操作
        tableList = TableUtil.getTableInfoWidthNames(talbeInfo, names)

        if len(tableList) == 0:
            Log.error(
                "java_create", "字段 `{0}` 不存在".format(names))
            return

        if mode == "-d":

            javaCreator.clearDir()
        elif mode == "-util":

            javaCreator.createUtil()
        elif mode == "-all":

            javaCreator.createUtil()
            javaCreator.createAllFile(tableList)
        else:

            if "model" in mode == False and "mapper" in mode == False and "provider" in mode == False and "service" in mode == False and "controller" in mode == False:
                JavaCreator.cmdError()

            javaCreator.createAllFile(tableList, mode=mode)

    def createAllFile(self, tableList, mode="-all"):

        for it in tableList:

            # 表名称
            tableName = it["name"]

            # 产生的类名称
            className = TableUtil.className(tableName)

            # 创建 文件夹
            TableUtil.checkPath(self.pathPrefix + className)

            if "model" in mode:
                JavaCreator.createModel(
                    self.pathPrefix, self.packageName, it)

            if "mapper" in mode:
                JavaCreator.createMapper(
                    self.pathPrefix, self.packageName, it)

            if "provider" in mode:
                JavaCreator.createProvider(
                    self.pathPrefix, self.packageName, it)

            if "service" in mode:
                JavaCreator.createService(
                    self.pathPrefix, self.packageName, it)

            if "controller" in mode:
                JavaCreator.createController(
                    self.pathPrefix, self.packageName, it)

    def createModel(pathPrefix, packageName, tableInfo):
        """
        @summary: 创建pojo实体类
        @param tableInfos: 表信息
        """

        # 表名称
        tableName = tableInfo["name"]
        # 产生的类名称
        className = TableUtil.className(tableName)
        # 产生的实例名称
        instanceName = TableUtil.instanceName(tableName)
        # 字段属性列表
        columns = copy.deepcopy(tableInfo["columns"])
        # 添加时间信息
        TableUtil.addModelDefaultProperty(columns)
        
        # 文件信息
        string = "package " + packageName + "." + className + ";\r\n\r\n"
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
        tostring_string = "    public String toString() {\r\n\r\n        return \" <" + \
            className + "> {"

        count = 0
        for columnInfo in columns:

            # 字段名称
            propertyName = TableUtil.instanceName(columnInfo["name"])
            propClassName = TableUtil.className(columnInfo["name"])

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
                tostring_string += "                \"" + propertyName + \
                    " = \" + " + propertyName + " + \", \" +\r\n"

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

            json_string += "        if (map.get(\"" + \
                propertyName + "\") != null) {\r\n"
            json_string += "            " + propertyName + " = " + \
                parseMap[columType] + \
                "((String) map.get(\"" + propertyName + "\"));\r\n"
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

        string += prop_string + const_string + const_string3 + \
            json_string + tostring_string + "\r\n}"

        # 文件路径
        pojoFilePath = pathPrefix + className + "/" + className + ".java"

        Log.success("Model", "生成：" + pojoFilePath)

        # 创建文件
        f = open(pojoFilePath, mode='w+')
        f.write(string)
        f.close()

    def createMapper(pathPrefix, packageName, tableInfo):

        # 表名称
        tableName = tableInfo["name"]
        # 产生的类名称
        className = TableUtil.className(tableName)
        # 对应的实例名称
        instanceName = TableUtil.instanceName(tableName)

        filepath = pathPrefix + className + "/" + className + "Mapper.java"

        # if file_manager.checkFilePath(filepath):

        string = "package " + packageName + "." + className + ";\r\n"
        string += "import org.apache.ibatis.annotations.*;\r\n\r\n"
        string += "import java.util.List;\r\n"
        string += "import org.springframework.stereotype.Component;\r\n\r\n"
        string += "@Component(value = \"" + className + "Mapper\")\r\n"
        string += "@Mapper\r\n"
        string += "public interface " + className + "Mapper {\r\n\r\n"
        string += "    //### 自动生成 ###"
        string += "    @SelectProvider(type = " + className + \
            "Provider.class, method = \"selectAll\")\r\n"
        string += "    public List<" + className + \
            "> list(@Param(\"page\") Integer page, @Param(\"size\") Integer size);\r\n\r\n"
        string += "    @SelectProvider(type = " + className + \
            "Provider.class, method = \"selectOne\")\r\n"
        string += "    public " + className + \
            " show(@Param(\"id\") Long id);\r\n\r\n"
        string += "    @InsertProvider(type = " + className + \
            "Provider.class, method = \"insertOne\")\r\n"
        string += "    @Options(useGeneratedKeys = true, keyProperty = \"id\", keyColumn = \"id\")//加入该注解可以保持对象后，查看对象插入id\r\n"
        string += "    public Boolean insert(" + \
            className + " " + instanceName + ");\r\n\r\n"
        string += "    @DeleteProvider(type = " + className + \
            "Provider.class, method = \"deleteOne\")\r\n"
        string += "    public Boolean delete(@Param(\"id\") Long id);\r\n\r\n"
        string += "    @UpdateProvider(type = " + className + \
            "Provider.class, method = \"updateOne\")\r\n"
        string += "    public Boolean update(" + \
            className + " " + instanceName + ");\r\n\r\n"
        string += "    //### 自动生成 ###"
        string += "}"


        Log.success("Mapper", "生成："+filepath)
        f = open(filepath, mode='w+')
        f.write(string)
        f.close()

    def createProvider(pathPrefix, packageName, tableInfo):
        # 表名称
        tableName = tableInfo["name"]

        # 对应的类名称
        className = TableUtil.className(tableName)

        # 对应的实例名称
        instanceName = TableUtil.instanceName(tableName)

        # 字段属性列表
        columns = tableInfo["columns"]
        columns = TableUtil.addModelDefaultProperty(columns)

        string = "package " + packageName + "." + className + ";\r\n\r\n"
        string += "import java.util.Map;\r\n\r\n"
        string += "public class " + className + "Provider {\r\n\r\n"

        if_string = ""
        insert_string = "        String key = \"\";\r\n        String value = \"\";\r\n"
        update_string = "        String sql = \"\";\r\n"

        colum_string = ""
        for columnInfo in columns:
            # 字段名称
            propertyName = TableUtil.instanceName(columnInfo["name"])
            propClassName = TableUtil.className(columnInfo["name"])

            # 字段类型
            columType = columnInfo["columnProperty"].split('(')[0]
            columType = columType.strip()
            columType = columType.upper()

            if (propertyName == 'id' or columType == 'REAL'):
                if_string = "        if (" + instanceName + ".get" + propClassName + \
                    "() != null && " + instanceName + \
                    ".get" + propClassName + "() > 0) {\r\n"

            elif (columType == 'TINYINT' or
                  columType == 'SMALLINT' or
                  columType == 'MEDIUMINT' or
                  columType == 'INT' or
                  columType == 'BIGINT' or
                  columType == 'TIMESTAMP'):
                if_string = "        if (" + instanceName + ".get" + propClassName + \
                    "() != null && " + instanceName + \
                    ".get" + propClassName + "() >= 0) {\r\n"

            elif (columType == 'CHAR' or
                  columType == 'VARCHAR' or
                  columType == 'TINYTEXT' or
                  columType == 'TEXT' or
                  columType == 'MEDIUMTEXT' or
                  columType == 'LONGTEXT'):
                if_string = "        if (" + instanceName + ".get" + propClassName + \
                    "() != null && !" + instanceName + ".get" + \
                    propClassName + "().isEmpty()) {\r\n"

            elif (columType == 'FLOAT'):
                if_string = "        if (" + instanceName + ".get" + propClassName + \
                    "() != null && " + instanceName + \
                    ".get" + propClassName + "() > 0) {\r\n"

            elif (columType == 'DOUBLE'):
                if_string = "        if (" + instanceName + ".get" + propClassName + \
                    "() != null && " + instanceName + \
                    ".get" + propClassName + "() > 0) {\r\n"

            elif (columType == 'BOOLEAN'):
                if_string = "        if (" + instanceName + ".get" + propClassName + \
                    "() != null && " + instanceName + ".get" + \
                    propClassName + "() == true) {\r\n"

            elif (columType == 'DATETIME' or
                  columType == 'DATE' or
                  columType == 'TIME'):
                if_string = "        if (" + instanceName + \
                    ".get" + propClassName + "() != null) {\r\n"

            else:
                Log.info("pojo", "未知字段类型: " + columType)
                pass

            colum_string += " " + tableName + "." + propertyName + ","

            insert_string += if_string
            insert_string += "           key += \"" + propertyName + ",\";\r\n"
            insert_string += "           value += \"#{" + \
                propertyName + "},\";\r\n"
            insert_string += "        }\r\n\r\n"

            update_string += if_string
            update_string += "           sql += \"" + \
                propertyName + " = #{" + propertyName + "},\";\r\n"
            update_string += "        }\r\n\r\n"

        colum_string = colum_string[0:len(colum_string)-1]

        string += "    public String selectAll(Map<String, Object> parm) {\r\n\r\n"
        string += "        return \"select " + colum_string + \
            " from " + tableName + " limit #{page},#{size}\";\r\n"
        string += "    }\r\n\r\n"
        string += "    public String selectOne() {\r\n\r\n"
        string += "        return \"select " + colum_string + " from " + \
            tableName + " where " + tableName + ".id=#{id}\";\r\n"
        string += "    }\r\n\r\n"
        string += "    public String deleteOne() {\r\n\r\n"
        string += "        return \"delete from " + \
            tableName + " where id = #{id}\";\r\n"
        string += "    }\r\n\r\n"
        string += "    public String insertOne(" + \
            className + " " + instanceName + ") {\r\n\r\n"
        string += insert_string
        string += "        key = key.substring(0,key.length()-1);\r\n"
        string += "        value = value.substring(0,value.length()-1);\r\n\r\n"
        string += "        return \"insert into " + tableName + \
            " (\" + key + \") values (\" + value + \")\";\r\n"
        string += "    }\r\n\r\n"
        string += "    public String updateOne(" + \
            className + " " + instanceName + ") {\r\n\r\n"
        string += update_string
        string += "        sql = sql.substring(0,sql.length()-1);\r\n\r\n"
        string += "        return \"update " + tableName + \
            " set \" + sql + \" where id = #{id}\";\r\n"
        string += "    }\r\n"
        string += "}\r\n"

        filepath = pathPrefix + className + "/" + className + "Provider.java"
        Log.success("Provider", "生成："+filepath)
        f = open(filepath, mode='w+')
        f.write(string)
        f.close()

    def createService(pathPrefix, packageName, tableInfo):
        # 表名称
        tableName = tableInfo["name"]

        # 对应的类名称
        className = TableUtil.className(tableName)

        # 对应的实例名称
        instanceName = TableUtil.instanceName(tableName)

        string = "package " + packageName + "." + className + ";\r\n\r\n"
        string += "import java.sql.Timestamp;\r\n"
        string += "import java.util.*;\r\n"
        string += "import org.springframework.beans.factory.annotation.Autowired;\r\n"
        string += "import org.springframework.validation.annotation.Validated;\r\n"
        string += "import org.springframework.web.bind.annotation.*;\r\n"
        string += "import org.springframework.stereotype.Service;\r\n\r\n"
        string += "import " + packageName + ".service.ResponseService;\r\n"
        string += "import " + packageName + ".utils.ResponseStatus;\r\n"
        string += "@Service\r\n"
        string += "public class " + className + "Service {\r\n\r\n"
        string += "    @Autowired\r\n"
        string += "    private " + className + \
            "Mapper " + instanceName + "Mapper; \r\n\r\n"
        string += "    @Autowired\r\n"
        string += "    private ResponseService responseService; \r\n\r\n"
        string += "    // 获取列表\r\n"
        string += "    public HashMap<String, Object> list(int page, int size, @Validated " + \
            className + " " + instanceName + ") {\r\n"
        string += "        \r\n"
        string += "        List<" + className + "> list = " + \
            instanceName + \
            "Mapper.list(page, size);\r\n"
        string += "        \r\n"
        string += "        HashMap<String, Object> map = responseService.getReturnResponse(ResponseStatus.success,list);\r\n"
        string += "        return map;\r\n"
        string += "    }\r\n\r\n"
        string += "    // 删除\r\n"
        string += "    public HashMap<String, Object> delete(@PathVariable(\"id\") Long id) {\r\n"
        string += "        \r\n"
        string += "        " + instanceName + "Mapper.delete(id);\r\n"
        string += "        \r\n"
        string += "        HashMap<String, Object> map = responseService.getReturnResponse(ResponseStatus.success,null);\r\n"
        string += "        return map;\r\n"
        string += "    }\r\n\r\n"
        string += "    // 查看详情\r\n"
        string += "    public HashMap<String, Object> show(@PathVariable(\"id\") Long id) {\r\n"
        string += "        \r\n"
        string += "        " + className + " " + instanceName + \
            " = " + instanceName + "Mapper.show(id);\r\n"
        string += "        \r\n"
        string += "        HashMap<String, Object> map = responseService.getReturnResponse(ResponseStatus.success," + \
            instanceName + ");\r\n"
        string += "        return map;\r\n"
        string += "    }\r\n\r\n"
        string += "    // 插入，保存\r\n"
        string += "    public HashMap<String, Object> store(@Validated " + \
            className + " " + instanceName + ") {\r\n"
        string += "        \r\n"
        string += "        Long id = " + instanceName + ".getId();\r\n"
        string += "        Timestamp t = new Timestamp((new Date()).getTime());\r\n"
        string += "        \r\n"
        string += "        Boolean status = true;\r\n"
        string += "        if (id != null && id > 0) {\r\n"
        string += "            // * 修改 */\r\n"
        string += "            " + instanceName + ".setUpdateAt(t);\r\n"
        string += "            status = " + instanceName + \
            "Mapper.update(" + instanceName + ");\r\n"
        string += "        } else {\r\n"
        string += "            // * 添加 */\r\n"
        string += "            " + instanceName + ".setCreateAt(t);\r\n"
        string += "            status = " + instanceName + \
            "Mapper.insert(" + instanceName + ");\r\n"
        string += "        }\r\n"
        string += "        \r\n"
        string += "        HashMap<String, Object> map = responseService.getReturnResponse(status ? ResponseStatus.success : ResponseStatus.error," + \
            instanceName + ");\r\n"
        string += "        return map;\r\n"
        string += "    }\r\n\r\n"
        string += "}\r\n\r\n"

        filepath = pathPrefix + className + "/" + className + "Service.java"
        Log.success("Service", "生成："+filepath)
        f = open(filepath, mode='w+')
        f.write(string)
        f.close()

    def createController(pathPrefix, packageName, tableInfo):
        # 表名称
        tableName = tableInfo["name"]

        # 对应的类名称
        className = TableUtil.className(tableName)

        # 对应的实例名称
        instanceName = TableUtil.instanceName(tableName)

        string = "package " + packageName + "." + className + ";\r\n\r\n"
        string += "import java.util.*;\r\n\r\n"
        string += "import org.springframework.beans.factory.annotation.Autowired;\r\n"
        string += "import org.springframework.validation.annotation.Validated;\r\n"
        string += "import org.springframework.web.bind.annotation.*;\r\n\r\n"
        if instanceName.find("User") > 0:
            string += "import com.blog.zz.service.LoginService;\r\n\r\n"
            string += "import com.blog.zz.model.AdminUser;\r\n\r\n"
        string += "@RequestMapping(\"/" + instanceName + "\")\r\n"
        string += "@RestController\r\n"
        string += "public class " + className + "Controller {\r\n\r\n"
        string += "    @Autowired\r\n"
        string += "    private " + className + \
            "Service " + instanceName + "Service; \r\n\r\n"
        if instanceName.find("User") > 0:
            string += "    @Autowired\r\n"
            string += "    private LoginService loginService; \r\n\r\n"
        string += "    // 获取列表\r\n"
        string += "    @GetMapping\r\n"
        string += "    public HashMap<String, Object> list(@RequestParam Map<String, Object> param) {\r\n"
        string += "        \r\n"
        string += "        int page = 0;\r\n"
        string += "        int size = 10;\r\n"
        string += "        if (param.get(\"page\") != null) {\r\n"
        string += "            page = Integer.parseInt((String) param.get(\"page\"));\r\n"
        string += "        }\r\n"
        string += "        if (param.get(\"size\") != null) {\r\n"
        string += "            size = Integer.parseInt((String) param.get(\"size\"));\r\n"
        string += "        }\r\n"
        string += "        \r\n"
        string += "        " + className + " " + \
            instanceName + " = new " + className + "();\r\n"
        string += "        " + instanceName + ".fromMap(param);\r\n"
        string += "        \r\n"
        string += "        HashMap<String, Object> map = " + \
            instanceName + \
            "Service.list(page, size, " + instanceName + ");\r\n"
        string += "        return map;\r\n"
        string += "    }\r\n\r\n"
        string += "    // 删除\r\n"
        string += "    @GetMapping(\"/delete/{id}\")\r\n"
        string += "    public HashMap<String, Object> delete(@PathVariable(\"id\") Long id) {\r\n"
        string += "        \r\n"
        string += "        HashMap<String, Object> map = " + \
            instanceName + "Service.delete(id);\r\n"
        string += "        return map;\r\n"
        string += "    }\r\n\r\n"
        string += "    // 查看详情\r\n"
        string += "    @GetMapping(\"/{id}\")\r\n"
        string += "    public HashMap<String, Object> show(@PathVariable(\"id\") Long id) {\r\n"
        string += "        \r\n"
        string += "        HashMap<String, Object> map = " + \
            instanceName + "Service.show(id);\r\n"
        string += "        return map;\r\n"
        string += "    }\r\n\r\n"
        string += "    // 插入，保存\r\n"
        string += "    @PostMapping\r\n"
        string += "    @Validated\r\n"
        string += "    public HashMap<String, Object> store(@RequestBody " + \
            className + " " + instanceName + ") {\r\n"
        string += "        \r\n"
        string += "        HashMap<String, Object> map = " + \
            instanceName + "Service.store(" + instanceName + ");\r\n"
        string += "        return map;\r\n"
        string += "    }\r\n"

        if instanceName.find("User") > 0:
            string += "\r\n    // 登录接口\r\n"
            string += "    @PostMapping(\"/login\")\r\n"
            string += "    public HashMap<String, Object> login(@RequestBody HashMap<String, Object> data) {\r\n"
            string += "\r\n"
            string += "        AdminUser adminUser = new AdminUser();\r\n"
            string += "        adminUser.setName(data.get(\"name\").toString());\r\n"
            string += "        adminUser.setPassword(data.get(\"password\").toString());\r\n"
            string += "\r\n"
            string += "        HashMap<String, Object> map = loginService.login(adminUser);\r\n"
            string += "        return map;\r\n"
            string += "    }\r\n"

        string += "}\r\n\r\n"

        filepath = pathPrefix + className + "/" + className + "Controller.java"
        Log.success("Controller", "生成："+filepath)
        f = open(filepath, mode='w+')
        f.write(string)
        f.close()

    def createUtil(self):
        Log.blank()
        Log.info("create_utils", "生成 utils 文件")

        files = [self.pathPrefix+"utils/Pager.java",
                 self.pathPrefix+"utils/ResponseStatus.java",
                 self.pathPrefix+"service/ResponseService.java",
                 self.pathPrefix+"service/LoginService.java",
                 self.pathPrefix+"mapper/LoginMapper.java",
                 ]

        for file_path in files:

            Log.success("utils", "生成："+file_path)
            f = open(file_path, mode='w+')

            string = "package " + self.packageName + ".utils;\r\n\r\n"
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
                string = "package " + self.packageName + ".service;\r\n"
                string += "\r\n"
                string += "import java.util.HashMap;\r\n"
                string += "import org.springframework.stereotype.Service;\r\n"
                string += "\r\n"
                string += "import " + self.packageName + ".utils.ResponseStatus;\r\n"
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
                string = "package com.blog.zz.service;\r\n"
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
                string += "    //过期时间:秒\r\n"
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
                string = "package " + self.packageName + ".service;\r\n\r\n"
                string += "\r\n"
                string += "import org.apache.ibatis.annotations.*;\r\n"
                string += "\r\n"
                string += "import java.util.HashMap;\r\n"
                string += "import org.springframework.stereotype.Component;\r\n"
                string += "import " + self.packageName + ".service.LoginService;\r\n"
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

    def clearDir(self):
        Log.blank()
        Log.info("java", "正在清空文件夹...")

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
    def cmdError():
        Log.info("java_create", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            java -all [names] 生成所有内容。\r\n \
            java -model [names] 生成model文件。\r\n \
            java -mapper [names] 生成mapper文件。\r\n \
            java -provider [names] 生成provider文件。\r\n \
            java -service [names] 生成service文件。\r\n \
            java -controller [names] 生成controller文件。\r\n \
            java -util [names] 生成util文件。\r\n \
        ")
