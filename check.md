/// d 创建数据库
/// d 创建数据表
///   创建数据种子
DbCreator
    /// d -db xxx 数据库创建
    /// d -table xxx,xxx 数据表创建
    ///   -seed xxx,xxx 数据种子创建
    /// -all 创建所有
    def create(info, mode, names)

    /// d 创建数据库
    def create_db(self, dbNameList)

    /// d 创建数据表
    ///   根据内容更新数据表
    def create_or_update_table(self, info, names)

    ///   创建数据种子
    def create_seed(self, info, names)

/// d 根据tablelist 生成对应文件
/// d 生成项目的登录相关文件
/// 生成项目启动文件和其他uitl文件
/// 生成其他的类库文件
JavaCreator
    javaTempPath = os.getcwd()+"/dist/java/"
    packagePath = ""
    packageName = ""

    /// d java model,mapper,provider,service,controller xxx,xxx 根据名称来生成
    /// d java -all 生成所有
    ///   java -util 生成util
    ///   java -d xxx,xxx 生成所有
    def create(talbeInfo, mode, names)

    /// d 根据tableinfo列表，生成对应的文件
    /// d 能够只对该生成的部分修改，不会动其他的
    def createModel(self, tableInfoList)

    /// d 根据tableinfo列表，生成对应的文件
    /// d 能够只对该生成的部分修改，不会动其他的
    def createMapper(self, tableInfoList)

    /// d 根据tableinfo列表，生成对应的文件
    /// d 能够只对该生成的部分修改，不会动其他的
    def createProvider(self, tableInfoList)

    /// d 根据tableinfo列表，生成对应的文件
    /// d 能够只对该生成的部分修改，不会动其他的
    def createService(self, tableInfoList)

    /// d 根据tableinfo列表，生成对应的文件
    /// d 能够只对该生成的部分修改，不会动其他的
    def createController(self, tableInfoList)

    ///  根据tableinfo列表，生成对应的文件
    ///  能够只对该生成的部分修改，不会动其他的
    def createUtil(self)

    ///  根据tableinfo列表，生成对应的文件
    ///  能够只对该生成的部分修改，不会动其他的
    def clearDir(self)

/// 生成对应的page router request文件
/// 
AmdinCreator:
    
    /// admin xxx,xxx 生成对应的page router request文件
    create:

    /// d 根据tableinfo列表，生成对应的page, mixin文件
    /// d mixin能够只对该生成的部分修改，不会动其他的
    createPage:

    /// d 根据tableinfo列表，生成对应的page, mixin文件
    /// d mixin能够只对该生成的部分修改，不会动其他的
    createRouters:

    /// d 根据tableinfo列表，生成对应的page, mixin文件
    /// d mixin能够只对该生成的部分修改，不会动其他的
    createApis:

    /// d 根据tableinfo列表，生成对应的page, mixin文件
    /// d mixin能够只对该生成的部分修改，不会动其他的
    createRequests: