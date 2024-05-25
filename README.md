# java_file_creator
快速生成 springboot下的java curd文件，admin文件，uniapp文件

## 使用
| 命令头  | 命令1                  | 命令2                                                   | 参数             |
| ------- | ---------------------- | ------------------------------------------------------- | ---------------- |
| python3 | db 生成数据库相关      | -db 生成数据库。                                        | names 数据库名称 |
| python3 |                        | -table 生成数据表。                                     | names 可以指定表 |
| python3 |                        | -seed 生成种子数据。                                    | names 可以指定表 |
|         |                        |                                                         |                  |
| python3 | java(生成java后台内容) | [model,mapper,provider,service,controller] 生成对应内容 | names 可以指定表 |
| python3 |                        | -util 生成util文件                                      | names 可以指定表 |
|         |                        |                                                         |                  |
| python3 | admin 生成后台管理系统 | -all 生成所有内容。                                     | names 可以指定表 |
| python3 |                        | -n 生成对应表的所有内容                                 | names 可以指定表 |

## tableinfo.json文件中定义表内容
```json
{
    "version": "1.0.3",
    "build": "1",
    "name": "blog",
    "title": "博客",
    "logPath": "Log/",
    "path": "/Users/xxx/Documents/GitHub/blog/",
    "db": {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "dbNames": [
            "myblog",
            "test1",
            "test2"
        ],
        "password": "123",
        "charSet": "utf8",
        "tableSchema": {
            "user:用户:myblog": [
                "nick_name:昵称:varchar(20)",
                "phone:手机号:varchar(15)",
                "email:邮箱:varchar(20)",
                "token:凭证:varchar(20)",
                "province:凭证:varchar(10)",
                "city:凭证:varchar(20)",
                "address:凭证:varchar(200)",
                "role_id:角色ID:int",
                "type:角色类型-0_管理用户 1_普通用户:int(2)"
            ],
        },
        "tableSeed": {
            "project_category": [
                "前端",
                "Flutter",
                "Java",
                "Python"
            ]
        },
        "tableList": [
            {
                "name": "user",
                "title": "用户",
                "des": "用户",
                "dbName": "myblog",
                "columns": [
                    {
                        "name": "nick_name",
                        "des": "昵称",
                        "columnProperty": "varchar(20)",
                        "sort": "up",
                        "align": "left",
                        "width": 100,
                        "formType": "text",
                        "showInSearch": 1,
                        "required": 0
                    },
                    {
                        "name": "type",
                        "des": "角色类型",
                        "columnProperty": "varchar(20)",
                        "sort": "up",
                        "align": "left",
                        "width": 100,
                        "formType": "select",
                        "showInSearch": 1,
                        "required": 0
                    },
                    ...
                ]
            },
        ]
    },
    "admin": {
        "port": 7701,
        "backupPath": "/Users/xxx/Documents/GitHub/java_file_creator/Backup/admin/",
        "adminSrcPath": "admin/src/",
        "routerPath": "admin/src/router/local.js",
        "apiPath": "admin/src/api/Api.js",
        "requestPath": "admin/src/api/ApiRequest.js",
        "pagePath": "admin/src/pages/"
    },
    "java": {
        "port": 7700,
        "backupPath": "/Users/xxx/Documents/GitHub/java_file_creator/Backup/java/",
        "packageName": "com.qlzw.smartwc",
        "packagePath": "java/src/main/java/com/qlzw/smartwc/",
        "utilsPath": "java/src/main/java/com/qlzw/smartwc/utils/"
    }
}
```
 
## java 目录中的配置
#### java pom.xml 依赖配置
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.3.0.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.qlzw.smartwc</groupId>
    <artifactId>demo</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>demo</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-properties-migrator</artifactId>
            <scope>runtime</scope>
        </dependency>

        <!--mybatis-->
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-logging</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <!-- netty 通信框架 -->
        <dependency>
            <groupId>io.netty</groupId>
            <artifactId>netty-all</artifactId>
        </dependency>

        <!-- druid依赖 -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.1.9</version>
        </dependency>

        <!-- DATA-JPA -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>

        <!-- fast-json -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.5</version>
        </dependency>

        <!-- spring-boot-starter -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>2.1.2</version>
        </dependency>

        <!-- 测试框架 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>

        <!-- mysql-connect -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <groupId>org.junit.vintage</groupId>
                    <artifactId>junit-vintage-engine</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <fork>true</fork><!--必须添加这个配置-->
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```

#### java application.properties 配置
```
# server
server.port=7777

# datasource
spring.datasource.url=jdbc:mysql://localhost:3306/test1?characterEncoding=utf-8&userSSL=false&serverTimezone=GMT%2B8
spring.datasource.username=root
spring.datasource.password=123
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
spring.datasource.initialSize=10
spring.datasource.maxActive=20
spring.datasource.minIdle=5

# mybatis
mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl

# log4j
logging.file.path=/Users/xxx/Desktop/springboot
```

## admin 目录中的配置
#### admin proxy_table 配置
将 
```
VUE_APP_PROXY=xx # 改成对应的名称
VUE_APP_API_BASE_URL=xxx # 修改成对应的地址即可
```

## uni 目录中的配置
#### 


## 更新内容

#### 1.0.7
1. db_creator
   1. create_seed 功能
   2. schema 添加 tableName, className, instanceName
2. mysql_util 
   1. 重构增删改查方法
3. log_util
   1. 重构log，添加是否显示字段
4. datetime_util
   1. 时间处理工具类

#### 1.0.6
1. java_creator 
   1. 修复登录jwtbug
2. admin_creator
   1. 登录和过期功能
   2. 修复登录bug

#### 1.0.5
1. Core/ 文件夹内容转移到 Utils/ 中
2. db_creator 
   1. 数据库，表明均为下划线，方便阅读
   2. 将_cmd 中的schema 方法移动到 dbcreator；
   3. schema 将字段处理为驼峰，首字母小写形式；
3. java_creator
   1. split_string 改成 // "    // ### 自动生成 ###"
   2. User类自动添加登录代码

#### 1.0.4
1. create_util 工具类方法修改成下划线
2. file_manager 
   1. 工具类名修改为FileManager
   2. 工具类方法修改成下划线
3. mysql 工具类方法名修改为下划线
4. db_creator 
   1. 修改表字段名为驼峰
   2. 数据库名纯大写
   3. 表名下划线
   4. 字段名驼峰首字母小写
5. admin_creator 
   1. 工具类修改方法为下划线
   2. 在 'tableSchema' 的对应字段中加入’#‘号可以关联到其他的表，并将输入内容改成select
   3. 在 'tableSchema' 的对应字段中加入’-‘号可以自动截断并加入到选项，选项内容可以用空格空开
   4. 在 'tableList' 的对应字段中加入'options'字段，可以加入选项
   5. adminPage 中的 'handelxxx' 方法名写错改成 'handel'
6. java_creator
   1. 工具类修改方法为下划线
   2. 修改
7. 

#### 1.0.3
1. 修改 db_creator 调整到稳定
2. 修改 java_creator 调整到稳定
3. 修改 admin_creator 调整到稳定

#### 1.0.2
1. 修复admin page 缺少id，createAt，updateAt，deleteAt，等字段
2. admin page 添加key字段
3. admin page search 屏蔽id，createAt，updateAt，deleteAt，等字段
4. admin page 导入的接口方法调整
5. admin page 添加handelModifyData handelWillAdd handelWillEdit等方法
6. admin request 生成接口方法调整
7. admin 命令调整详见上面表格
8. 修复java mapper 缺少id，createAt，updateAt，deleteAt，等字段
9. java 命令调整详见上面表格
10. 添加db_creator，可以生成数据库和数据表 java 命令调整详见上面表格
11. 添加schema 命令; 根据tableinfo.json 中的 tableSchema 字段信息生成 tableList字段内的内容，规则如下：
    1.  table中 表名^表描述^表详细信息
    2.  column中 字段名^字段描述^数据属性

#### 1.0.2
1. admin_creator 增加和修改去除createAt；搜索列表添加createAt；

#### 1.0.1
1. 指定tableInfo.json 位置，可以多工程工作，修复相关bug

#### 1.0.0 
1. java、admin目录能正常生成内容并正常工作