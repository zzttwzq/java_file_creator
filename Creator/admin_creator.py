import copy
import os
import sys

#添加上级目录
sys.path.append("..//")
from Utils.file_util import FileUtil
from Utils.log_util import Log
from Utils.create_util import CreateUtil

class AdminCreator:
    pagePath = ""
    routerPath = ""
    apiPath = ""
    requestPath = ""
    split_string = "    //### 自动生成 ###"

    @staticmethod
    def create(tableInfo, mode, names):
        adminCreator = AdminCreator()

        # ------------ 准备路径信息
        adminCreator.routerPath = tableInfo["path"] + tableInfo["admin"]["routerPath"]
        adminCreator.apiPath = tableInfo["path"] + tableInfo["admin"]["apiPath"]
        adminCreator.pagePath = tableInfo["path"] + tableInfo["admin"]["pagePath"]
        adminCreator.requestPath = tableInfo["path"] + tableInfo["admin"]["requestPath"]
        # 检查源目录文件夹是否可用,不可用则不创建，担心直接替换文件的风险
        if not FileUtil.path_exists(adminCreator.pagePath):
            Log.error("admin", "源目录不存在，请指定源目录")
            return 0

        Log.blank()
        Log.info(
            "admin", "================ 正在为`{0}`生成admin文件 ================".format(names))

        # 备份目录
        FileUtil.pack_dir(tableInfo["path"] + tableInfo["admin"]["adminSrcPath"], tableInfo["admin"]["backupPath"])

        # ------------ 执行操作
        tableList = CreateUtil.get_tableInfo_width_names(tableInfo, names)

        if len(tableList) == 0:
            Log.error(
                "admin", "字段 `{0}` 不存在".format(names))
            return
        
        if len(names) == 0:
            adminCreator._cmd_error()
        elif mode == "-d":
            adminCreator.clearDir()
        elif mode == "-router":
            adminCreator.clearDir()
        elif mode == "-d":
            adminCreator.clearDir()
        elif mode == "-n" or mode == "-all":
            adminCreator.create_routers(tableList)
            adminCreator.create_apis(tableInfo, tableList)
            adminCreator.create_requests(tableList)
            adminCreator.create_page(tableList)
                    
    def create_page(self, tableInfos):
        Log.blank()
        Log.info("admin", "开始生成 pages")

        for tableInfo in tableInfos:
            # 表名称
            tableName = tableInfo["name"]

            # 表标题
            tableTitle = tableInfo['title']

            # 表描述
            classDes = tableInfo["des"]

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 创建 文件夹
            FileUtil.check_path(self.pagePath + className)

            # 字段属性列表
            columnList = copy.deepcopy(tableInfo["columns"])

            columns = ""
            searchs = ""
            forms = ""
            content = ""
            relateApi = ""
            relateData = ""
            relateMethod = ""
            relateMethod2 = ""
            relateMethodCall = ""

            for columnInfo in columnList:
                # ---------- table columns ----------
                columnDes = columnInfo['des']
                columnName = columnInfo['name']

                columns += "        {\r\n"
                columns += "          title: '{0}',//{1}\r\n".format(
                    columnDes.split("-")[0], columnDes)
                columns += "          dataIndex: '{0}',\r\n".format(columnName)
                columns += "          key: '{0}',\r\n".format(columnName)
                keys = columnInfo.keys()
                
                if "#" in columnDes:
                    relateName = columnDes.split("#")[1]
                    relateClassName = CreateUtil.camelize(relateName)
                    relateInstanceName = CreateUtil.instance_name(relateName)
                    
                    relateApi += "get{0}, \r\n".format(relateClassName)
                    relateData += "      {0}List: [], \r\n".format(relateInstanceName)
                    relateMethodCall += "\r\n      this.get{0}List(); ".format(relateClassName)
                    
                    relateMethod += '    // 获取列表数据\r\n'
                    relateMethod += '    async get{0}List() {1} \r\n'.format(relateClassName, '{')
                    relateMethod += '      let data = await get{0}({1} "page": 0, "size": 100000 {2});\r\n'.format(relateClassName, '{', '}')
                    relateMethod += '      // 转换select options 数据\r\n'
                    relateMethod += '      data = data.map(v => {\r\n'
                    relateMethod += '        return {\r\n'
                    relateMethod += '          "label": v["name"] != undefined ? v["name"] : v["title"],\r\n'
                    relateMethod += '          "value": v["id"],\r\n'
                    relateMethod += '        };\r\n'
                    relateMethod += '      })\r\n'
                    # relateMethod += '      console.log(">>>> {0}List", data); \r\n'.format(relateInstanceName)
                    relateMethod += '      this.{0}List = data; \r\n'.format(relateInstanceName)
                    relateMethod += '      // 给formlist里的`{0}`.options 重新赋值\r\n'.format(columnName)
                    relateMethod += '      this.formList.map(it => {0}\r\n'.format("{")
                    relateMethod += '        if (it["name"] == "{0}") {1}\r\n'.format(columnName, "{")
                    relateMethod += '          it["options"] = this.{0}List;\r\n'.format(relateInstanceName)
                    relateMethod += '        }\r\n'
                    relateMethod += '      });\r\n'
                    relateMethod += '      this.searchList.map(it => {0}\r\n'.format("{")
                    relateMethod += '        if (it["name"] == "{0}") {1}\r\n'.format(columnName, "{")
                    relateMethod += '          it["options"] = this.{0}List;\r\n'.format(relateInstanceName)
                    relateMethod += '        }\r\n'
                    relateMethod += '      });\r\n'
                    relateMethod += '    },\r\n'
                    
                    relateMethod2 += '      data.map(d => {\r\n'
                    relateMethod2 += '        this.{}List.map(t => '.format(relateInstanceName) + '{\r\n'
                    relateMethod2 += '          if (d["{}"] == t.value) '.format(columnName) + '{\r\n'
                    relateMethod2 += '            d["{}"] = t.label;\r\n'.format(columnName)
                    relateMethod2 += '          }\r\n'
                    relateMethod2 += '        })\r\n'
                    relateMethod2 += '      })\r\n'
                    relateMethod2 += '      \r\n'
                    
                    columnDes = columnDes.split("#")[0]
                    columnInfo['formType'] = "select"
                    columnInfo['options'] = []

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

                if columnName != "id" and columnName != "createAt" and columnName != "updateAt" and columnName != "deleteAt":
                    forms += item

                # search
                if showInSearch == 1:
                    item = item.replace(
                        '{ required: true', '{ required: false')
                    if columnName != "id" and columnName != "deleteAt":
                        searchs += item

            content += "<template>\r\n"
            content += "  <div>\r\n"
            content += '    <FastTable\r\n'
            content += '      title="{}"\r\n'.format(classDes)
            content += '      :tableHeaderList="columns"\r\n'
            content += '      :tableSearchList="searchList"\r\n'
            content += '      :tableFormList="formList"\r\n'
            content += '      pageNumKey="page"\r\n'
            content += '      pageSizeKey="size"\r\n'
            content += '      :pageStart="0"\r\n'
            content += '      :useCustomForm="false"\r\n'
            content += '      :tableFormWidth="500"\r\n'
            content += '      :listRequest="listRequest"\r\n'
            content += '      :addRequest="addRequest"\r\n'
            content += '      :editRequest="editRequest"\r\n'
            content += '      :detailRequest="detailRequest"\r\n'
            content += '      :deleteRequest="deleteRequest"\r\n'
            content += '      :showLog="true"\r\n'
            content += '      :handleListRequestParams="handleListRequestParams"\r\n'
            content += '      @onWillSearch="onWillSearch"\r\n'
            content += '      @onWillSearchReqeust="onWillSearchReqeust"\r\n'
            content += '      @onDidSearch="onDidSearch"\r\n'
            content += '      @onWillGetList="onWillGetList"\r\n'
            content += '      @onWillGetListRequest="onWillGetListRequest"\r\n'
            content += '      @onGetListSuccess="onGetListSuccess"\r\n'
            content += '      @onGetListError="onGetListError"\r\n'
            content += '      @onWillAdd="onWillAdd"\r\n'
            content += '      @onAddSuccess="onAddSuccess"\r\n'
            content += '      @onAddError="onAddError"\r\n'
            content += '      @onWillEdit="onWillEdit"\r\n'
            content += '      @onEditSuccess="onEditSuccess"\r\n'
            content += '      @onEditError="onEditError"\r\n'
            content += '      @onWillSaveReqeust="onWillSaveReqeust"\r\n'
            content += '      @onWillDelete="onWillDelete"\r\n'
            content += '      @onWillDeleteReqeust="onWillDeleteReqeust"\r\n'
            content += '      @onDeleteSuccess="onDeleteSuccess"\r\n'
            content += '      @onDeleteError="onDeleteError"\r\n'
            content += '      @onFormPrefixClick="onFormPrefixClick"\r\n'
            content += '      @onFormSuffixClick="onFormSuffixClick"\r\n'
            content += '    >\r\n'
            content += '      <template slot="tableCustomForm">\r\n'
            content += '        <div>\r\n'
            content += '        </div>\r\n'
            content += '      </template>\r\n'
            content += '    </FastTable>\r\n'
            content += "  </div>\r\n"
            content += "</template>\r\n"
            content += "\r\n"
            content += "<script>\r\n"
            content += "// 导入mixin文件\r\n"
            content += 'import mixin from \"./mixin\" \r\n'
            content += "\r\n"
            content += "export default {\r\n"
            content += "  mixins: [mixin],\r\n"
            content += "  name: '{0}Page', // {1} {2} \r\n ".format(
                className, tableTitle, classDes)
            content += "  data() {\r\n"
            content += "    return {}\r\n"
            content += "  },\r\n"
            content += "  created() {\r\n"
            content += "    this.init();\r\n"
            content += "  },\r\n"
            content += "  methods: {},\r\n"
            content += "};\r\n"
            content += "</script>\r\n"
            content += "\r\n"
            content += "<style lang='less' scoped>\r\n"
            content += "</style>\r\n"
            content += "\r\n"
            
            mixin = "import {" + " get{0}, post{1}, get{2}ByID, delete{3}ByID,{4} ".format(
                className, className, className, className, relateApi) + " } from \"@/api/ApiRequest\" \r\n"
            mixin += "\r\n"
            mixin += "export default {\r\n"
            mixin += "  data() {\r\n"
            mixin += "    return {\r\n"
            mixin += "      /// relateList\r\n"
            mixin += "{0}".format(relateData)
            mixin += "\r\n"
            mixin += "      /// table\r\n"
            mixin += "      columns: [\r\n"
            mixin += "{0}\r\n".format(columns)
            mixin += "        {\r\n"
            mixin += "          title: '操作',\r\n"
            mixin += "          scopedSlots: {\r\n"
            mixin += "            customRender: 'action',\r\n"
            mixin += "          },\r\n"
            mixin += "        },\r\n"
            mixin += "      ],\r\n"
            mixin += "\r\n"
            mixin += "      /// 搜索内容\r\n"
            mixin += "      searchList: [\r\n"
            mixin += searchs
            mixin += "      ],\r\n"
            mixin += "\r\n"
            mixin += "      /// 表单信息列表\r\n"
            mixin += "      formList: [\r\n"
            mixin += forms
            mixin += "      ],\r\n"
            mixin += "\r\n"
            mixin += "      listRequest: get{0},\r\n".format(className)
            mixin += "      addRequest: post{0},\r\n".format(className)
            mixin += "      editRequest: post{0},\r\n".format(className)
            mixin += "      detailRequest: get{0}ByID,\r\n".format(
                className)
            mixin += "      deleteRequest: delete{0}ByID,\r\n".format(
                className)
            mixin += "    };\r\n"
            mixin += "  },\r\n"
            mixin += "  methods: {\r\n"
            mixin += "    async init() {"
            mixin += "{0}\r\n".format(relateMethodCall)
            mixin += "    },\r\n"
            mixin += "{0}".format(relateMethod)
            mixin += '    //===================== 处理请求参数\r\n'
            mixin += '    // 列表请求参数\r\n'
            mixin += '    async handleListRequestParams(params) {\r\n'
            mixin += '      this.log("handleListRequestParams", params);\r\n'
            mixin += '      return params;\r\n'
            mixin += '    },\r\n'
            mixin += '    // 新增或者修改保存参数\r\n'
            mixin += '    async handleSaveRequestParams(params) {\r\n'
            mixin += '      this.log("handleSaveRequestParams", params);\r\n'
            mixin += '      return params;\r\n'
            mixin += '    },\r\n'
            mixin += '    // 请求详情接口参数\r\n'
            mixin += '    async handleDetailRequestParams(params) {\r\n'
            mixin += '      this.log("handleDetailRequestParams", params);\r\n'
            mixin += '      return params;\r\n'
            mixin += '    },\r\n'
            mixin += '    // 删除列表参数\r\n'
            mixin += '    async handleDeleteRequestParams(params) {\r\n'
            mixin += '      this.log("handleDeleteRequestParams", params);\r\n'
            mixin += '      return params;\r\n'
            mixin += '    },\r\n'
            mixin += '    // 处理列表返回数据\r\n'
            mixin += '    // async handleListData(data) {\r\n'
            mixin += '    //  this.log("handleListData", data);\r\n'
            mixin += '    //  return data;\r\n'
            mixin += '    // },\r\n'
            mixin += '    //===================== search\r\n'
            mixin += '    // 准备搜索回调\r\n'
            mixin += '    onWillSearch(params) {\r\n'
            mixin += '      this.log("onWillSearch", params);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 准备搜索回调\r\n'
            mixin += '    onWillSearchReqeust(params, pagination) {\r\n'
            mixin += '      this.log("onWillSearchReqeust", params, pagination);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 完成搜索回调\r\n'
            mixin += '    onDidSearch() {\r\n'
            mixin += '      this.log("onDidSearch");\r\n'
            mixin += '    },\r\n'
            mixin += '\r\n'
            mixin += '    //===================== 列表\r\n'
            mixin += '    // 准备调用列表接口\r\n'
            mixin += '    onWillGetList() {\r\n'
            mixin += '      this.log("onWillGetList");\r\n'
            mixin += '    },\r\n'
            mixin += '    // 即将开始请求列表接口\r\n'
            mixin += '    onWillGetListRequest(params) {\r\n'
            mixin += '      this.log("onWillGetListRequest", params);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 列表请求成功\r\n'
            mixin += '    onGetListSuccess(data) {\r\n'
            mixin += relateMethod2
            mixin += '      this.log("onGetListSuccess", data);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 列表请求失败\r\n'
            mixin += '    onGetListError(error) {\r\n'
            mixin += '      this.log("onGetListError", error);\r\n'
            mixin += '    },\r\n'
            mixin += '\r\n'
            mixin += '    //===================== 新增\r\n'
            mixin += '    // 准备新增\r\n'
            mixin += '    onWillAdd() {\r\n'
            mixin += '      this.log("onWillAdd");\r\n'
            mixin += '    },\r\n'
            mixin += '    // 新增成功\r\n'
            mixin += '    onAddSuccess(data) {\r\n'
            mixin += '      this.log("onAddSuccess", data);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 新增失败\r\n'
            mixin += '    onAddError(error) {\r\n'
            mixin += '      this.log("onAddError", error);\r\n'
            mixin += '    },\r\n'
            mixin += '\r\n'
            mixin += '    //===================== 更新\r\n'
            mixin += '    // 准备更新\r\n'
            mixin += '    onWillEdit(data) {\r\n'
            mixin += '      this.log("onWillEdit", data);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 更新成功\r\n'
            mixin += '    onEditSuccess(data) {\r\n'
            mixin += '      this.log("onEditSuccess", data);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 更新失败\r\n'
            mixin += '    onEditError(error) {\r\n'
            mixin += '      this.log("onEditError", error);\r\n'
            mixin += '    },\r\n'
            mixin += '\r\n'
            mixin += '    // 准备调用新增或者修改接口\r\n'
            mixin += '    onWillSaveReqeust(params) {\r\n'
            mixin += '      this.log("onWillSaveReqeust", params);\r\n'
            mixin += '    },\r\n'
            mixin += '\r\n'
            mixin += '    //===================== 删除\r\n'
            mixin += '    // 准备删除\r\n'
            mixin += '    onWillDelete(id) {\r\n'
            mixin += '      this.log("onWillDelete", id);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 即将开始请求删除接口\r\n'
            mixin += '    onWillDeleteReqeust(params) {\r\n'
            mixin += '      this.log("onWillDeleteReqeust", params);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 删除成功\r\n'
            mixin += '    onDeleteSuccess(data) {\r\n'
            mixin += '      this.log("onDeleteSuccess", data);\r\n'
            mixin += '    },\r\n'
            mixin += '    // 删除失败\r\n'
            mixin += '    onDeleteError(error) {\r\n'
            mixin += '      this.log("onDeleteError", error);\r\n'
            mixin += '    },\r\n'
            mixin += '\r\n'
            mixin += '    //===================== 其他\r\n'
            mixin += '    // form表单前缀内容点击\r\n'
            mixin += '    onFormPrefixClick(error) {\r\n'
            mixin += '      this.log("onFormPrefixClick", error);\r\n'
            mixin += '    },\r\n'
            mixin += '    // form表单后缀内容点击\r\n'
            mixin += '    onFormSuffixClick(error) {\r\n'
            mixin += '      this.log("onFormSuffixClick", error);\r\n'
            mixin += '    },\r\n'
            mixin += '    log(title, msg) {\r\n'
            mixin += '      console.log(`[' + className + '->${title}]`, msg ?? "");\r\n'
            mixin += '    }\r\n'
            mixin += "  },\r\n"
            mixin += "};\r\n"
            
            self._generate_file(self.pagePath + className + "/mixin.js", "", mixin)
            self._generate_file(self.pagePath + className + "/index.vue", "", content, override=False)

    def create_routers(self, tableInfos):
        Log.blank()
        Log.info("AdminRouters", "创建 routers")

        string = ''
        for tableInfo in tableInfos:
            # 表名称
            tableName = tableInfo["name"]

            # 表标题
            tableTitle = tableInfo['title']

            # 表描述
            classDes = tableInfo["des"]

            # 对应的类名称
            className = CreateUtil.camelize(tableName)

            # 对应的实例名称
            instance_name = CreateUtil.instance_name(tableName)

            tableKeys = tableInfo.keys()

            string += "            {\r\n"
            string += "                path: \"/{0}\",\r\n".format(
                instance_name)
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

            self._generate_file(self.routerPath, "\r\n" + string, "", log_type=3, log_prefix="router", log_txt="创建："+instance_name)

    def create_apis(self, info, tableInfos):
        Log.blank()
        Log.info("AmdinApi", "创建 api")

        appName = info["name"]

        string = ''
        for tableInfo in tableInfos:
            # 表名称
            tableName = tableInfo["name"]

            # 表描述
            classDes = tableInfo["des"]

            # 常量名称
            constName = tableName.upper()

            # 对应的实例名称
            instance_name = CreateUtil.instance_name(tableName)

            string += "\r\n    // {0} \r\n".format(classDes)
            string += "    {0}: `/$".format(constName) + '{BASE_URL}' + "{}`, \r\n".format(instance_name)
            Log.info("api", "创建："+tableName)

        self._generate_file(self.apiPath, "\r\n" + string, "", log_type=2, log_prefix="AmdinApi", log_txt="创建："+appName)

    def create_requests(self, tableInfos):
        Log.blank()
        Log.info("AmdinRequest", "创建 request")

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
            className = CreateUtil.camelize(tableName)
            
            # 实例名称
            instance_name = CreateUtil.instance_name(tableName)

            # 常量名称
            constName = tableName.upper()
            
            # 登录功能
            addUserLogin = tableName.find("user") > -1 or tableName.find("User") > -1

            # 字段属性列表
            columnLists = tableInfo["columns"]

            columnNames = ""
            for columnInfo in columnLists:
                # ---------- table columns ----------
                columnDes = columnInfo['des']
                columnName = columnInfo['name']

                columnNames += "    {0} : {1}\r\n".format(
                    columnName, columnDes)

            apis += "\r\n    {0}, // {1}".format(constName, classDes)

            requests += "\r\n"
            requests += "\r\n//************************ {0}\r\n".format(
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
                ", METHOD.GET, params ? params : {})\r\n"
            requests += "}\r\n"
            requests += "\r\n"

            requests += "/**\r\n"
            requests += " * 添加或修改{0}\r\n".format(tableTitle)
            requests += " \r\n"
            requests += " */\r\n"
            requests += "export async function post" + \
                className + "(params) {\r\n"
            requests += "    return request(" + constName + \
                ", METHOD.POST, params ? params : { })\r\n"
            requests += "}\r\n"
            requests += "\r\n"

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
                ' + "/" + ' + "id, METHOD.GET, {id : id})\r\n"
            requests += "}\r\n"
            requests += "\r\n"

            requests += "/**\r\n"
            requests += " * 删除{0}\r\n".format(tableTitle)
            requests += " * @param id 详情id \r\n"
            requests += " \r\n"
            requests += " */\r\n"
            requests += "export async function delete" + \
                className + "ByID(id) {\r\n"
            requests += "    return request(" + constName + \
                ' + "/delete/" + ' + "id, METHOD.GET, {})\r\n"
            requests += "}\r\n"
            requests += "\r\n"
            
            if addUserLogin:
                requests += "/**\r\n"
                requests += " * {}登录接口\r\n".format(tableTitle)
                requests += " * @param name 用户名 \r\n"
                requests += " * @param password 密码 \r\n"
                requests += " \r\n"
                requests += " */\r\n"
                requests += "export async function " + instance_name + "Login(name, password) {\r\n"
                requests += '    return request(' + tableName.upper() + ' + "/login", METHOD.POST, {"name": name, "password":password, })\r\n'
                requests += "}\r\n"
                requests += "\r\n"

            Log.info("AmdinRequest", "创建："+className)

        string = 'import { METHOD, request } from "../utils/request.js"\r\n'
        string += 'import {'
        string += apis
        string += '\r\n} from "./Api.js"'
        string += '\r\n'
        string += requests

        self._generate_file(self.requestPath, "", string, log_type=2, log_prefix="request", log_txt="生成："+self.requestPath)

    # 生成文件或替换文件内容
    def _generate_file(self, filePath, replaceString, totalString, override=True, log_type=1, log_prefix="admin", log_txt=""):
        # 检查文件路径
        fileDir = filePath.split("/")
        fileDir[len(fileDir) - 1] = ""
        fileDir = "/".join(fileDir)
        FileUtil.check_path(fileDir)
        
        if FileUtil.path_exists(filePath) :
            f1 = open(filePath, "r")
            content = f1.readlines()
            content = "".join(content)
            content = content.split(self.split_string)
            
            if len(content) != 3:
                content = totalString
            else:
                content[1] = replaceString
                content = (self.split_string+"").join(content)
        else:
            content = totalString
                
        if override or FileUtil.path_exists(filePath) == False:
            # 创建文件
            if log_type == 1:
                Log.info(log_prefix, "生成："+filePath)
            elif log_type == 2:
                Log.success(log_prefix, log_txt)
            elif log_type == 3:
                Log.info(log_prefix, log_txt)
            
            FileUtil.write_file(content=content, file_path=filePath)

    @staticmethod
    def _cmd_error():
        Log.info("admin", "命令错误：\r\n \
            尝试以下命令：、\r\n  \
            admin -all [names] 生成所有内容。\r\n \
            admin -page [names] 生成page文件。\r\n \
            admin -router [names] 生成router路由。\r\n \
            admin -api [names] 生成api信息。\r\n \
            admin -request [names] 生成request文件。\r\n \
        ")
