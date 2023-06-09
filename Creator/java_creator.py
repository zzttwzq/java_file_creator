import os
from Core.file_manager import *
from Core.table_util import *


class JavaCreator:
    dirs = ["controller", "model", "mapper",
            "provider", "service", "utils", "backUp"]
    logPath = os.getcwd()+"/Log/"
    javaDestinationDir = ""
    pathPrefix = os.getcwd()+"/dist/java/"
    packageName = ""

    @staticmethod
    def create(names):

        javaCreator = JavaCreator()
        info = TableUtil.getConfigInfo()
        javaCreator.packageName = info["packageName"]
        packagePathName = info["packageName"]
        packagePathName = packagePathName.replace(".", "/")
        javaCreator.javaDestinationDir = info["appPath"] + \
            "java/src/main/java/" + packagePathName + "/"

        # 检查源目录文件夹是否可用,不可用则不创建，担心直接替换文件的风险
        if not os.path.exists(javaCreator.javaDestinationDir):
            Log.error("java_create", "源目录不存在，请指定源目录")
            return 0

        if names == "-d":

            javaCreator.clearDir()
        else:

            tableList = TableUtil.getTableInfoWidthNames(names)

            Log.blank()
            Log.info(
                "java_create", "================ 正在为`{0}`生成java文件 ================".format(names))

            # 创建 文件夹
            javaCreator.checkFolder()

            # 创建 pojo
            javaCreator.createPOJO(tableList)

            # 创建 mapper
            javaCreator.createMapper(tableList)

            # 创建 provider
            javaCreator.createProvider(tableList)

            # 创建 service
            javaCreator.createService(tableList)

            # 创建 controller
            javaCreator.createController(tableList)

            # 创建 工具类
            javaCreator.createUtil()

    def backUpFolder(self):
        """
        @summary: 备份源目录需要生成的文件
        """

        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)

        for name in self.dirs:
            filepath = self.pathPrefix+name+"/"
            if not os.path.exists(filepath):
                os.makedirs(filepath)

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

    def createPOJO(self, tableInfos):
        """
        @summary: 创建pojo实体类
        @param tableInfos: 表信息
        """

        Log.blank()
        Log.info("create_pojo", "生成 java pojo 类")

        for tableInfo in tableInfos:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = TableUtil.className(tableName)

            # 字段属性列表
            columns = tableInfo["columns"]

            # 添加时间信息
            TableUtil.addModelDefaultProperty(columns)

            # 文件信息
            string = "package " + self.packageName + ".model;\r\n\r\n"
            string += "import javax.persistence.Entity;\r\n"
            string += "import javax.persistence.GeneratedValue;\r\n"
            string += "import javax.persistence.GenerationType;\r\n"
            string += "import javax.persistence.Id;\r\n"
            string += "import java.sql.Timestamp;\r\n\r\n"
            string += "@Entity\r\n"
            string += "public class " + className + " {\r\n\r\n"

            prop_string = ""
            get_string = ""
            set_string = ""
            const_string = "\r\n    public " + className + "("
            const_string2 = ""
            const_string3 = "    public " + className + "() {}\r\n\r\n"
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
                get_string += "    public {0} get{1} () ".format(
                    dataType, propClassName) + "{ return this." + propertyName + ";}\r\n\r\n"
                set_string += "    public void set{0} ({1} {2}) ".format(
                    propClassName, dataType, propertyName) + "{ this."+propertyName+" = "+propertyName+";}\r\n\r\n"

                const_string2 += "        this." + propertyName + "=" + propertyName + ";\r\n"
                count = count + 1

            const_string = const_string[0:len(const_string)-1]
            const_string += ") {\r\n"
            const_string = const_string + const_string2 + "    }\r\n\r\n"

            tostring_string = tostring_string[0:len(tostring_string)-2]
            tostring_string = ""+tostring_string
            tostring_string += " \"}\";\r\n    }"

            prop_string = "    @Id\r\n    @GeneratedValue(strategy = GenerationType.IDENTITY)\r\n" + \
                prop_string

            string += prop_string + const_string + const_string3 + \
                get_string + set_string + tostring_string + "\r\n}"

            # 文件路径
            pojoFilePath = self.pathPrefix + "model/" + className + ".java"

            Log.info("pojo", "开始生成：" + pojoFilePath)

            # 创建文件
            f = open(pojoFilePath, mode='w+')
            f.write(string)
            f.close()

    def createMapper(self, tableInfos):
        Log.blank()
        Log.info("create_mapper", "生成 java mappers")

        for tableInfo in tableInfos:

            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = TableUtil.className(tableName)

            # 对应的实例名称
            instanceName = TableUtil.instanceName(tableName)

            string = "package " + self.packageName + ".mapper;\r\n"
            string += "import org.apache.ibatis.annotations.*;\r\n\r\n"
            string += "import java.util.List;\r\n"
            string += "import org.springframework.stereotype.Component;\r\n\r\n"
            string += "import " + self.packageName + ".model." + className + ";\r\n"
            string += "import " + self.packageName + \
                ".provider." + className + "Provider;\r\n\r\n"
            string += "@Component(value = \"" + className + "Mapper\")\r\n"
            string += "@Mapper\r\n"
            string += "public interface " + className + "Mapper {\r\n\r\n"
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
            string += "}"

            filepath = self.pathPrefix + "/mapper/" + className + "Mapper.java"
            Log.info("mapper", "开始生成："+filepath)
            f = open(filepath, mode='w+')
            f.write(string)
            f.close()

    def createProvider(self, tableInfos):
        Log.blank()
        Log.info("create_provider", "生成 java providers")

        for tableInfo in tableInfos:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = TableUtil.className(tableName)

            # 对应的实例名称
            instanceName = TableUtil.instanceName(tableName)

            # 字段属性列表
            columns = tableInfo["columns"]

            string = "package " + self.packageName + ".provider;\r\n\r\n"
            string += "import java.util.Map;\r\n\r\n"
            string += "import " + self.packageName + ".model." + className + ";\r\n\r\n"
            string += "public class " + className + "Provider {\r\n\r\n"

            if_string = ""
            insert_string = "        String key = \"\";\r\n        String value = \"\";\r\n"
            update_string = "        String sql = \"\";\r\n"

            colum_string = ""
            for columnInfo in columns:
                # 字段名称
                # propName = columnInfo["name"]
                propertyName = TableUtil.instanceName(columnInfo["name"])
                propClassName = TableUtil.className(columnInfo["name"])

                # 字段类型
                columType = columnInfo["columnProperty"].split('(')[0]
                columType = columType.strip()
                columType = columType.upper()

                if (propertyName == 'id' or
                        columType == 'REAL'):

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
                        ".get" + propClassName + "() > 0) {\r\n"

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

                colum_string += " " + propertyName + ","

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

            filepath = self.pathPrefix + "provider/" + className + "Provider.java"
            Log.info("provider", "开始生成："+filepath)
            f = open(filepath, mode='w+')
            f.write(string)
            f.close()

    def createService(self, tableInfos):
        Log.blank()
        Log.info("create_service", "生成 java service")

        for tableInfo in tableInfos:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = TableUtil.className(tableName)

            # 对应的实例名称
            instanceName = TableUtil.instanceName(tableName)

            string = "package " + self.packageName + ".service;\r\n\r\n"
            string += "import java.util.*;\r\n"
            string += "import org.springframework.beans.factory.annotation.Autowired;\r\n"
            string += "import org.springframework.validation.annotation.Validated;\r\n"
            string += "import org.springframework.web.bind.annotation.*;\r\n"
            string += "import org.springframework.stereotype.Service;\r\n\r\n"
            string += "import " + self.packageName + ".model." + className + ";\r\n"
            string += "import " + self.packageName + ".mapper." + className + "Mapper;\r\n"
            string += "import " + self.packageName + ".utils.Pager;\r\n"
            string += "import " + self.packageName + ".utils.ResponseStatus;\r\n\r\n"
            string += "@Service\r\n"
            string += "public class " + className + "Service {\r\n\r\n"
            string += "    @Autowired\r\n"
            string += "    private " + className + \
                "Mapper " + instanceName + "Mapper; \r\n\r\n"
            # string += "    @Autowired\r\n"
            # string += "    private " + className + \
            #     "Repository " + instanceName + "Repository; \r\n\r\n"
            string += "    @Autowired\r\n"
            string += "    private ResponseService responseService; \r\n\r\n"
            string += "    // 获取列表\r\n"
            string += "    public HashMap<String, Object> list(Pager page,@Validated " + \
                className + " " + instanceName + ") {\r\n"
            string += "        \r\n"
            string += "        List<" + className + "> list = " + \
                instanceName + \
                "Mapper.list(page.getPage(),page.getSize());\r\n"
            string += "        \r\n"
            string += "        HashMap map = responseService.getReturnResponse(ResponseStatus.success,list);\r\n"
            string += "        \r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "    // 删除\r\n"
            string += "    public HashMap<String, Object> delete(@PathVariable(\"id\") Long id) {\r\n"
            string += "        \r\n"
            string += "        " + instanceName + "Mapper.delete(id);\r\n"
            string += "        \r\n"
            string += "        HashMap map = responseService.getReturnResponse(ResponseStatus.success,null);\r\n"
            string += "        \r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "    // 查看详情\r\n"
            string += "    public HashMap<String, Object> show(@PathVariable(\"id\") Long id) {\r\n"
            string += "        \r\n"
            string += "        " + className + " " + instanceName + \
                " = " + instanceName + "Mapper.show(id);\r\n"
            string += "        \r\n"
            string += "        HashMap map = responseService.getReturnResponse(ResponseStatus.success," + \
                instanceName + ");\r\n"
            string += "        \r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "    // 插入，保存\r\n"
            string += "    public HashMap<String, Object> store(@Validated " + \
                className + " " + instanceName + ") {\r\n"
            string += "        \r\n"
            string += "        Long id = " + instanceName + ".getId();\r\n"
            string += "        \r\n"
            string += "        Boolean res = true;\r\n"
            string += "        if (id != null && id > 0) {\r\n"
            string += "            res = " + instanceName + \
                "Mapper.update(" + instanceName + ");\r\n"
            string += "        } else {\r\n"
            string += "            res = " + instanceName + \
                "Mapper.insert(" + instanceName + ");\r\n"
            string += "        }\r\n"
            string += "        \r\n"
            string += "        HashMap map = responseService.getReturnResponse(res ? ResponseStatus.success : ResponseStatus.error," + \
                instanceName + ");\r\n"
            string += "        \r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "}\r\n\r\n"

            filepath = self.pathPrefix + "service/" + className + "Service.java"
            Log.info("Service", "开始生成："+filepath)
            f = open(filepath, mode='w+')
            f.write(string)
            f.close()

    def createController(self, tableInfos):
        Log.blank()
        Log.info("create_controller", "生成 java controller")

        for tableInfo in tableInfos:

            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = TableUtil.className(tableName)

            # 对应的实例名称
            instanceName = TableUtil.instanceName(tableName)

            string = "package " + self.packageName + ".controller;\r\n\r\n"
            string += "import java.util.*;\r\n\r\n"
            string += "import org.springframework.beans.factory.annotation.Autowired;\r\n"
            string += "import org.springframework.validation.annotation.Validated;\r\n"
            string += "import org.springframework.web.bind.annotation.*;\r\n\r\n"
            string += "import " + self.packageName + ".model." + className + ";\r\n"
            string += "import " + self.packageName + \
                ".service." + className + "Service;\r\n"
            string += "import " + self.packageName + ".utils.Pager;\r\n\r\n"
            string += "@RequestMapping(\"/" + instanceName + "\")\r\n"
            string += "@RestController\r\n"
            string += "public class " + className + "Controller {\r\n\r\n"
            string += "    @Autowired\r\n"
            string += "    private " + className + \
                "Service " + instanceName + "Service; \r\n\r\n"
            string += "    // 获取列表\r\n"
            string += "    @GetMapping\r\n"
            string += "    public HashMap<String, Object> list(Pager page," + \
                className + " " + instanceName + ") {\r\n"
            string += "        \r\n"
            string += "        HashMap map = " + instanceName + \
                "Service.list(page," + instanceName + ");\r\n"
            string += "        \r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "    // 删除\r\n"
            string += "    @GetMapping(\"/delete/{id}\")\r\n"
            string += "    public HashMap<String, Object> delete(@PathVariable(\"id\") Long id) {\r\n"
            string += "        \r\n"
            string += "        HashMap map = " + \
                instanceName + "Service.delete(id);\r\n"
            string += "        \r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "    // 查看详情\r\n"
            string += "    @GetMapping(\"/{id}\")\r\n"
            string += "    public HashMap<String, Object> show(@PathVariable(\"id\") Long id) {\r\n"
            string += "        \r\n"
            string += "        HashMap map = " + \
                instanceName + "Service.show(id);\r\n"
            string += "        \r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "    // 插入，保存\r\n"
            string += "    @PostMapping\r\n"
            string += "    @Validated\r\n"
            string += "    public HashMap<String, Object> store(@RequestBody " + \
                className + " " + instanceName + ") {\r\n"
            string += "        \r\n"
            string += "        HashMap map = " + instanceName + \
                "Service.store(" + instanceName + ");\r\n"
            string += "        \r\n"
            string += "        return map;\r\n"
            string += "    }\r\n"
            string += "}\r\n\r\n"

            filepath = self.pathPrefix + "controller/" + className + "Controller.java"
            Log.info("controller", "开始生成："+filepath)
            f = open(filepath, mode='w+')
            f.write(string)
            f.close()

    def createUtil(self):
        Log.blank()
        Log.info("create_utils", "生成 utils 文件")

        files = [self.pathPrefix+"utils/Pager.java",
                 self.pathPrefix+"utils/ResponseStatus.java",
                 self.pathPrefix+"service/ResponseService.java"]

        for file_path in files:

            Log.info("utils", "开始生成："+file_path)
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
                string += "        Integer page_start = (page-1)*size;\r\n"
                string += "        Integer page_end = page*size;\r\n"
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
