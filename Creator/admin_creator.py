import copy

import os
from Core.file_manager import *
from Core.table_util import *
import shutil

class AdminCreator:
    dirs = ["pages", "backUp"]
    logPath = os.getcwd()+"/Log/"
    pathPrefix = os.getcwd()+"/dist/admin/"

    destinationDir = ""
    routerPath = ""
    apiPath = ""

    @staticmethod
    def create(talbeInfo, mode, names):

        adminCreator = AdminCreator()

        # ------------ 准备路径信息
        adminCreator.routerPath = talbeInfo["appPath"] + \
            "admin/src/router/local.js"
        adminCreator.apiPath = talbeInfo["appPath"] + "admin/src/api/"
        adminCreator.destinationDir = talbeInfo["appPath"] + "admin/src/pages/"
        adminCreator.pathPrefix = talbeInfo["appPath"] + "admin/src/"
        # 检查源目录文件夹是否可用,不可用则不创建，担心直接替换文件的风险
        if not os.path.exists(adminCreator.destinationDir):
            Log.error("java_create", "源目录不存在，请指定源目录")
            return 0

        # 创建 文件夹
        TableUtil.createFolder(adminCreator.logPath,
                               adminCreator.pathPrefix, adminCreator.dirs)

        # ------------ 备份文件
        zip_name = shutil.make_archive(
            adminCreator.destinationDir, f'zip', adminCreator.destinationDir)
        print(zip_name)  # 返回文件的最终路径
        zip_name1 = zip_name
        zip_name = zip_name.split(".")
        zip_name2 = "pagesBack_{0}.".format(time.strftime(
            "%Y-%m-%d_%H:%M:%S", time.localtime())).join(zip_name)
        os.rename(zip_name1, zip_name2)
        shutil.move(zip_name2, "dist/admin/backUp")

        # ------------ 执行操作
        tableList = TableUtil.getTableInfoWidthNames(talbeInfo, names)
        Log.blank()
        Log.info(
            "admin_create", "================ 正在为`{0}`生成admin文件 ================".format(names))

        if mode == "-d":

            adminCreator.clearDir()
        elif mode == "-all":

            # 创建 page
            adminCreator.createPage(tableList)

            # 创建 router
            adminCreator.createRouter(tableList)

            # 创建 api
            adminCreator.createApi(tableList)

            # 创建 request
            adminCreator.createRequest(tableList)
        elif mode == "-page":

            # 创建 page
            adminCreator.createPage(tableList)
        elif mode == "-router":

            # 创建 router
            adminCreator.createRouter(tableList)
        elif mode == "-api":

            # 创建 api
            adminCreator.createApi(tableList)
        elif mode == "-request":

            # 创建 request
            adminCreator.createRequest(tableList)
        else:

            AdminCreator.cmdError()

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

    def createPage(self, tableInfos):
        Log.blank()
        Log.info("admin", "生成 admin pages")

        for tableInfo in tableInfos:

            # 表名称
            tableName = tableInfo["name"]

            # 表标题
            tableTitle = tableInfo['title']

            # 表描述
            classDes = tableInfo["des"]

            # 对应的类名称
            className = TableUtil.className(tableName)

            # 字段属性列表
            columnLists = tableInfo["columns"]
            columnLists2 = copy.deepcopy(columnLists)

            # 添加时间信息
            TableUtil.addModelDefaultProperty(columnLists2)

            columns = ""
            searchs = ""
            forms = ""
            content = ""

            for columnInfo in columnLists2:
                # ---------- table columns ----------
                columnDes = columnInfo['des']
                columnName = TableUtil.instanceName(columnInfo['name'])

                # if columnName == "createAt" or columnName == "updateAt" or columnName == "deleteAt":
                #     continue

                columns += "        {\r\n"
                columns += "          title: '{0}',//{1}\r\n".format(
                    columnDes, columnDes)
                columns += "          dataIndex: '{0}',\r\n".format(columnName)
                columns += "          key: '{0}',\r\n".format(columnName)
                keys = columnInfo.keys()

                propKeys = ""
                if "sort" in keys:
                    propKeys += "          sort: '{0}',\r\n".format(
                        columnInfo["sort"])

                if "align" in keys:
                    propKeys += "          align: '{0}',\r\n".format(
                        columnInfo["align"])

                if "width" in keys:
                    propKeys += "          width: {0},\r\n".format(
                        columnInfo["width"])

                if "fixed" in keys:
                    propKeys += "          fixed: '{0}',\r\n".format(
                        columnInfo["fixed"])

                if "precision" in keys:
                    propKeys += "          precision: {0},\r\n".format(
                        columnInfo["precision"])

                if "showTime" in keys:
                    if columnInfo["showTime"] == 1:
                        a = "true"
                    else:
                        a = "false"
                    propKeys += "          showTime: {0},\r\n".format(a)

                columns += propKeys
                columns += "        },\r\n"

                # ---------- searchs forms ----------
                formType = columnInfo['formType']
                showInSearch = columnInfo['showInSearch']
                required = str(columnInfo['required'])

                item = "        {\r\n"
                item += "          name: '{0}', //{1} \r\n".format(
                    columnName, columnDes)
                item += "          type: '{0}', // text, number, numberRange, select, date, datetime, dateRange\r\n".format(
                    formType)
                item += "          decorator: [\r\n"
                item += "            '{0}',\r\n".format(columnName)
                item += "            {\r\n"
                item += "              rules: [\r\n"
                item += "                { required: " + required + \
                    ", message: '" + columnDes + " 为必填项' },\r\n"
                if formType == 'text':
                    if "limit" in keys:
                        limit = columnInfo['limit'].split("-")
                        li1 = limit[0]
                        if len(limit) > 1:
                            li2 = limit[1]
                        else:
                            li2 = ''

                        item += "                { min: " + li1 + \
                            ", message: '内容必须大于{1}个字符' },\r\n".format(li1)
                        item += "                { max: " + li2 + \
                            ", message: '内容不超过{1}个字符' },\r\n".format(li2)

                item += "              ],\r\n"
                item += "            },\r\n"
                item += "          ],\r\n"
                if formType == 'number':
                    item += "          precision: 0,\r\n"

                if formType == 'select':

                    option_string = ''
                    for value3 in columnInfo['options']:
                        option_string += "            {\r\n"
                        option_string += "              'label': '{0}',\r\n".format(
                            value3['label'])
                        option_string += "              'value': {1}\r\n".format(
                            value3['value'])
                        option_string += "            },\r\n"

                    item += "          options: [\r\n"
                    item += option_string
                    item += "          ],\r\n"

                item += propKeys
                item += "        },\r\n"

                if columnName != "id" and columnName != "createAt" and columnName != "updateAt" and columnName != "deleteAt":
                    forms += item

                # search
                if showInSearch == 1:
                    item = item.replace(
                        '{ required: true', '{ required: false')
                    if columnName != "id" and columnName != "createAt" and columnName != "updateAt" and columnName != "deleteAt":
                        searchs += item

            content += "<template>\r\n"
            content += "  <div>\r\n"
            content += "    <FastTable\r\n"
            content += "      title=\"{0}\"\r\n".format(tableTitle)
            content += "      :columns=\"columns\"\r\n"
            content += "      :searchList=\"searchList\"\r\n"
            content += "      :formList=\"formList\"\r\n"
            content += "      :listRequest=\"listRequest\"\r\n"
            content += "      :addRequest=\"addRequest\"\r\n"
            content += "      :editRequest=\"editRequest\"\r\n"
            content += "      :editDetailRequest=\"editDetailRequest\"\r\n"
            content += "      :deleteRequest=\"deleteRequest\"\r\n"
            content += "      :handelListData=\"handelListData\"\r\n"
            content += "      :handelModifyData=\"handelModifyData\"\r\n"
            content += "      :handelWillAdd=\"handelWillAdd\"\r\n"
            content += "      :handelWillEdit=\"handelWillEdit\"\r\n"
            content += "      pageNumKey=\"page\"\r\n"
            content += "      pageSizeKey=\"size\"\r\n"
            content += "      :pageStart=\"0\"\r\n"
            content += "      >\r\n"
            content += "    </FastTable>\r\n"
            content += "  </div>\r\n"
            content += "</template>\r\n"
            content += "\r\n"
            content += "<script>\r\n"
            content += 'import { ' + 'get{0}, post{1}, get{2}ByID, delete{3}ByID'.format(
                className, className, className, className) + ' } from \"@/api/request\" \r\n'
            content += "\r\n"
            content += "export default {\r\n"
            content += "  name: '{0}Page', // {1} {2} \r\n ".format(
                className, tableTitle, classDes)
            content += "  data() {\r\n"
            content += "    return {\r\n"
            content += "      /// table\r\n"
            content += "      columns: [\r\n"
            content += "{0}\r\n".format(columns)
            content += "        {\r\n"
            content += "          title: '操作',\r\n"
            content += "          scopedSlots: {\r\n"
            content += "            customRender: 'action',\r\n"
            content += "          },\r\n"
            content += "        },\r\n"
            content += "      ],\r\n"
            content += "\r\n"
            content += "      /// 搜索内容\r\n"
            content += "      searchList: [\r\n"
            content += searchs
            content += "      ],\r\n"
            content += "\r\n"
            content += "      /// 表单信息列表\r\n"
            content += "      formList: [\r\n"
            content += forms
            content += "      ],\r\n"
            content += "\r\n"
            content += "      listRequest: get{0},\r\n".format(className)
            content += "      addRequest: post{0},\r\n".format(className)
            content += "      editRequest: post{0},\r\n".format(className)
            content += "      editDetailRequest: get{0}ByID,\r\n".format(
                className)
            content += "      deleteRequest: delete{0}ByID,\r\n".format(
                className)
            content += "    };\r\n"
            content += "  },\r\n"
            content += "  created() {},\r\n"
            content += "  methods: {\r\n"
            content += "    handelListData(data) {\r\n"
            content += "      data.map((it) => {\r\n"
            content += "        // console.log(it)\r\n"
            content += "      })\r\n"
            content += "    },\r\n"
            content += "    handelModifyData(values) {},\r\n"
            content += "    handelWillAdd(values) {},\r\n"
            content += "    handelWillEdit(values) {},\r\n"
            content += "  },\r\n"
            content += "};\r\n"
            content += "</script>\r\n"
            content += "\r\n"
            content += "<style lang='less' scoped>\r\n"
            content += "</style>\r\n"
            content += "\r\n"

            dirPath = "{0}pages/{1}/".format(self.pathPrefix, className)
            filepath = "{0}index.vue".format(dirPath, className)

            if not os.path.exists(dirPath):
                os.makedirs(dirPath)

            Log.info("page", "开始生成："+filepath)
            f = open(filepath, mode='w+')
            f.write(content)
            f.close()

    def createRouter(self, tableInfos):
        Log.blank()
        Log.info("admin", "生成 admin routers")

        f = open(self.routerPath)
        c = f.read()
        f.close()
        c = ''.join(c)

        content = c.split("//### 自动生成的Router")

        string = ''
        for tableInfo in tableInfos:
            # 表名称
            tableName = tableInfo["name"]

            # 表标题
            tableTitle = tableInfo['title']

            # 表描述
            classDes = tableInfo["des"]

            # 对应的类名称
            className = TableUtil.className(tableName)

            # 对应的实例名称
            instanceName = TableUtil.instanceName(tableName)

            tableKeys = tableInfo.keys()

            string += "            {\r\n"
            string += "                path: \"/{0}\",\r\n".format(
                instanceName)
            string += "                name: \"{0}\",\r\n".format(tableTitle)
            string += "                des: \"{0}\",\r\n".format(classDes)
            string += "                meta: {\r\n"
            if "icon" in tableKeys:
                string += "                    icon: \"{0}\"\r\n".format(
                    tableInfo["icon"])
            else:
                string += "                    icon: \"user\"\r\n"
            string += "                },\r\n"
            string += "                component: () => import (\"@/pages/{0}/\"),\r\n".format(
                className)
            string += "            },\r\n"

            Log.info("router", "开始生成："+instanceName)

        content[1] = "\r\n" + string + "            "
        content = "//### 自动生成的Router".join(content)

        f = open(self.routerPath, encoding='utf-8', mode="w+")
        f.write(content)
        f.close()

    def createApi(self, tableInfos):
        Log.blank()
        Log.info("admin", "生成 admin api")

        f = open(self.apiPath + "api.js")
        c = f.read()
        f.close()
        c = ''.join(c)

        content = c.split("//### 自动生成的Apis")
        info = TableUtil.getConfigInfo()
        appName = info["appName"]

        string = ''
        for tableInfo in tableInfos:
            # 表名称
            tableName = tableInfo["name"]

            # 表标题
            tableTitle = tableInfo['title']

            # 表描述
            classDes = tableInfo["des"]

            # 常量名称
            constName = tableName.upper()

            # 对应的实例名称
            instanceName = TableUtil.instanceName(tableName)

            string += "\r\n    // {0} \r\n".format(tableTitle)
            string += "    {0}: `$".format(constName) + '{BASE_URL}' + \
                "/{0}/{1}`, // {2} \r\n".format(appName,
                                                instanceName, classDes)
            Log.info("router", "开始生成："+instanceName)

        content[1] = "\r\n" + string + "\r\n    "
        content = "//### 自动生成的Apis".join(content)

        f = open(self.apiPath + "api.js", encoding='utf-8', mode="w+")
        f.write(content)
        f.close()

    def createRequest(self, tableInfos):
        Log.blank()
        Log.info("admin", "生成 admin request")

        f = open(self.apiPath + "request.js")
        c = f.read()
        f.close()
        c = ''.join(c)

        content = c.split("//### 自动生成的Api")
        requests = ""
        apis = ""
        for tableInfo in tableInfos:
            # 表名称
            tableName = tableInfo["name"]

            # 表标题
            tableTitle = tableInfo['title']

            # 表描述
            classDes = tableInfo["des"]

            # 对应的类名称
            className = TableUtil.className(tableName)

            # 常量名称
            constName = tableName.upper()

            # 字段属性列表
            columnLists = tableInfo["columns"]
            columnLists2 = copy.deepcopy(columnLists)

            # 添加时间信息
            TableUtil.addModelDefaultProperty(columnLists2)

            columnNames = ""
            for columnInfo in columnLists:
                # ---------- table columns ----------
                columnDes = columnInfo['des']
                columnName = columnInfo['name']

                columnNames += "    {0} : {1}\r\n".format(
                    columnName, columnDes)

            apis += "\r\n    {0}, // {1}".format(constName, classDes)

            requests += "\r\n\r\n//************************ {0}\r\n".format(
                tableTitle)

            requests += "/**\r\n"
            requests += " * 获取{0}列表\r\n".format(tableTitle)
            requests += " \r\n"
            requests += "* @returns { "
            requests += "\r\n" + columnNames
            requests += "  }\r\n"
            requests += " */\r\n"
            requests += "export async function get" + \
                className + "(params) {\r\n"
            requests += "    return request(" + constName + \
                ", METHOD.GET, params ? params : {}, null)\r\n"
            requests += "}\r\n\r\n"

            requests += "/**\r\n"
            requests += " * 添加或修改{0}\r\n".format(tableTitle)
            requests += " \r\n"
            requests += " */\r\n"
            requests += "export async function post" + \
                className + "(params) {\r\n"
            requests += "    return request(" + constName + \
                ", METHOD.POST, params ? params : { }, null)\r\n"
            requests += "}\r\n\r\n"

            requests += "/**\r\n"
            requests += " * 获取{0}对应的详情\r\n".format(tableTitle)
            requests += " * @param id 详情id \r\n"
            requests += " \r\n"
            requests += "* @returns { "
            requests += "\r\n" + columnNames
            requests += "  }\r\n"
            requests += " */\r\n"
            requests += "export async function get" + \
                className + "ByID(id) {\r\n"
            requests += "    return request(" + constName + \
                ' + "/" + ' + "id, METHOD.GET, {id : id}, null)\r\n"
            requests += "}\r\n\r\n"

            requests += "/**\r\n"
            requests += " * 删除{0}\r\n".format(tableTitle)
            requests += " * @param id 详情id \r\n"
            requests += " \r\n"
            requests += " */\r\n"
            requests += "export async function delete" + \
                className + "ByID(id) {\r\n"
            requests += "    return request(" + constName + \
                ' + "/delete/" + ' + "id, METHOD.GET, {}, null)\r\n"
            requests += "}\r\n\r\n"

            Log.info("router", "开始生成："+className)

        content[1] = apis + "\r\n    "
        content[3] = requests

        content = "//### 自动生成的Api".join(content)
        f = open(self.apiPath + "request.js", encoding='utf-8', mode="w+")
        f.write(content)
        f.close()

    @staticmethod
    def cmdError():
        Log.info("admin_create", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            admin -all [names] 生成所有内容。\r\n \
            admin -page [names] 生成page文件。\r\n \
            admin -router [names] 生成router路由。\r\n \
            admin -api [names] 生成api信息。\r\n \
            admin -request [names] 生成request文件。\r\n \
        ")
