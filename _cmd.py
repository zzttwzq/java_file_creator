import sys
import os
from Core.fileparser import *
from Core.file_manager import *
from Core.mysql import MySqlConn

# colum_type_list = [
#     'TINYINT', 'SMALLINT', 'MEDIUMINT', 'INT', 'BIGINT',
#     'FLOAT', 'DOUBLE', 'DOUBLE PRECISION', 'REAL', 'DECIMAL',
#     'BIT', 'SERIAL', 'BOOL', 'BOOLEAN', 'DEC',
#     'FIXED', 'NUMERIC', 'CHAR', 'VARCHAR', 'TINYTEXT',
#     'TEXT', 'MEDIUMTEXT', 'LONGTEXT', 'TINYBLOB', 'MEDIUMBLOB',
#     'BLOB', 'LONGBLOB', 'BINARY', 'VARBINARY', 'ENUM',
#     'SET', 'DATE', 'DATETIME', 'TIMESTAMP', 'TIME',
#     'YEAR', 'GEOMETRY', 'POINT', 'LINESTRING', 'POLYGON',
#     'MULTIPOINT', 'MULTILINESTRING', 'MULTIPOLYGON', 'GEOMETRYCOLLECTION']

class cmds:

    def check_folder(self) :

        logPath = os.getcwd()+"/Log/"
        if not os.path.exists(logPath):
            os.makedirs(logPath)

        dirs = ["controller","model","mapper","provider","repository"]
        files = []

        for name in dirs :
            filepath = os.getcwd()+"/dist/"+name+"/"
            if not os.path.exists(filepath):
                os.makedirs(filepath)

    def init_tables(self):
        c = iniParser("tableinfo.ini")
        sections = c.getAllSections()
        for name in sections:
            lists = c.getAllKeys(name)
            lists.insert(0, ('id', 'INT NOT NULL AUTO_INCREMENT PRIMARY KEY . 记录ID'))
            lists.append(('create_at', 'DATETIME . 创建于'))
            lists.append(('update_at', 'DATETIME . 更新于'))
            lists.append(('delete_at', 'DATETIME. 删除于'))

            desc = ''
            cloums = ''
            for item in lists:

                key = item[0]
                arr = item[1].split('.')
                info = arr[0]
                des = arr[1]

                cloums = cloums + "`{0}` {1} COMMENT '{2}',".format(key, info, des)

            cloums = cloums[0:len(cloums)-1]
            intsert1 = "CREATE TABLE {0} ({1}) ENGINE=InnoDB DEFAULT CHARSET='utf8';".format(
                name, cloums)

            Log.info('开始插入表:'+name)
            SqlLog.record(intsert1, '创建表:'+name)

            mysql = MySqlConn()
            mysql.execSql(intsert1)
            mysql.dispose()
    
    def clear_dir(self) :

        dirs = ["controller","model","mapper","provider","repository"]
        files = []

        for name in dirs :
            filepath = os.getcwd()+"/dist/"+name+"/"
            fs = os.listdir(filepath)

            for f in fs :
                files.append(filepath+f)

        for f in files :
            if f.find(".DS_Store") < 0 :
                Log.info("删除文件："+f)
                os.remove(f)


    def create_controllers(self, path_name) :

        c = iniParser("tableinfo.ini")
        sections = c.getAllSections()

        Log.info("","")
        Log.info("controller","============= 生成 java controller ================")

        for table_name in sections:

            model_name = table_name.capitalize()

            filepath = os.getcwd()+"/dist/controller/" + model_name + "Controller.java"
            Log.info("controller","开始生成："+filepath)
            f = open(filepath, mode='w+')

            string = "package " + path_name + ".controller;\r\n\r\n"
            string += "import " + path_name + ".model." + model_name + ";\r\n\r\n"
            string += "import " + path_name + ".mapper." + model_name + "Mapper;\r\n"
            string += "import " + path_name + ".repository." + model_name + "Repository;\r\n"

            string += "import " + path_name + ".utils.Pager;\r\n"
            string += "import " + path_name + ".utils.RESPONSE_STATUS;\r\n"
            string += "import " + path_name + ".utils.ResponseStatusGennerator;\r\n"

            string += "import org.springframework.beans.factory.annotation.Autowired;\r\n"
            string += "import org.springframework.validation.annotation.Validated;\r\n"
            string += "import org.springframework.web.bind.annotation.*;\r\n\r\n"
            string += "import java.util.*;\r\n"
            string += "@RequestMapping(\"/" + table_name + "\")\r\n\r\n"
            string += "@RestController\r\n"
            string += "public class " + model_name + "Controller {\r\n\r\n"
            string += "    @Autowired\r\n"
            string += "    private " + model_name + "Mapper " + table_name + "Mapper; \r\n\r\n"
            string += "    @Autowired\r\n"
            string += "    private " + model_name + "Repository " + table_name + "Repository; \r\n\r\n"
            string += "    @Autowired\r\n"
            string += "    private ResponseStatusGennerator responseStatus; \r\n\r\n"
            string += "    // 获取列表\r\n"
            string += "    @GetMapping\r\n"
            string += "    public HashMap<String, Object> list(Pager page,@Validated " + model_name + " " + table_name + ") {\r\n"
            string += "        \r\n"
            string += "        List<" + model_name + "> list = " + table_name + "Mapper.list(page.getPage(),page.getSize());\r\n"
            string += "        \r\n"
            string += "        HashMap<String, Object> map = new HashMap<>();\r\n"
            string += "        map.put(\"code\", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));\r\n"
            string += "        map.put(\"msg\", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));\r\n"
            string += "        map.put(\"data\", list);\r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "    // 删除\r\n"
            string += "    @GetMapping(\"/delete/{id}\")\r\n"
            string += "    public HashMap<String, Object> delete(@PathVariable(\"id\") Long id) {\r\n"
            string += "        \r\n"
            string += "        " + table_name + "Mapper.delete(id);\r\n"
            string += "        \r\n"
            string += "        HashMap<String, Object> map = new HashMap<>();\r\n"
            string += "        map.put(\"code\", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));\r\n"
            string += "        map.put(\"msg\", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));\r\n"
            string += "        map.put(\"data\", null);\r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "    // 查看详情\r\n"
            string += "    @GetMapping(\"/{id}\")\r\n"
            string += "    public HashMap<String, Object> show(@PathVariable(\"id\") Long id) {\r\n"
            string += "        \r\n"
            string += "        " + model_name + " " + table_name + " = " + table_name + "Mapper.show(id);\r\n"
            string += "        \r\n"
            string += "        HashMap<String, Object> map = new HashMap<>();\r\n"
            string += "        map.put(\"code\", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));\r\n"
            string += "        map.put(\"msg\", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));\r\n"
            string += "        map.put(\"data\", " + table_name + ");\r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "    // 插入，保存\r\n"
            string += "    @PostMapping\r\n"
            string += "    public HashMap<String, Object> store(@Validated " + model_name + " " + table_name + ") {\r\n"
            string += "        \r\n"
            string += "        Long id = " + table_name + ".getId() != null ? " + table_name + ".getId() : 0;\r\n"
            string += "        \r\n"
            string += "        if (id > 0) {\r\n"
            string += "        \r\n"
            string += "            " + table_name + "Mapper.update(" + table_name + ");\r\n"
            string += "        } else {\r\n"
            string += "        \r\n"
            string += "            " + table_name + "Mapper.insert(" + table_name + ");\r\n"
            string += "        }\r\n"
            string += "        \r\n"
            string += "        HashMap<String, Object> map = new HashMap<>();\r\n"
            string += "        map.put(\"code\", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));\r\n"
            string += "        map.put(\"msg\", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));\r\n"
            string += "        map.put(\"data\", " + table_name + ");\r\n"
            string += "        return map;\r\n"
            string += "    }\r\n\r\n"
            string += "}\r\n\r\n"

            f.write(string)
            f.close()

    def create_repositories(self,path_name) : 

        c = iniParser("tableinfo.ini")
        sections = c.getAllSections()

        Log.info("","")
        Log.info("repository","============= 生成 java repositories ================")

        for table_name in sections:

            model_name = table_name.capitalize()

            filepath = os.getcwd()+"/dist/repository/" + model_name + "Repository.java"
            Log.info("repository","开始生成："+filepath)
            f = open(filepath, mode='w+')

            string = "package " + path_name + ".repository;\r\n\r\n"
            string += "import " + path_name + ".model." + model_name + ";\r\n"
            string += "import org.springframework.data.jpa.repository.JpaRepository;\r\n"
            string += "import org.springframework.stereotype.Repository;\r\n\r\n"
            string += "@Repository\r\n"
            string += "public interface " + model_name + "Repository extends JpaRepository <" + model_name + ",Long>  {}\r\n\r\n"

            f.write(string)
            f.close()

    def create_mappers(self, path_name) : 
        
        c = iniParser("tableinfo.ini")
        sections = c.getAllSections()

        Log.info("","")
        Log.info("  mapper  ","============= 生成 java mappers ================")

        for table_name in sections:

            model_name = table_name.capitalize()

            filepath = os.getcwd()+"/dist/mapper/" + model_name + "Mapper.java"
            Log.info("  mapper  ","开始生成："+filepath)
            f = open(filepath, mode='w+')

            string = "package " + path_name + ".mapper;\r\n\r\n"
            string += "import " + path_name + ".model." + model_name + ";\r\n"
            string += "import " + path_name + ".provider." + model_name + "Provider;\r\n"

            string += "import org.apache.ibatis.annotations.*;\r\n"
            string += "import java.util.List;\r\n"
            string += "import org.springframework.stereotype.Component;\r\n\r\n"
            string += "@Component(value = \"" + table_name + "Mapper\")\r\n"
            string += "@Mapper\r\n"
            string += "public interface " + model_name + "Mapper {\r\n\r\n"
            string += "    @SelectProvider(type = " + model_name + "Provider.class,method = \"selectAll\")\r\n"
            string += "    public List<" + model_name + "> list(@Param(\"page\") Integer page,@Param(\"size\") Integer size);\r\n\r\n"
            string += "    @SelectProvider(type = " + model_name + "Provider.class,method = \"selectOne\")\r\n"
            string += "    public " + model_name + " show(@Param(\"id\") Long id);\r\n\r\n"
            string += "    @InsertProvider(type = " + model_name + "Provider.class,method = \"insertOne\")\r\n"
            string += "    @Options(useGeneratedKeys = true,keyProperty = \"id\",keyColumn = \"id\")//加入该注解可以保持对象后，查看对象插入id\r\n"
            string += "    public Boolean insert(" + model_name + " " + table_name + ");\r\n\r\n"
            string += "    @DeleteProvider(type = " + model_name + "Provider.class,method = \"deleteOne\")\r\n"
            string += "    public Boolean delete(@Param(\"id\") Long id);\r\n\r\n"
            string += "    @UpdateProvider(type = " + model_name + "Provider.class,method = \"updateOne\")\r\n"
            string += "    public Boolean update(" + model_name + " " + table_name + ");\r\n\r\n"
            string += "}"

            f.write(string)
            f.close()

    def create_provider(self, path_name) :

        c = iniParser("tableinfo.ini")
        sections = c.getAllSections()

        Log.info("","")
        Log.info(" provider ","============= 生成 java providers ================")

        for table_name in sections:

            lists = c.getAllKeys(table_name)
            lists.insert(0, ('id', 'INT. 记录ID'))
            lists.append(('create_at', 'INT. 创建于'))
            lists.append(('update_at', 'INT. 更新于'))
            lists.append(('delete_at', 'INT. 删除于'))

            model_name = table_name.capitalize()

            filepath = os.getcwd() + "/dist/provider/" + model_name + "Provider.java"
            Log.info(" provider ","开始生成："+filepath)
            f = open(filepath, mode='w+')

            string = "package " + path_name + ".provider;\r\n\r\n"
            string += "import " + path_name + ".utils.Pager;\r\n"
            string += "import " + path_name + ".model." + model_name + ";\r\n"
            string += "import java.util.Map;\r\n\r\n"
            string += "public class " + model_name + "Provider {\r\n\r\n"

            if_string = ""
            insert_string = "        String key = \"\";\r\n        String value = \"\";\r\n"
            update_string = "        String sql = \"\";\r\n"
            colum_string = ""

            for item in lists:

                key = item[0]
                arr = item[1].split('.')
                info = arr[0]
                des = arr[1]

                colum_type = info.split('.')[0]
                colum_type = colum_type.split('(')[0]
                colum_type = colum_type.strip()
                colum_type = colum_type.upper()

                if (key == 'id' or
                    colum_type == 'REAL'):

                    if_string = "        if (" + table_name + ".get" +  key.capitalize() +  "() != null && " + table_name + ".get" +  key.capitalize() +  "() > 0) {\r\n"

                elif (colum_type == 'TINYINT' or
                    colum_type == 'SMALLINT' or
                    colum_type == 'MEDIUMINT' or
                    colum_type == 'INT' or
                    colum_type == 'BIGINT' or
                    colum_type == 'TIMESTAMP'):

                    if_string = "        if (" + table_name + ".get" +  key.capitalize() +  "() != null && " + table_name + ".get" +  key.capitalize() +  "() > 0) {\r\n"

                elif (colum_type == 'CHAR' or
                    colum_type == 'VARCHAR' or
                    colum_type == 'TINYTEXT' or
                    colum_type == 'TEXT' or
                    colum_type == 'MEDIUMTEXT' or
                    colum_type == 'LONGTEXT'):

                    if_string = "        if (" + table_name + ".get" +  key.capitalize() +  "() != null && !" + table_name + ".get" +  key.capitalize() +  "().isEmpty()) {\r\n"

                elif (colum_type == 'FLOAT'):

                    if_string = "        if (" + table_name + ".get" +  key.capitalize() +  "() != null && " + table_name + ".get" +  key.capitalize() +  "() > 0) {\r\n"

                elif (colum_type == 'DOUBLE'):

                    if_string = "        if (" + table_name + ".get" +  key.capitalize() +  "() != null && " + table_name + ".get" +  key.capitalize() +  "() > 0) {\r\n"

                elif (colum_type == 'BOOLEAN'):

                    if_string = "        if (" + table_name + ".get" +  key.capitalize() +  "() != null && " + table_name + ".get" +  key.capitalize() +  "() == true) {\r\n"

                elif (colum_type == 'DATETIME' or
                    colum_type == 'DATE' or
                    colum_type == 'TIME'):

                    if_string = "        if (" + table_name + ".get" +  key.capitalize() +  "() != null && " + table_name + ".get" +  key.capitalize() +  "() > 0) {\r\n"

                else:
                    print(item)
                    pass

                colum_string += key + ","

                insert_string += if_string
                insert_string += "           key += \"" +  key + ",\";\r\n"
                insert_string += "           value += \"#{" +  key + "},\";\r\n"
                insert_string += "        }\r\n\r\n"

                update_string += if_string
                update_string += "           sql += \"" +  key + " = #{" +  key + "},\";\r\n"
                update_string += "        }\r\n\r\n"

            colum_string = colum_string[0:len(colum_string)-1]

            string += "    public String selectAll(Map<String, Object> parm) {\r\n\r\n"
            string += "        return \"select " + colum_string + " from " + table_name + " limit #{page},#{size}\";\r\n"
            string += "    }\r\n\r\n"
            string += "    public String selectOne() {\r\n\r\n"
            string += "        return \"select " + colum_string + " from " + table_name + " where " + table_name + ".id=#{id}\";\r\n"
            string += "    }\r\n\r\n"
            string += "    public String deleteOne() {\r\n\r\n"
            string += "        return \"delete from " + table_name + " where id = #{id}\";\r\n"
            string += "    }\r\n\r\n"
            string += "    public String insertOne(" + model_name + " " + table_name + ") {\r\n\r\n"
            string += insert_string
            string += "        key = key.substring(0,key.length()-1);\r\n"
            string += "        value = value.substring(0,value.length()-1);\r\n\r\n"
            string += "        return \"insert into " + table_name + " (\" + key + \") values (\" + value + \")\";\r\n"
            string += "    }\r\n\r\n"
            string += "    public String updateOne(" + model_name + " " + table_name + ") {\r\n\r\n"
            string += update_string
            string += "        sql = sql.substring(0,sql.length()-1);\r\n\r\n"
            string += "        return \"update " + table_name + " set \" + sql + \" where id = #{id}\";\r\n"
            string += "    }\r\n"
            string += "}\r\n"

            f.write(string)
            f.close()

    def create_model(self, path_name):

        c = iniParser("tableinfo.ini")
        sections = c.getAllSections()

        Log.info("","")
        Log.info("  model   ","============= 生成 java models ================")

        for table_name in sections:

            lists = c.getAllKeys(table_name)
            lists.insert(0, ('id', 'INT. 记录ID'))
            lists.append(('create_at', 'INT. 创建于'))
            lists.append(('update_at', 'INT. 更新于'))
            lists.append(('delete_at', 'INT. 删除于'))

            model_name = table_name.capitalize()

            filepath = os.getcwd() + "/dist/model/" + model_name + ".java"
            Log.info("  model   ","开始生成："+filepath)
            f = open(filepath, mode='w+')

            string = "package " + path_name + ".model;\r\n\r\n"
            string += "import javax.persistence.Entity;\r\n"
            string += "import javax.persistence.GeneratedValue;\r\n"
            string += "import javax.persistence.GenerationType;\r\n"
            string += "import javax.persistence.Id;\r\n"
            string += "import java.util.Date;\r\n\r\n"
            string += "@Entity\r\n"
            string += "public class " + model_name + " {\r\n\r\n"

            prop_string = ""
            get_string = ""
            set_string = ""
            const_string = "\r\n    public " + model_name + "("
            const_string2 = ""
            const_string3 = "    public " + model_name + "() {}\r\n\r\n"
            tostring_string = "    public String toString() {\r\n\r\n        return \" <" + model_name + "> {"

            count = 0
            for item in lists:

                key = item[0]
                arr = item[1].split('.')
                info = arr[0]
                des = arr[1]

                colum_type = info.split('.')[0]
                colum_type = colum_type.split('(')[0]
                colum_type = colum_type.strip()
                colum_type = colum_type.upper()

                if (key == 'id' or
                    colum_type == 'REAL'):

                    prop_string += "    private Long " + key + "; //" + des + " \r\n"
                    const_string += "Long " + key + ","
                    get_string += "    public Long get" + key.capitalize() + " () { return this." + key + ";}\r\n\r\n"
                    set_string += "    public void set" + key.capitalize() + " (Long " + key + ") { this." + key + " = " + key + ";}\r\n\r\n"

                    if count == 0 :
                        tostring_string += key + " = \" + " + key + " + \" \" +\r\n"
                    else :
                        tostring_string += "                \"" + key + " = \" + " + key + " + \" \" +\r\n"

                elif (colum_type == 'TINYINT' or
                    colum_type == 'SMALLINT' or
                    colum_type == 'MEDIUMINT' or
                    colum_type == 'INT' or
                    colum_type == 'BIGINT'):

                    prop_string += "    private Integer " + key + "; //" + des + " \r\n"
                    const_string += "Integer " + key + ","
                    get_string += "    public Integer get" +  key.capitalize() +  " () { return this." + key + ";}\r\n\r\n"
                    set_string += "    public void set" + key.capitalize() + " (Integer " + key + ") { this." + key + " = " + key + ";}\r\n\r\n"

                    tostring_string += "                \"" + key + " = \" + " + key + " + \" \" +\r\n"

                elif (colum_type == 'CHAR' or
                    colum_type == 'VARCHAR' or
                    colum_type == 'TINYTEXT' or
                    colum_type == 'TEXT' or
                    colum_type == 'MEDIUMTEXT' or
                    colum_type == 'LONGTEXT'):

                    prop_string += "    private String " + key + "; //" + des + " \r\n"
                    const_string += "String " + key + ","
                    get_string += "    public String get" + key.capitalize() + " () { return this." + key + ";}\r\n\r\n"
                    set_string += "    public void set" + key.capitalize() + " (String " + key + ") { this." + key + " = " + key + ";}\r\n\r\n"

                    tostring_string += "                \"" + key + " = '\" + " + key + " + \"' \" +\r\n"
                    
                elif (colum_type == 'FLOAT'):

                    prop_string += "    private Float " + key + "; //" + des + " \r\n"
                    const_string += "Float " + key + ","
                    get_string += "    public Float get" + key.capitalize() + " () { return this." + key + ";}\r\n\r\n"
                    set_string += "public void set" + key.capitalize() + " (Float " + key + ") { this." + key + " = " + key + ";}\r\n\r\n"

                    tostring_string += "                \"" + key + " = \" + " + key + " + \" \" +\r\n"

                elif (colum_type == 'DOUBLE'):

                    prop_string += "    private Double " + key + "; //" + des + " \r\n"
                    const_string += "Double " + key + ","
                    get_string += "    public Double get" + key.capitalize() + " () { return this." + key + ";}\r\n\r\n"
                    set_string += "    public void set" + key.capitalize() + " (Double " + key + ") { this." + key + " = " + key + ";}\r\n\r\n"

                    tostring_string += "                \"" + key + " = \" + " + key + " + \" \" +\r\n"

                elif (colum_type == 'BOOLEAN'):

                    prop_string += "    private Boolean " + key + "; //" + des + " \r\n"
                    const_string += "Boolean " + key + ","
                    get_string += "    public Boolean get" + key.capitalize() + " () { return this." + key + ";}\r\n\r\n"
                    set_string += "    public void set" + key.capitalize() + " (Boolean " + key + ") { this." + key + " = " + key + ";}\r\n\r\n"

                    tostring_string += "                \"" + key + " = \" + " + key + " + \" \" +\r\n"

                elif (colum_type == 'DATETIME' or
                    colum_type == 'DATE' or
                    colum_type == 'TIME' or
                    colum_type == 'TIMESTAMP'):

                    prop_string += "    private Integer " + key + "; //" + des + " \r\n"
                    const_string += "Integer " + key + ","
                    get_string += "    public Integer get" +  key.capitalize() +  " () { return this." + key + ";}\r\n\r\n"
                    set_string += "    public void set" + key.capitalize() + " (Integer " + key + ") { this." + key + " = " + key + ";}\r\n\r\n"

                    tostring_string += "                \"" + key + " = \" + " + key + " + \", \" +\r\n"

                else:
                    print(item)
                    pass
                
                const_string2 += "        this." + key + "=" + key + ";\r\n"

                count = count + 1

            const_string = const_string[0:len(const_string)-1]
            const_string += ") {\r\n"
            const_string = const_string + const_string2 + "    }\r\n\r\n"

            tostring_string = tostring_string[0:len(tostring_string)-2]
            tostring_string = ""+tostring_string
            tostring_string += " \"}\";\r\n    }"

            prop_string = "    @Id\r\n    @GeneratedValue(strategy = GenerationType.IDENTITY)\r\n" + prop_string

            string += prop_string + const_string + const_string3 + get_string + set_string + tostring_string + "\r\n}"

            f.write(string)
            f.close()

    def init_db(self):
        pass

try:
    c = cmds()
    c.check_folder()

    cmd = sys.argv[1]
    path = ""
    if len(sys.argv) > 2 :
        path = sys.argv[2]

    if cmd == "all_file" :

        if len(path) > 0 :
            c.create_controllers(path)
            c.create_repositories(path)
            c.create_mappers(path)
            c.create_provider(path)
            c.create_model(path)
        else :
            Log.error("错误","未指定路径！")

    elif cmd == "controller" :
        if len(path) > 0 :
            c.create_controllers(path)
        else :
            Log.error("错误","未指定路径！")

    elif cmd == "repository" :
        if len(path) > 0 :
            c.create_repositories(path)
        else :
            Log.error("错误","未指定路径！")

    elif cmd == "mapper" :
        if len(path) > 0 :
            c.create_mappers(path)
        else :
            Log.error("错误","未指定路径！")

    elif cmd == "provider" :
        if len(path) > 0 :
            c.create_provider(path)
        else :
            Log.error("错误","未指定路径！")

    elif cmd == "model" :
        if len(path) > 0 :
            c.create_model(path)
        else :
            Log.error("错误","未指定路径！")

    elif cmd == "table" :
        c.init_tables()

    elif cmd == "clear" :
        c.clear_dir()

    if cmd == "" :
        pass

except Exception as e:
    Log.error("System",str(e))