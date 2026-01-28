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
    javaPath = ""
    visible_controllers = []
    modelIgnoreAutoId = []
    modelDtoIgnore = []
    modelIgnore = []
    split_string = "// ############ 自动生成 ############"

    @staticmethod
    def create(info, mode, names):
        javaCreator = JavaCreator()

        # ------------ 准备路径信息
        javaCreator.package_name = info["java"]["packageName"]
        javaCreator.visible_controllers = info["java"]["visibleControllers"]
        javaCreator.modelIgnoreAutoId = info["java"]["modelIgnoreAutoId"]
        javaCreator.modelDtoIgnore = info["java"]["modelDtoIgnore"]
        javaCreator.modelIgnore = info["java"]["modelIgnore"]
        javaCreator.javaPath = info["path"] + info["java"]["path"]
        
        p = javaCreator.package_name.split(".")
        p = "/".join(p)
        javaCreator.package_path = javaCreator.javaPath + "src/main/java/" + p + "/"
        
        Log.info("admin", "源目录：" + javaCreator.package_path)

        if not FileUtil.path_exists(javaCreator.package_path):
            Log.error("java_creator", "源目录不存在，请指定源目录")
            return 0

        Log.blank()
        Log.info(
            "java", "================ 正在为`{0}`生成java文件 ================".format(names))

        # 备份目录
        FileUtil.pack_dir(javaCreator.package_path, info["path"] + info["backUpPath"] + "/java/")

        # ------------ 执行操作
        tableList = CreateUtil.get_tableInfo_width_names(info, names)
        if len(tableList) == 0:
            Log.error(
                "java", "字段 `{0}` 不存在".format(names))
            return 0
        
        if len(names) == 0:
            JavaCreator.__cmd_error()
        elif mode == "-d":
            javaCreator.clearDir()
        elif mode == "-all":
            # javaCreator.create_model(tableList)
            # javaCreator.create_dto(tableList, info["db"]["dto"])
            # javaCreator.create_repository(tableList)
            # javaCreator.create_controller(tableList)
            # javaCreator.create_mapper(tableList)
            # javaCreator.create_provider(tableList)
            javaCreator.create_model(tableList)
            javaCreator.create_mapper(tableList)
            javaCreator.create_service(tableList)
            javaCreator.create_controller(tableList)
            javaCreator.create_dao(tableList)
            javaCreator.create_vo(tableList)

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

    def create_dto(self, table_info_list, dto_info):
        """
        @summary: 创建model实体类
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建model实体类 ================")

        parseMap = {
            "REAL": "Long.valueOf",
            'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Integer.valueOf",
            'BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Long.valueOf",
            "INT": "Integer.valueOf",
            "TINYINT": "Integer.valueOf",
            "SMALLINT": "Integer.valueOf",
            "MEDIUMINT": "Long.valueOf",
            "BIGINT": "Long.valueOf",
            "FLOAT": "Float.valueOf",
            "DOUBLE": "Double.valueOf",
            "CHAR": "",
            "VARCHAR": "",
            "TINYTEXT": "",
            "TEXT": "",
            "MEDIUMTEXT": "",
            "LONGTEXT": "",
            "BOOL": "Boolean.valueOf",
            "BOOLEAN": "Boolean.valueOf",
            "DATETIME": "Timestamp.valueOf",
            "DATE": "Timestamp.valueOf",
            "TIME": "Timestamp.valueOf",
            "TIMESTAMP": "Timestamp.valueOf",
        }

        coulumTypeTemp = {
            "REAL": "Long",
            'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Integer",
            'BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Long",
            "INT": "Integer",
            "TINYINT": "Integer",
            "SMALLINT": "Integer",
            "MEDIUMINT": "Long",
            "BIGINT": "Long",
            "CHAR": "String",
            "VARCHAR": "String",
            "TINYTEXT": "String",
            "TEXT": "String",
            "MEDIUMTEXT": "String",
            "LONGTEXT": "String",
            "FLOAT": "Float",
            "DOUBLE": "Double",
            "BOOLEAN": "boolean",
            "BOOL": "boolean",
            "DATETIME": "Timestamp",
            "DATE": "Timestamp",
            "TIME": "Timestamp",
            "TIMESTAMP": "Timestamp",
        }

        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            if (tableName in self.modelDtoIgnore) == True:
                Log.warn(f"!!! table_name: {tableName} modelDtoIgnore 中，所以忽略")
                continue
            
            # 产生的类名称
            className = CreateUtil.camelize(tableName)
            
            # 字段属性列表
            columns = copy.deepcopy(tableInfo["columns"])
            
            # 文件信息
            string = self.split_string+ "\r\n"
            string += "package " + self.package_name + ".dto;\r\n\r\n"
            string += 'import java.util.Map;\r\n'
            string += 'import java.sql.Timestamp;\r\n'
            string += '\r\n'
            string += 'import jakarta.persistence.Column;\r\n'
            string += 'import jakarta.persistence.GeneratedValue;\r\n'
            string += 'import jakarta.persistence.GenerationType;\r\n'
            string += 'import jakarta.persistence.EntityListeners;\r\n'
            string += 'import jakarta.persistence.Id;\r\n'
            string += '\r\n'
            string += 'import org.springframework.data.annotation.CreatedDate;\r\n'
            string += 'import org.springframework.data.annotation.LastModifiedDate;\r\n'
            string += '\r\n'
            string += 'import lombok.Data;\r\n'
            string += 'import lombok.NoArgsConstructor;\r\n'
            string += 'import lombok.ToString;\r\n'
            string += 'import lombok.AllArgsConstructor;\r\n'
            string += '\r\n'
            string += '@Data\r\n'
            string += '\r\n'
            string += '@ToString\r\n'
            string += '@NoArgsConstructor\r\n'
            string += '@AllArgsConstructor\r\n'
            string += "public class " + className + "DTO {\r\n\r\n"
            
            prop_string = ""
            json_string = "    public void fromMap(Map<String, Object> map) {\r\n"

            for columnInfo in columns:

                # 字段名称
                propertyName = columnInfo["name"]

                # 字段描述
                des = columnInfo["des"]

                # 字段类型
                columType = columnInfo["columnProperty"].split('(')[0]
                columType = columType.split(' ')[0]
                columType = columType.strip()
                columType = columType.upper()
                dataType = coulumTypeTemp[columType]
                instPropertyName = CreateUtil.instance_name(propertyName)
                if propertyName == "id":
                    dataType = "Long"
                    prop_string += "    @Id\r\n"
                    if tableName != "user":
                        prop_string += "    @GeneratedValue(strategy = GenerationType.IDENTITY)\r\n"

                if propertyName == "create_at":
                    prop_string += '\r\n    @CreatedDate\r\n'
                    prop_string += '    @Column(name="create_at", updatable=false)\r\n'

                if propertyName == "update_at":
                    prop_string += '\r\n    @LastModifiedDate\r\n'
                    prop_string += '    @Column(name="update_at")\r\n'

                if dataType == "":
                    prop_string += '@JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")'

                prop_string += "    private {0} {1}; //{2} \r\n".format(
                    dataType, instPropertyName, des)

                json_string += "        if (map.get(\"" +     instPropertyName + "\") != null) {\r\n"
                if propertyName == "id":
                    json_string += "            " + instPropertyName + " = " +     parseMap["REAL"] +     "(map.get(\"" + instPropertyName + "\").toString());\r\n"
                else:
                    if columType in "CHAR,VARCHAR,TINYTEXT,TEXT,MEDIUMTEXT,LONGTEXT":
                        json_string += "            " + instPropertyName + " = " +     parseMap[columType] +     "map.get(\"" + instPropertyName + "\").toString();\r\n"
                    else:
                        json_string += "            " + instPropertyName + " = " +     parseMap[columType] +     "(map.get(\"" + instPropertyName + "\").toString());\r\n"
                json_string += "        }\r\n\r\n"

            # 获取dto下的数据
            liKeys = dto_info.keys()
            for key in liKeys:
                tableProps = dto_info[key]
                tableTitle = key.split(":")[0]

                if tableTitle == tableName:
                    for li in tableProps:
                        columInfo = li.split(":")
                        columName = columnInfo[0]
                        columDesc = columnInfo[1]
                        columProps = columnInfo[2]
                        columType = columProps.split('(')[0]

                        prop_string += "    private {0} {1}; //{2} \r\n".format(
                        dataType, instPropertyName, des)

            prop_string +="\r\n"

            json_string = json_string[0:len(json_string)-2]
            json_string += "    }\r\n"

            string += prop_string
            string += "}\r\n"
            string += self.split_string + "\r\n"

            # 生成文件
            self._generate_file_with_dir(string, "dto", className + "DTO.java", force=True)

    def create_repository(self, table_info_list):
        """
        @summary: 创建Repository
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建Repository ================")
        
        for tableInfo in table_info_list:
            self.create_empty_repository(tableInfo)

    def create_controller1(self, table_info_list):
        """
        @summary: 创建Controller
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建Controller ================")
        
        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            print(f">>>>>>>> {self.visible_controllers}")

            if self.visible_controllers is not None and len(self.visible_controllers) > 0:
                if (tableName in self.visible_controllers) == False:
                    Log.warn(f"!!! table_name: {tableName} 存在在visible_controllers 中，所以忽略")
                    continue

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的类名称
            instanceName = CreateUtil.instance_name(tableName)

            # 登录功能
            addUserLogin = tableName == "user"

            # 文件名称
            fileName = className + "Controller.java"
            
            self.create_empty_controller(tableInfo)
            
            contentString = "\r\n"

            fileDir = self.package_path + "controller" + "/"
            filePath = fileDir + fileName
            fileContent = FileUtil.read_file(filePath)
            fileContent = "".join(fileContent)
            fileContent = fileContent.split(self.split_string)
            fileContent = fileContent[2]

            if addUserLogin:
                contentString += '    @Autowired\r\n'
                contentString += f'    UserCommonService userCommonService;\r\n'
                contentString += '    \r\n'
            
            if addUserLogin:
                contentString += '    // 手机号登录\r\n'
                contentString += '    @PostMapping("loginByPhone")\r\n'
                contentString += '    public HashMap<String, Object> loginByPhone(@RequestBody Map<String, Object> param) {\r\n'
                contentString += '        String phone = "";\r\n'
                contentString += '        String smsCode = "";\r\n'
                contentString += '        if (param.containsKey("phone")) {\r\n'
                contentString += '            phone = (String) param.get("phone");\r\n'
                contentString += '        } else {\r\n'
                contentString += '\r\n'
                contentString += '            return ResponseService.error("phone 为空！");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        if (param.containsKey("smsCode")) {\r\n'
                contentString += '            smsCode = (String) param.get("smsCode");\r\n'
                contentString += '        } else {\r\n'
                contentString += '\r\n'
                contentString += '            return ResponseService.error("smsCode 为空！");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        return userCommonService.loginByPhone(phone, smsCode);\r\n'
                contentString += '    }\r\n'
                contentString += '\r\n'
                contentString += '    // 账号密码登录\r\n'
                contentString += '    @PostMapping("loginByPassword")\r\n'
                contentString += '    public HashMap<String, Object> loginByPassword(@RequestBody Map<String, Object> param) {\r\n'
                contentString += '        String userName = "";\r\n'
                contentString += '        String password = "";\r\n'
                contentString += '        if (param.containsKey("userName")) {\r\n'
                contentString += '            userName = (String) param.get("userName");\r\n'
                contentString += '        } else {\r\n'
                contentString += '            return ResponseService.error("参数错误：userName 为空！");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        if (param.containsKey("password")) {\r\n'
                contentString += '            password = (String) param.get("password");\r\n'
                contentString += '        } else {\r\n'
                contentString += '\r\n'
                contentString += '            return ResponseService.error("password 为空！");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        return userCommonService.loginByPassword(userName, password);\r\n'
                contentString += '    }\r\n'
                contentString += '\r\n'
                contentString += '    // 手机号注册\r\n'
                contentString += '    @PostMapping("registerByPhone")\r\n'
                contentString += '    public HashMap<String, Object> registerByPhone(@RequestBody Map<String, Object> param) throws CustomException {\r\n'
                contentString += '        String phone = "";\r\n'
                contentString += '        String smsCode = "";\r\n'
                contentString += '        String inviteCode = "";\r\n'
                contentString += '        if (param.containsKey("phone")) {\r\n'
                contentString += '            phone = (String) param.get("phone");\r\n'
                contentString += '        } else {\r\n'
                contentString += '\r\n'
                contentString += '            return ResponseService.error("phone 为空！");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        if (param.containsKey("smsCode")) {\r\n'
                contentString += '            smsCode = (String) param.get("smsCode");\r\n'
                contentString += '        } else {\r\n'
                contentString += '\r\n'
                contentString += '            return ResponseService.error("smsCode 为空！");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        if (param.containsKey("inviteCode")) {\r\n'
                contentString += '            inviteCode = (String) param.get("inviteCode");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        return userCommonService.registerByPhone(phone, smsCode, inviteCode);\r\n'
                contentString += '    }\r\n'
                contentString += '\r\n'
                contentString += '    // 账号密码注册\r\n'
                contentString += '    @PostMapping("registerByPassword")\r\n'
                contentString += '    public HashMap<String, Object> registerByPassword(@RequestBody Map<String, Object> param) throws CustomException {\r\n'
                contentString += '        String userName = "";\r\n'
                contentString += '        String password = "";\r\n'
                contentString += '        String inviteCode = "";\r\n'
                contentString += '        if (param.containsKey("userName")) {\r\n'
                contentString += '            userName = (String) param.get("userName");\r\n'
                contentString += '        } else {\r\n'
                contentString += '            return ResponseService.error("参数错误：userName 为空！");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        if (param.containsKey("password")) {\r\n'
                contentString += '            password = (String) param.get("password");\r\n'
                contentString += '        } else {\r\n'
                contentString += '\r\n'
                contentString += '            return ResponseService.error("password 为空！");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        if (param.containsKey("inviteCode")) {\r\n'
                contentString += '            inviteCode = (String) param.get("inviteCode");\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        return userCommonService.registerByPassword(userName, password, inviteCode);\r\n'
                contentString += '    }\r\n'
                contentString += '\r\n'
                contentString += '    @GetMapping("/getUserInfo")\r\n'
                contentString += '    @Validated\r\n'
                contentString += '    public HashMap<String, Object> getUserInfo() throws CustomException {\r\n'
                contentString += '\r\n'
                contentString += '        return userCommonService.getUserInfo();\r\n'
                contentString += '    }\r\n'
                contentString += '\r\n'

            if 'public HashMap<String, Object> list(' not in fileContent:
                contentString += '    // 获取列表\r\n'
                contentString += '    @GetMapping\r\n'
                contentString += '    public HashMap<String, Object> list(@RequestParam Map<String, Object> param) {\r\n'
                contentString += '\r\n'
                contentString += '        Pageable pageable = PageUtil.getPageableWitParam(param, "createAt", false);\r\n'
                contentString += f'        Page<{className}> list =  {instanceName}Repository.findAll(pageable);\r\n'
                contentString += '        return ResponseService.success("成功！", list);\r\n'
                contentString += '    }\r\n'
                contentString += '\r\n'

            if 'public HashMap<String, Object> delete(' not in fileContent:
                contentString += '    // 删除\r\n'
                contentString += '    @GetMapping("/delete/{id}")\r\n'
                contentString += '    public HashMap<String, Object> delete(@PathVariable("id") Long id) {\r\n'
                contentString += f'        {className} temp = new {className}();\r\n'
                contentString += f'        temp.setId(id);\r\n'
                contentString += f'        {instanceName}Repository.delete(temp);\r\n'
                contentString += '        return ResponseService.success("成功！", null);\r\n'
                contentString += '    }\r\n'
                contentString += '\r\n'

            if 'public HashMap<String, Object> show(' not in fileContent:
                contentString += '    // 查看详情\r\n'
                contentString += '    @GetMapping("/{id}")\r\n'
                contentString += '    public HashMap<String, Object> show(@PathVariable("id") Long id) {\r\n'
                contentString += f'        {className} temp = {instanceName}Repository.findById(id).orElse(null);\r\n'
                contentString += '\r\n'
                contentString += '        if (temp == null) {\r\n'
                contentString += '            return ResponseService.error("数据不存在！");\r\n'
                contentString += '        }\r\n'
                contentString += '        return ResponseService.success("成功！", temp);\r\n'
                contentString += '    }\r\n'
                contentString += '\r\n'
            
            if 'public HashMap<String, Object> store('not in fileContent:
                contentString += '    // 插入，保存功能；这个接口会把数据全都替换掉\r\n'
                contentString += '    @PostMapping\r\n'
                contentString += '    @Validated\r\n'
                contentString += f'    public HashMap<String, Object> store(@RequestBody {className} temp) ' + '{\r\n'
                contentString += '\r\n'
                contentString += f'        temp = {instanceName}Repository.save(temp);\r\n'
                contentString += '        return ResponseService.success("成功！", temp);\r\n'
                contentString += '    }\r\n'

            if 'public HashMap<String, Object> save('not in fileContent:
                contentString += '\r\n    // 插入，保存功能；这个接口只会替换有值的数据，null的不替换\r\n'
                contentString += '    @PostMapping("/save")\r\n'
                contentString += '    @Validated\r\n'
                contentString += f'    public HashMap<String, Object> save(@RequestBody {className} temp) ' + '{\r\n'
                contentString += '\r\n'
                contentString += f'        {className} b;\r\n'
                contentString += '        if (temp.getId() != null) {\r\n'
                contentString += f'            b = {instanceName}Repository.findById(temp.getId()).orElse(null);\r\n'
                contentString += '            if (b == null) {\r\n'
                contentString += '                return ResponseService.error("id不存在");\r\n'
                contentString += '            }\r\n'
                contentString += '            else {\r\n'
                contentString += '                BeanUtils.copyProperties(temp, b, ObjectSerializeUtil.getNullPropertyNames(temp));\r\n'
                contentString += f'                {instanceName}Repository.save(b);\r\n'
                contentString += '            }\r\n'
                contentString += '        }\r\n'
                contentString += '        else {\r\n'
                contentString += f'            b = {instanceName}Repository.save(temp);\r\n'
                contentString += '        }\r\n'
                contentString += '\r\n'
                contentString += '        return ResponseService.success("成功！", b);\r\n'
                contentString += '    }\r\n'

            contentString += '    '
            
            self._generate_file_with_dir(contentString, "controller", fileName, force=False)

    def create_provider(self, tableInfo):

        for tableInfo in tableInfo:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的实例名称
            instanceName = CreateUtil.instance_name(tableName)

            # 字段属性列表
            columns = tableInfo["columns"]
            # columns = TableUtil.addModelDefaultProperty(columns)

            string = "package " + self.package_name + ".provider;\r\n\r\n"
            string += "import com.qlzw.smartwc.dao." + className + ";\r\n\r\n"
            string += "import java.util.Map;\r\n\r\n"
            string += "public class " + className + "Provider {\r\n\r\n"

            if_string = ""
            insert_string = "        String key = \"\";\r\n        String value = \"\";\r\n"
            update_string = "        String sql = \"\";\r\n"

            colum_string = ""
            for columnInfo in columns:
                # 字段名称
                propertyName = CreateUtil.instance_name(columnInfo["name"])
                propClassName = CreateUtil.camelize(columnInfo["name"])

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

            string += "    //### 自动生成 ###\r\n"
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
            string += "    //### 自动生成 ###\r\n"
            string += "}\r\n"

            filepath = self.package_path + "provider/" + className + "Provider.java"
            Log.success("Provider", "生成："+filepath)
            f = open(filepath, mode='w+')
            f.write(string)
            f.close()

    def create_empty_repository(self, tableInfo):
        # 表名称
        tableName = tableInfo["name"]

        # 对应的类名称
        className = CreateUtil.camelize(tableName)

        dirName = "repository"
        fileName = className + "Repository.java"
        filePath = self.package_path + dirName + "/" + fileName
        if FileUtil.path_exists(filePath) == False:
            string = "package " + self.package_name + ".repository;\r\n\r\n"
            string += "\r\n"
            string += "import org.springframework.data.jpa.repository.JpaRepository;\r\n"
            string += "import org.springframework.stereotype.Repository;\r\n"
            string += "\r\n"
            string += "import " + self.package_name + f".dao.{className};\r\n"
            string += "\r\n"
            string += "@Repository\r\n"
            string += f"public interface {className}Repository extends JpaRepository<{className}, Long>"+"{\r\n"
            string += '    \r\n'
            string += f'    {self.split_string}\r\n'
            string += f'    {self.split_string}\r\n'
            string += '    \r\n'
            string += '}\r\n'

            self._generate_file_with_dir(string, dirName, fileName, force=True)

    def create_empty_controller(self, tableInfo):
        # 表名称
        tableName = tableInfo["name"]

        # 对应的类名称
        className = CreateUtil.camelize(tableName)

        # 对应的类名称
        instanceName = CreateUtil.instance_name(tableName)

        dirName = "controller"
        fileName = className + "Controller.java"
        filePath = self.package_path + dirName + "/" + fileName
        if FileUtil.path_exists(filePath) == False:
            string = f"package {self.package_name}.controller;\r\n\r\n"
            string += "import java.util.*;\r\n"
            string += "\r\n"
            string += 'import org.springframework.beans.BeanUtils;\r\n'
            string += 'import org.springframework.data.domain.Page;\r\n'
            string += f'import {self.package_name}.exception.CustomException;\r\n'
            string += 'import org.springframework.data.domain.Pageable;\r\n'
            string += 'import org.springframework.web.bind.annotation.*;\r\n'
            string += 'import org.springframework.validation.annotation.Validated;\r\n'
            string += 'import org.springframework.beans.factory.annotation.Autowired;\r\n'
            string += '\r\n'
            string += f'import {self.package_name}.dao.{className};\r\n'
            string += f'import {self.package_name}.repository.{className}Repository;\r\n'
            string += f'import com.common.utils.*;\r\n'
            string += "\r\n"
            string += "@RequestMapping(\"/" + instanceName + "\")\r\n"
            string += "@RestController\r\n"
            string += "public class " + className + "Controller {\r\n"
            string += '    \r\n'
            string += '    @Autowired\r\n'
            string += f'    {className}Repository {instanceName}Repository;\r\n'
            string += '    \r\n'
            string += f'    {self.split_string}\r\n'
            string += f'    {self.split_string}\r\n'
            string += '    \r\n'
            string += '}\r\n'

            self._generate_file_with_dir(string, dirName, fileName, force=True)


    def create_model(self, table_info_list):
        """
        @summary: 创建model实体类
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建model实体类 ================")

        parseMap = {
            "REAL": "Long.valueOf",
            'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Integer.valueOf",
            'BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Long.valueOf",
            "INT": "Integer.valueOf",
            "TINYINT": "Integer.valueOf",
            "SMALLINT": "Integer.valueOf",
            "MEDIUMINT": "Long.valueOf",
            "BIGINT": "Long.valueOf",
            "FLOAT": "Float.valueOf",
            "DOUBLE": "Double.valueOf",
            "CHAR": "",
            "VARCHAR": "",
            "TINYTEXT": "",
            "TEXT": "",
            "MEDIUMTEXT": "",
            "LONGTEXT": "",
            "BOOL": "Boolean.valueOf",
            "BOOLEAN": "Boolean.valueOf",
            "DATETIME": "Timestamp.valueOf",
            "DATE": "Timestamp.valueOf",
            "TIME": "Timestamp.valueOf",
            "TIMESTAMP": "Timestamp.valueOf",
        }

        coulumTypeTemp = {
            "REAL": "Long",
            'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Integer",
            'BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Long",
            "INT": "Integer",
            "TINYINT": "Integer",
            "SMALLINT": "Integer",
            "MEDIUMINT": "Long",
            "BIGINT": "Long",
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

        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            if (tableName in self.modelIgnore) == True:
                Log.warn(f"!!! table_name: {tableName} modelIgnore 中，所以忽略")
                continue
            
            # 产生的类名称
            className = CreateUtil.camelize(tableName)
            
            # dir名称
            instanceName = CreateUtil.instance_name(tableName)
            
            # 字段属性列表
            columns = copy.deepcopy(tableInfo["columns"])
            
            # 文件信息
            string = self.split_string+ "\r\n"
            string += f"package {self.package_name}.{instanceName};\r\n\r\n"
            string += 'import java.util.Map;\r\n'
            string += 'import java.sql.Timestamp;\r\n'
            string += '\r\n'
            string += 'import lombok.*;\r\n'
            string += '\r\n'
            string += '@Getter\r\n'
            string += '@Setter\r\n'
            string += '@ToString\r\n'
            string += '@NoArgsConstructor\r\n'
            string += '@AllArgsConstructor\r\n'
            string += "public class " + className + " {\r\n\r\n"
            
            prop_string = ""
            json_string = "    public void fromMap(Map<String, Object> map) {\r\n"

            for columnInfo in columns:

                # 字段名称
                propertyName = columnInfo["name"]

                # 字段描述
                des = columnInfo["des"]

                # 字段类型
                columType = columnInfo["columnProperty"].split('(')[0]
                columType = columType.split(' ')[0]
                columType = columType.strip()
                columType = columType.upper()
                dataType = coulumTypeTemp[columType]
                instPropertyName = CreateUtil.instance_name(propertyName)
                if propertyName == "id":
                    dataType = "Long"

                    # if (tableName in self.modelIgnoreAutoId) == False:
                        # prop_string += "    @GeneratedValue(strategy = GenerationType.IDENTITY)\r\n"

                # if propertyName == "create_at":
                #     prop_string += '\r\n    @CreatedDate\r\n'
                #     prop_string += '    @Column(name="create_at", updatable=false)\r\n'

                # if propertyName == "update_at":
                #     prop_string += '\r\n    @LastModifiedDate\r\n'
                #     prop_string += '    @Column(name="update_at")\r\n'

                if dataType == "":
                    prop_string += '@JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")'

                prop_string += "    private {0} {1}; //{2} \r\n".format(
                    dataType, instPropertyName, des)

                json_string += "        if (map.get(\"" +     instPropertyName + "\") != null) {\r\n"
                if propertyName == "id":
                    json_string += "            " + instPropertyName + " = " +     parseMap["REAL"] +     "(map.get(\"" + instPropertyName + "\").toString());\r\n"
                else:
                    if columType in "CHAR,VARCHAR,TINYTEXT,TEXT,MEDIUMTEXT,LONGTEXT":
                        json_string += "            " + instPropertyName + " = " +     parseMap[columType] +     "map.get(\"" + instPropertyName + "\").toString();\r\n"
                    else:
                        json_string += "            " + instPropertyName + " = " +     parseMap[columType] +     "(map.get(\"" + instPropertyName + "\").toString());\r\n"
                json_string += "        }\r\n\r\n"

            prop_string +="\r\n"

            json_string = json_string[0:len(json_string)-2]
            json_string += "    }\r\n"

            string += prop_string + json_string
            string += "}\r\n"
            string += self.split_string + "\r\n"

            # 生成文件
            self._generate_file_with_dir(string, instanceName, className + ".java", force=True)

    def create_vo(self, table_info_list):
        """
        @summary: 创建model实体类
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建model实体类 ================")

        parseMap = {
            "REAL": "Long.valueOf",
            'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Integer.valueOf",
            'BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Long.valueOf",
            "INT": "Integer.valueOf",
            "TINYINT": "Integer.valueOf",
            "SMALLINT": "Integer.valueOf",
            "MEDIUMINT": "Long.valueOf",
            "BIGINT": "Long.valueOf",
            "FLOAT": "Float.valueOf",
            "DOUBLE": "Double.valueOf",
            "CHAR": "",
            "VARCHAR": "",
            "TINYTEXT": "",
            "TEXT": "",
            "MEDIUMTEXT": "",
            "LONGTEXT": "",
            "BOOL": "Boolean.valueOf",
            "BOOLEAN": "Boolean.valueOf",
            "DATETIME": "Timestamp.valueOf",
            "DATE": "Timestamp.valueOf",
            "TIME": "Timestamp.valueOf",
            "TIMESTAMP": "Timestamp.valueOf",
        }

        coulumTypeTemp = {
            "REAL": "Long",
            'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Integer",
            'BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Long",
            "INT": "Integer",
            "TINYINT": "Integer",
            "SMALLINT": "Integer",
            "MEDIUMINT": "Long",
            "BIGINT": "Long",
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

        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            if (tableName in self.modelIgnore) == True:
                Log.warn(f"!!! table_name: {tableName} modelIgnore 中，所以忽略")
                continue
            
            # 产生的类名称
            className = CreateUtil.camelize(tableName)
            
            # dir名称
            instanceName = CreateUtil.instance_name(tableName)
            
            # 字段属性列表
            columns = copy.deepcopy(tableInfo["columns"])
            
            # 文件信息
            string = self.split_string+ "\r\n"
            string += f"package {self.package_name}.{instanceName};\r\n\r\n"
            string += 'import java.util.Map;\r\n'
            string += 'import java.sql.Timestamp;\r\n'
            string += '\r\n'
            string += 'import lombok.*;\r\n'
            string += '\r\n'
            string += '@Getter\r\n'
            string += '@Setter\r\n'
            string += '@ToString\r\n'
            string += '@NoArgsConstructor\r\n'
            string += '@AllArgsConstructor\r\n'
            string += "public class " + className + "VO {\r\n\r\n"
            
            prop_string = ""
            json_string = "    public void fromMap(Map<String, Object> map) {\r\n"

            for columnInfo in columns:

                # 字段名称
                propertyName = columnInfo["name"]

                # 字段描述
                des = columnInfo["des"]

                # 字段类型
                columType = columnInfo["columnProperty"].split('(')[0]
                columType = columType.split(' ')[0]
                columType = columType.strip()
                columType = columType.upper()
                dataType = coulumTypeTemp[columType]
                instPropertyName = CreateUtil.instance_name(propertyName)
                if propertyName == "id":
                    dataType = "Long"

                    # if (tableName in self.modelIgnoreAutoId) == False:
                        # prop_string += "    @GeneratedValue(strategy = GenerationType.IDENTITY)\r\n"

                # if propertyName == "create_at":
                #     prop_string += '\r\n    @CreatedDate\r\n'
                #     prop_string += '    @Column(name="create_at", updatable=false)\r\n'

                # if propertyName == "update_at":
                #     prop_string += '\r\n    @LastModifiedDate\r\n'
                #     prop_string += '    @Column(name="update_at")\r\n'

                if dataType == "":
                    prop_string += '@JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")'

                prop_string += "    private {0} {1}; //{2} \r\n".format(
                    dataType, instPropertyName, des)

                json_string += "        if (map.get(\"" +     instPropertyName + "\") != null) {\r\n"
                if propertyName == "id":
                    json_string += "            " + instPropertyName + " = " +     parseMap["REAL"] +     "(map.get(\"" + instPropertyName + "\").toString());\r\n"
                else:
                    if columType in "CHAR,VARCHAR,TINYTEXT,TEXT,MEDIUMTEXT,LONGTEXT":
                        json_string += "            " + instPropertyName + " = " +     parseMap[columType] +     "map.get(\"" + instPropertyName + "\").toString();\r\n"
                    else:
                        json_string += "            " + instPropertyName + " = " +     parseMap[columType] +     "(map.get(\"" + instPropertyName + "\").toString());\r\n"
                json_string += "        }\r\n\r\n"

            prop_string +="\r\n"

            json_string = json_string[0:len(json_string)-2]
            json_string += "    }\r\n"

            string += prop_string + json_string
            string += "}\r\n"
            string += self.split_string + "\r\n"

            # 生成文件
            self._generate_file_with_dir(string, instanceName, className + "VO.java", force=True)

    def create_mapper(self, tableInfo):

        for tableInfo in tableInfo:
            # 表名称
            tableName = tableInfo["name"]

            # 产生的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的类名称
            instanceName = CreateUtil.instance_name(tableName)

            path = self.package_path + "/"
            FileUtil.check_path(path)
            filePath = path + instanceName + "/" + className + "Mapper.java"

            print(f">>>> {filePath}")

            if FileUtil.path_exists(filePath):
                Log.info("文件已存在！")
            else:
                self.create_empty_mapper(tableInfo)

    def create_empty_mapper(self, tableInfo):
        
        # 表名称
        tableName = tableInfo["name"]

        # 对应的类名称
        className = CreateUtil.camelize(tableName)

        # 对应的类名称
        instanceName = CreateUtil.instance_name(tableName)
        
        context = ""
        fileName = className + "Mapper.java"

        context += f'package {self.package_name}.{instanceName};\n'
        context += '\n'
        context += 'import com.baomidou.mybatisplus.core.mapper.BaseMapper;\n'
        context += '\n'
        context += f'public interface {className}Mapper extends BaseMapper<{className}> {{\n'
        context += '\n'
        context += '}\n'
        context += '\n'

        self._generate_file_with_dir(context, instanceName, fileName, force=True)

    def create_service(self, table_info_list):
        
        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的类名称
            instanceName = CreateUtil.instance_name(tableName)

            path = self.package_path + "/"
            FileUtil.check_path(path)
            filePath = path + instanceName + "/" + className + "Service.java"

            if FileUtil.path_exists(filePath):
                Log.info("文件已存在！")
            else:
                self.create_empty_service(tableInfo)

    def create_empty_service(self, tableInfo):
        # 表名称
        tableName = tableInfo["name"]

        # 对应的类名称
        className = CreateUtil.camelize(tableName)

        # 对应的类名称
        instanceName = CreateUtil.instance_name(tableName)
        
        content = ""
        fileName = className + "Service.java"

        content += f"package {self.package_name}.{instanceName};\n"
        content += '\n'
        content += 'import com.baomidou.mybatisplus.core.metadata.IPage;\n'
        content += 'import com.baomidou.mybatisplus.extension.plugins.pagination.Page;\n'
        content += 'import com.common.base.BaseService;\n'
        content += 'import org.springframework.stereotype.Service;\n'
        content += '\n'
        content += 'import java.util.ArrayList;\n'
        content += 'import java.util.List;\n'
        content += 'import java.util.Map;\n'
        content += '\n'
        content += '@Service\n'
        content += f'public class {className}Service extends BaseService<{className}Dao, {className}> {{\n'
        content += '\n'
        content += f'    // 对外提供获取 {className}VO 列表的方法\n'
        content += f'    public IPage<{className}VO> listVO(Map<String, Object> param) {{\n'
        content += f'        // 获取 {className} 列表\n'
        content += f'        IPage<{className}> {className}Page = list(param);\n'
        content += f'        \n'
        content += f'        // 创建新的 Page 对象用于存放 {className}VO\n'
        content += f'        Page<{className}VO> {className}VOPage = new Page<>({className}Page.getCurrent(), {className}Page.getSize(), {className}Page.getTotal());\n'
        content += '        \n'
        content += '        // 转换列表数据\n'
        content += f'        List<{className}VO> {className}VOList = new ArrayList<>();\n'
        content += f'        for ({className} {className} : {className}Page.getRecords()) {{\n'
        content += f'            {className}VOList.add(baseDAO.convertToVO({className}, {className}VO.class));\n'
        content += '        }\n'
        content += '        \n'
        content += f'        {className}VOPage.setRecords({className}VOList);\n'
        content += f'        return {className}VOPage;\n'
        content += '    }\n'
        content += '\n'
        content += f'    // 对外提供获取 {className}VO 的方法\n'
        content += f'    public {className}VO showVO(Long id) {{\n'
        content += f'        {className} {className} = show(id);\n'
        content += f'        return baseDAO.convertToVO({className}, {className}VO.class);\n'
        content += '    }\n'
        content += '\n'
        content += f'    // 对外提供保存 {className}VO 的方法\n'
        content += f'    public {className}VO storeVO({className}VO model) {{\n'
        content += f'        // 将 {className}VO 转换为 {className}\n'
        content += f'        {className} {className} = baseDAO.convertToVO(model, {className}.class);\n'
        content += f'        // 保存 {className}\n'
        content += f'        {className} saved = null;\n'
        content += '\n'
        content += '        if (model.getId() == null) {\n'
        content += f'            saved = store({className});\n'
        content += '        }\n'
        content += '        else{\n'
        content += f'            update({className});\n'
        content += f'            saved = {className};\n'
        content += '        }\n'
        content += '\n'
        content += f'        // 将保存后的 {className} 转换回 {className}VO\n'
        content += f'        return baseDAO.convertToVO(saved, {className}VO.class);\n'
        content += '    }\n'
        content += '}\n'
        content += '\n'


        self._generate_file_with_dir(content, instanceName, fileName, force=True)

    def create_controller(self, table_info_list):
        
        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的类名称
            instanceName = CreateUtil.instance_name(tableName)

            path = self.package_path + "/"
            FileUtil.check_path(path)
            filePath = path + instanceName + "/" + className + "Controller.java"

            if FileUtil.path_exists(filePath):
                Log.info("文件已存在！")
            else:
                self.create_empty_control(tableInfo)

    def create_empty_control(self, tableInfo):
        
        # 表名称
        tableName = tableInfo["name"]

        # 对应的类名称
        className = CreateUtil.camelize(tableName)

        # 对应的类名称
        instanceName = CreateUtil.instance_name(tableName)
        
        content = ""
        fileName = className + "Controller.java"

        content += f"package {self.package_name}.{instanceName};\n"
        content += '\n'
        content += 'import com.common.base.BaseController;\n'
        content += 'import org.springframework.web.bind.annotation.RequestMapping;\n'
        content += 'import org.springframework.web.bind.annotation.RestController;\n'
        content += '\n'
        content += f'@RequestMapping("/{instanceName}")\n'
        content += '@RestController\n'
        content += f'public class {className}Controller extends BaseController<{className}Service, {className}, {className}VO> {{\n'
        content += '\n'
        content += '    @Override\n'
        content += f'    protected {className}VO convertToVO({className} model) {{\n'
        content += f'        return baseService.baseDAO.convertToVO(model, {className}VO.class);\n'
        content += '    }\n'
        content += '\n'
        content += '    @Override\n'
        content += f'    protected {className} convertToModel({className}VO vo) {{\n'
        content += f'        return baseService.baseDAO.convertToVO(vo, {className}.class);\n'
        content += '    }\n'
        content += '}\n'
        content += '\n'

        self._generate_file_with_dir(content, instanceName, fileName, force=True)

    def create_dao(self, table_info_list):
        
        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的类名称
            instanceName = CreateUtil.instance_name(tableName)

            path = self.package_path + "/"
            FileUtil.check_path(path)
            filePath = path + instanceName + "/" +className + "Dao.java"

            if FileUtil.path_exists(filePath):
                Log.info("文件已存在！")
            else:
                self.create_empty_dao(tableInfo)

    def create_empty_dao(self, tableInfo):
        
        # 表名称
        tableName = tableInfo["name"]

        # 对应的类名称
        className = CreateUtil.camelize(tableName)

        # 对应的类名称
        instanceName = CreateUtil.instance_name(tableName)
        
        content = ""
        fileName = className + "Dao.java"

        content += f'package {self.package_name}.{instanceName};\n'
        content += '\n'
        content += 'import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;\n'
        content += 'import com.baomidou.mybatisplus.core.metadata.IPage;\n'
        content += 'import com.baomidou.mybatisplus.extension.plugins.pagination.Page;\n'
        content += 'import org.springframework.stereotype.Component;\n'
        content += '\n'
        content += 'import com.common.base.BaseDAO;\n'
        content += '\n'
        content += '@Component\n'
        content += f'public class {className}Dao extends BaseDAO<{className}Mapper, {className}> {{\n'
        content += '\n'
        content += f'    public IPage<{className}> getByPageByCreate(int page, int size) {{\n'
        content += f'        Page<{className}> pages = new Page<>(page, size);\n'
        content += f'        return baseMapper.selectPage(pages, new QueryWrapper<{className}>()\n'
        content += f'                .orderByDesc("create_at"));\n'
        content += '    }\n'
        content += '}\n'
        content += '\n'

        self._generate_file_with_dir(content, instanceName, fileName, force=True)

    def create_empty_vo(self, tableInfo):
        pass


    def create_mapper1(self, tableInfo):

        for tableInfo in tableInfo:
            # 表名称
            tableName = tableInfo["name"]

            # 产生的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的实例名称
            instanceName = CreateUtil.instance_name(tableName)

            filepath = self.package_path + "mapper/" + className + "Mapper.java"

            # if file_manager.checkFilePath(filepath):

            string = "package " + self.package_name + ".mapper;\r\n"
            string += "import org.apache.ibatis.annotations.*;\r\n\r\n"
            string += "import java.util.List;\r\n"
            string += "import com.qlzw.smartwc.dao." + className + ";\r\n\r\n"
            string += "import com.qlzw.smartwc.Mapper." + className + "Mapper;\r\n"
            string += "import com.qlzw.smartwc.Provider." + className + "Provider;\r\n"

            string += "import org.springframework.stereotype.Component;\r\n\r\n"
            string += "@Component(value = \"" + className + "Mapper\")\r\n"
            string += "@Mapper\r\n"
            string += "public interface " + className + "Mapper {\r\n\r\n"
            string += "    //### 自动生成 ###\r\n"
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
            string += "    //### 自动生成 ###\r\n"
            string += "}"

            Log.success("Mapper", "生成："+filepath)
            f = open(filepath, mode='w+')
            f.write(string)
            f.close()

    def create_model1(self, table_info_list):
        """
        @summary: 创建model实体类
        @param tableInfos: 表信息
        """
        
        Log.blank()
        Log.info("java", "================ 创建model实体类 ================")

        parseMap = {
            "REAL": "Long.valueOf",
            'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Integer.valueOf",
            'BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Long.valueOf",
            "INT": "Integer.valueOf",
            "TINYINT": "Integer.valueOf",
            "SMALLINT": "Integer.valueOf",
            "MEDIUMINT": "Long.valueOf",
            "BIGINT": "Long.valueOf",
            "FLOAT": "Float.valueOf",
            "DOUBLE": "Double.valueOf",
            "CHAR": "",
            "VARCHAR": "",
            "TINYTEXT": "",
            "TEXT": "",
            "MEDIUMTEXT": "",
            "LONGTEXT": "",
            "BOOL": "Boolean.valueOf",
            "BOOLEAN": "Boolean.valueOf",
            "DATETIME": "Timestamp.valueOf",
            "DATE": "Timestamp.valueOf",
            "TIME": "Timestamp.valueOf",
            "TIMESTAMP": "Timestamp.valueOf",
        }

        coulumTypeTemp = {
            "REAL": "Long",
            'INT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Integer",
            'BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY': "Long",
            "INT": "Integer",
            "TINYINT": "Integer",
            "SMALLINT": "Integer",
            "MEDIUMINT": "Long",
            "BIGINT": "Long",
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

        for tableInfo in table_info_list:
            # 表名称
            tableName = tableInfo["name"]

            if (tableName in self.modelIgnore) == True:
                Log.warn(f"!!! table_name: {tableName} modelIgnore 中，所以忽略")
                continue
            
            # 产生的类名称
            className = CreateUtil.camelize(tableName)
            
            # 字段属性列表
            columns = copy.deepcopy(tableInfo["columns"])
            
            # 文件信息
            string = self.split_string+ "\r\n"
            string += "package " + self.package_name + ".dao;\r\n\r\n"
            string += 'import java.util.Map;\r\n'
            string += 'import java.sql.Timestamp;\r\n'
            string += '\r\n'
            string += 'import jakarta.persistence.Column;\r\n'
            string += 'import jakarta.persistence.Entity;\r\n'
            string += 'import jakarta.persistence.GeneratedValue;\r\n'
            string += 'import jakarta.persistence.GenerationType;\r\n'
            string += 'import jakarta.persistence.EntityListeners;\r\n'
            string += 'import jakarta.persistence.Id;\r\n'
            string += 'import jakarta.persistence.Table;\r\n'
            string += '\r\n'
            string += 'import org.springframework.data.annotation.CreatedDate;\r\n'
            string += 'import org.springframework.data.annotation.LastModifiedDate;\r\n'
            string += 'import org.springframework.data.jpa.domain.support.AuditingEntityListener;\r\n'
            string += '\r\n'
            string += 'import lombok.Data;\r\n'
            string += 'import lombok.NoArgsConstructor;\r\n'
            string += 'import lombok.ToString;\r\n'
            string += 'import lombok.AllArgsConstructor;\r\n'
            string += '\r\n'
            string += '@Data\r\n'
            string += '@Entity\r\n'
            string += '@Table(name = "{}")\r\n'.format(tableName)
            string += '\r\n'
            string += '@ToString\r\n'
            string += '@NoArgsConstructor\r\n'
            string += '@AllArgsConstructor\r\n'
            string += '@EntityListeners(AuditingEntityListener.class) // 监听实体变更\r\n'
            string += "public class " + className + " {\r\n\r\n"
            
            prop_string = ""
            json_string = "    public void fromMap(Map<String, Object> map) {\r\n"

            for columnInfo in columns:

                # 字段名称
                propertyName = columnInfo["name"]

                # 字段描述
                des = columnInfo["des"]

                # 字段类型
                columType = columnInfo["columnProperty"].split('(')[0]
                columType = columType.split(' ')[0]
                columType = columType.strip()
                columType = columType.upper()
                dataType = coulumTypeTemp[columType]
                instPropertyName = CreateUtil.instance_name(propertyName)
                if propertyName == "id":
                    dataType = "Long"
                    prop_string += "    @Id\r\n"

                    if (tableName in self.modelIgnoreAutoId) == False:
                        prop_string += "    @GeneratedValue(strategy = GenerationType.IDENTITY)\r\n"

                if propertyName == "create_at":
                    prop_string += '\r\n    @CreatedDate\r\n'
                    prop_string += '    @Column(name="create_at", updatable=false)\r\n'

                if propertyName == "update_at":
                    prop_string += '\r\n    @LastModifiedDate\r\n'
                    prop_string += '    @Column(name="update_at")\r\n'

                if dataType == "":
                    prop_string += '@JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")'

                prop_string += "    private {0} {1}; //{2} \r\n".format(
                    dataType, instPropertyName, des)

                json_string += "        if (map.get(\"" +     instPropertyName + "\") != null) {\r\n"
                if propertyName == "id":
                    json_string += "            " + instPropertyName + " = " +     parseMap["REAL"] +     "(map.get(\"" + instPropertyName + "\").toString());\r\n"
                else:
                    if columType in "CHAR,VARCHAR,TINYTEXT,TEXT,MEDIUMTEXT,LONGTEXT":
                        json_string += "            " + instPropertyName + " = " +     parseMap[columType] +     "map.get(\"" + instPropertyName + "\").toString();\r\n"
                    else:
                        json_string += "            " + instPropertyName + " = " +     parseMap[columType] +     "(map.get(\"" + instPropertyName + "\").toString());\r\n"
                json_string += "        }\r\n\r\n"

            prop_string +="\r\n"

            json_string = json_string[0:len(json_string)-2]
            json_string += "    }\r\n"

            string += prop_string + json_string
            string += "}\r\n"
            string += self.split_string + "\r\n"

            # 生成文件
            self._generate_file_with_dir(string, "dao", className + ".java", force=True)

    # 生成文件或替换文件内容
    def _generate_file_with_dir(self, changeContent, dirName, fileName="", force=False):

        # 检查文件路径
        fileDir = self.package_path + dirName + "/"
        FileUtil.check_path(fileDir)
        filePath = fileDir + fileName
        
        # 创建文件
        if FileUtil.path_exists(filePath) and force == False:
            content = FileUtil.read_file(filePath)
            content = "".join(content)
            content = content.split(self.split_string)

            if len(content) != 3:
                content = changeContent
            else:
                content[1] = changeContent
                # content[2] = "\r\n" + content[2]
                content = (self.split_string).join(content)
        else:
            content = changeContent

        Log.info("JavaCreator", "生成："+filePath)
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
                string = "package " + self.package_name + ".service;\r\n\r\n"
                string += "\r\n"
                string += "import java.util.HashMap;\r\n"
                string += "import org.springframework.stereotype.Service;\r\n"
                string += "\r\n"
                string += "import com.common.utils.*;\r\n"
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
                string = "package " + self.package_name + ".service;\r\n\r\n"
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
                string += "import com.blog.zz.utils.*;\r\n"
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
                string = "package " + self.package_name + ".service;\r\n\r\n"
                string += "\r\n"
                string += "import org.apache.ibatis.annotations.*;\r\n"
                string += "\r\n"
                string += "import java.util.HashMap;\r\n"
                string += "import org.springframework.stereotype.Component;\r\n"
                string += "import " + self.package_name + ".service.LoginService;\r\n"
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