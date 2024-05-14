import copy

import os
from Core.file_manager import Log
from Core.create_util import CreateUtil

class UniCreator:
    pathPrefix = ""
    pagePath = ""
    routerPath = ""
    apiPath = ""

    @staticmethod
    def create(talbeInfo, mode, names):

        uniCreator = UniCreator()

        # ------------ 准备路径信息
        uniCreator.pathPrefix = talbeInfo["appPath"] + "uni/"
        uniCreator.routerPath = talbeInfo["appPath"] + "uni/pages.json"
        uniCreator.apiPath = talbeInfo["appPath"] + "uni/common/ApiManager/"
        uniCreator.pagePath = talbeInfo["appPath"] + "uni/pages/"

        # 检查源目录文件夹是否可用,不可用则不创建，担心直接替换文件的风险
        if not os.path.exists(uniCreator.routerPath):
            Log.error("uni_creator", "源目录不存在，请指定源目录")
            return 0

        # 备份目录
        CreateUtil.pack_dir(uniCreator.pagePath, "dist/uni/pages/")
        CreateUtil.pack_dir(uniCreator.apiPath, "dist/uni/api/")
        CreateUtil.pack_dir(uniCreator.routerPath, "dist/uni/router/")

        # ------------ 执行操作
        tableList = CreateUtil.get_tableInfo_width_names(talbeInfo, names)
        Log.blank()
        Log.info(
            "UniCreator", "================ 正在为`{0}`生成Uni文件 ================".format(names))

        if mode == "-d":

            uniCreator.clearDir()

        elif len(tableList) == 0:

            Log.error("uni_creator", "生成的数据为空！")

        else:
            if "page" in mode == False:
                UniCreator._cmd_error()

            UniCreator.createApis(uniCreator.apiPath, tableList)
            UniCreator.createRouters(uniCreator.routerPath, tableList)
            UniCreator.createRequests(uniCreator.apiPath, tableList)
            UniCreator.createPages(uniCreator.pagePath, tableList)

    @staticmethod
    def createPages(pagePath, tableInfos):
        Log.blank()
        Log.info("UniPages", "开始生成 pages")

        for tableInfo in tableInfos:

            # 表名称
            tableName = tableInfo["name"]

            # 表标题
            tableTitle = tableInfo['title']

            # 表描述
            classDes = tableInfo["des"]

            # 对应的类名称
            className = CreateUtil.className(tableName)

            # 创建 文件夹
            CreateUtil.check_path(pagePath + className)

            # 字段属性列表
            columnList = copy.deepcopy(tableInfo["columns"])

            # 添加时间信息
            CreateUtil.add_model_default_property(columnList)

            columns = ""
            searchs = ""
            forms = ""
            content = ""

            for columnInfo in columnList:
                # ---------- table columns ----------
                columnDes = columnInfo['des']
                columnName = CreateUtil.instance_name(columnInfo['name'])

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
                item += "          title: '{0}',\r\n".format(columnDes)
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

                if columnName != "id" and columnName != "updateAt" and columnName != "deleteAt":
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
                className, className, className, className) + ' } from \"@/services/request\" \r\n'
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
            content += "        console.log(it)\r\n"
            content += "      })\r\n"
            content += "    },\r\n"
            content += "    handelModifyData(values) {console.log(values);},\r\n"
            content += "    handelWillAdd(values) {console.log(values);},\r\n"
            content += "    handelWillEdit(values) {console.log(values);},\r\n"
            content += "  },\r\n"
            content += "};\r\n"
            content += "</script>\r\n"
            content += "\r\n"
            content += "<style lang='less' scoped>\r\n"
            content += "</style>\r\n"
            content += "\r\n"

            filepath = "{0}{1}/index.vue".format(pagePath, className)

            Log.success("page", "生成："+className)

            f = open(filepath, mode='w+')
            f.write(content)
            f.close()

    @staticmethod
    def createRouters(routerPath, tableInfos):
        Log.blank()
        Log.info("UniRouter", "开始生成 routers")

        f = open(routerPath)
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
            className = CreateUtil.className(tableName)

            # 对应的实例名称
            instance_name = CreateUtil.instance_name(tableName)

            tableKeys = tableInfo.keys()

            string += "        {\r\n"
            string += "            \"path\": \"pages/{0}/index\"\r\n".format(
                className)
            string += "        },\r\n"

            Log.success("router", "生成："+instance_name)

        string = string[0:len(string)-3]
        string += "\r\n"
        content[1] = "\r\n" + string + "        "
        content = "//### 自动生成的Router".join(content)

        f = open(routerPath, encoding='utf-8', mode="w+")
        f.write(content)
        f.close()

    @staticmethod
    def createApis(apiPath, tableInfos):
        Log.blank()
        Log.info("UniApi", "开始生成 Uni api")

        f = open(apiPath + "api.js")
        c = f.read()
        f.close()
        c = ''.join(c)

        content = c.split("//### 自动生成的Apis")
        info = CreateUtil.get_config_info()
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
            instance_name = CreateUtil.instance_name(tableName)

            string += "\r\n    // {0} \r\n".format(tableTitle)
            string += "    {0}: `$".format(constName) + '{BASE_URL}' + \
                "/{0}/{1}`, // {2} \r\n".format(appName,
                                                instance_name, classDes)
            Log.success("api", "生成："+instance_name)

        content[1] = "\r\n" + string + "\r\n    "
        content = "//### 自动生成的Apis".join(content)

        f = open(apiPath + "api.js", encoding='utf-8', mode="w+")
        f.write(content)
        f.close()

    @staticmethod
    def createRequests(apiPath, tableInfos):
        Log.blank()
        Log.info("UniRequest", "开始生成 request")

        f = open(apiPath + "request.js")
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
            className = CreateUtil.className(tableName)

            # 对应的类实例化名称
            instance_name = CreateUtil.instance_name(tableName)

            # 常量名称
            constName = tableName.upper()

            # 字段属性列表
            columnLists = tableInfo["columns"]
            columnLists2 = copy.deepcopy(columnLists)

            # 添加时间信息
            CreateUtil.add_model_default_property(columnLists2)

            columnNames = ""
            paramNames = ""
            for columnInfo in columnLists:
                # ---------- table columns ----------
                columnDes = columnInfo['des']
                columnName = columnInfo['name']

                columnNames += "    {0} : {1}\r\n".format(
                    columnName, columnDes)
                paramNames += "@param {0} {1}\r\n".format(
                    columnName, columnDes)

            apis += "\r\n    {0}, // {1}".format(constName, classDes)

            requests += "\r\n\r\n//************************ {0}\r\n".format(
                tableTitle)

            requests += "/**\r\n"
            requests += " * 获取{0}列表\r\n".format(tableTitle)
            requests += " \r\n"
            requests += "* @returns [{ "
            requests += "\r\n" + columnNames
            requests += "  }]\r\n"
            requests += " */\r\n"
            requests += "export async function get" + \
                className + "(params) {\r\n"
            requests += "    return new Promise((resolve, reject) => {\r\n"
            requests += "        request.{0}(\r\n".format('get')
            requests += "            `{0}/{1}`,\r\n".format(
                "${config.getRequestHost()}", instance_name)
            requests += "            params,\r\n"
            requests += "            success_data => {\r\n"
            requests += "                resolve(success_data);\r\n"
            requests += "            },\r\n"
            requests += "            error => {\r\n"
            requests += "                reject(error);\r\n"
            requests += "            }\r\n"
            requests += "        ); \r\n"
            requests += "    });\r\n"
            requests += "}\r\n\r\n"

            requests += "/**\r\n"
            requests += " * 添加或修改{0}\r\n".format(tableTitle)
            requests += paramNames
            requests += "\r\n */\r\n"
            requests += "export async function post" + \
                className + "(params) {\r\n"
            requests += "    return new Promise((resolve, reject) => {\r\n"
            requests += "        request.{0}(\r\n".format('post')
            requests += "            `{0}/{1}`,\r\n".format(
                "${config.getRequestHost()}", instance_name)
            requests += "            params,\r\n"
            requests += "            success_data => {\r\n"
            requests += "                resolve(success_data);\r\n"
            requests += "            },\r\n"
            requests += "            error => {\r\n"
            requests += "                reject(error);\r\n"
            requests += "            }\r\n"
            requests += "        ); \r\n"
            requests += "    });\r\n"
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
            requests += "    return new Promise((resolve, reject) => {\r\n"
            requests += "        request.{0}(\r\n".format('post')
            requests += "            `{0}/{1}`,\r\n".format(
                "${config.getRequestHost()}", instance_name)
            requests += "            {'id': id},\r\n"
            requests += "            success_data => {\r\n"
            requests += "                resolve(success_data);\r\n"
            requests += "            },\r\n"
            requests += "            error => {\r\n"
            requests += "                reject(error);\r\n"
            requests += "            }\r\n"
            requests += "        ); \r\n"
            requests += "    });\r\n"
            requests += "}\r\n\r\n"

            requests += "/**\r\n"
            requests += " * 删除{0}\r\n".format(tableTitle)
            requests += " * @param id 详情id \r\n"
            requests += " */\r\n"
            requests += "export async function delete" + \
                className + "ByID(id) {\r\n"
            requests += "    return new Promise((resolve, reject) => {\r\n"
            requests += "        request.{0}(\r\n".format('post')
            requests += "            `{0}/{1}`,\r\n".format(
                "${config.getRequestHost()}", instance_name)
            requests += "            {'id': id},\r\n"
            requests += "            success_data => {\r\n"
            requests += "                resolve(success_data);\r\n"
            requests += "            },\r\n"
            requests += "            error => {\r\n"
            requests += "                reject(error);\r\n"
            requests += "            }\r\n"
            requests += "        ); \r\n"
            requests += "    });\r\n"
            requests += "}\r\n\r\n"

            Log.success("request", "生成："+className)

        content[1] = apis + "\r\n    "
        content[3] = requests

        content = "//### 自动生成的Api".join(content)
        f = open(apiPath + "request.js", encoding='utf-8', mode="w+")
        f.write(content)
        f.close()

    @staticmethod
    def _cmd_error():
        Log.info("uni_create", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            uni -page [-all/names] 生成页面\r\n \
        ")
