# java_file_creator
快速生成 springboot下的java curd文件，admin文件，uniapp文件

## 使用
| 命令头  | 命令1                  | 命令2                         | 参数             |
| ------- | ---------------------- | ----------------------------- | ---------------- |
| python3 | admin 生成后台管理系统 | -all 生成所有内容。           | names 可以指定表 |
| python3 |                        | -page 生成page文件。          | names 可以指定表 |
| python3 |                        | -router 生成router路由。      | names 可以指定表 |
| python3 |                        | -api 生成api信息。            | names 可以指定表 |
| python3 |                        | -request 生成request文件。    | names 可以指定表 |
|         |                        |                               |                  |
| python3 | java 生成java后台内容  | -all 生成所有内容。           | names 可以指定表 |
| python3 |                        | -model 生成page文件。         | names 可以指定表 |
| python3 |                        | -mapper 生成router路由。      | names 可以指定表 |
| python3 |                        | -provider 生成api信息。       | names 可以指定表 |
| python3 |                        | -service 生成request文件。    | names 可以指定表 |
| python3 |                        | -controller 生成request文件。 | names 可以指定表 |
| python3 |                        | -util 生成request文件。       | names 可以指定表 |
|         |                        |                               |                  |
| python3 | db 生成数据库相关      | -db 生成数据库。              | names 数据库名称 |
| python3 |                        | -table 生成数据表。           | names 可以指定表 |
| python3 |                        | -seed 生成种子数据。          | names 可以指定表 |
|         |                        |                               |                  |

## tableinfo.json文件中定义表内容
```json
{
	"version": "1.0.1", // app 版本号
    "build": "100", // app build版本号
    "packageName": "com.dd.demo1", // java包名
    "appPath": "/Users/mac/Desktop/java_fast_template/", //app根路径
    "appName": "blog111", // app英文名称，用户api等
    "appNameCN": "博客", // app中文名称，显示在页面上的app名称
	"dbName": "test1", // 数据库名称
    "tableSchema": {
        "learn_category^学习分类^学习分类": [
            "title^标题^varchar(1000)"
        ],
    },
    "tableList": [{ // 表信息
            "name": "test_table1", // 表名称，请使用下划线分隔开
            "title": "我是标题", // 表标题
            "des": "我是描述，描述！！！", // 表描述
            "columns": [{
                    "name": "id", // 字段名称
                    "des": "小程序用户性别", // 字段描述
                    "columnProperty": "int", // 字段属性
                    "sort": "up", // 字段排序，在admin table中会用到
                    "align": "left", // 字段显示位置，在admin table中会用到
                    "width": 100,// 字段显示位置，在admin search中用到
                    "showInSearch": true,// 在admin 搜索栏中是否展示
                    "formType": "number",// 在表单中使用的组件类型
                    "required": true// 是否是必填项
                },
                {
                    "name": "name",
                    "des": "昵称",
                    "columnProperty": "varchar(20)",
                    "sort": "up",
                    "align": "left",
                    "width": 100,
                    "showInSearch": true,
                    "formType": "text",
                    "required": true
                }
            ]
        },
    ],
    "tableSeeds": [{
        "name": "table1",
        "data": [
            {
                "id": 1
            }
        ]
    }]
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
logging.file.path=/Users/wuzhiqiang/Desktop/springboot
```

## admin 目录中的配置
#### admin proxy_table 配置
在 ``` vue.config.js ```中找到
```js
    devServer: {
        port: 8900,
        proxy: {
            '^/blog111': {
                //此处要与 /services/api.js 中的 API_PROXY_PREFIX 值保持一致
                target: process.env.VUE_APP_API_BASE_URL,
                changeOrigin: true,
                logLevel: 'debug',
                pathRewrite: { //重写匹配的字段，如果不需要放在请求路径上，可以重写为""
                    "^/blog111": ""
                }
            }
        }
    },
```
将 ```blog111```改成对应的名称，再修改 ``` .env.xxx ```
```
VUE_APP_API_BASE_URL=xxx /// 修改成对应的地址即可
```

## uni 目录中的配置
#### 



## 更新内容
#### 1.0.2
1. 修复admin page 缺少id，createAt，updateAt，deleteAt，等字段
2. admin page 添加key字段
3. admin page search 屏蔽id，createAt，updateAt，deleteAt，等字段
4. admin page 导入的接口方法调整
5. admin page 添加handelModifyData handelWillAdd handelWillEdit等方法
6. admin request 生成接口方法调整
7. admin 命令调整如下：
   
| 命令头  | 命令1                  | 命令2                      | 参数             |
| ------- | ---------------------- | -------------------------- | ---------------- |
| python3 | admin 生成后台管理系统 | -all 生成所有内容。        | names 可以指定表 |
| python3 |                        | -page 生成page文件。       | names 可以指定表 |
| python3 |                        | -router 生成router路由。   | names 可以指定表 |
| python3 |                        | -api 生成api信息。         | names 可以指定表 |
| python3 |                        | -request 生成request文件。 | names 可以指定表 |

8. 修复java mapper 缺少id，createAt，updateAt，deleteAt，等字段
9. java 命令调整如下：
   
| 命令头  | 命令1                 | 命令2                         | 参数             |
| ------- | --------------------- | ----------------------------- | ---------------- |
| python3 | java 生成java后台内容 | -all 生成所有内容。           | names 可以指定表 |
| python3 |                       | -model 生成page文件。         | names 可以指定表 |
| python3 |                       | -mapper 生成router路由。      | names 可以指定表 |
| python3 |                       | -provider 生成api信息。       | names 可以指定表 |
| python3 |                       | -service 生成request文件。    | names 可以指定表 |
| python3 |                       | -controller 生成request文件。 | names 可以指定表 |
| python3 |                       | -util 生成request文件。       | names 可以指定表 |

10. 添加db_creator，可以生成数据库和数据表 java 命令调整如下：

| 命令头  | 命令1             | 命令2                | 参数             |
| ------- | ----------------- | -------------------- | ---------------- |
| python3 | db 生成数据库相关 | -db 生成数据库。     | names 数据库名称 |
| python3 |                   | -table 生成数据表。  | names 可以指定表 |
| python3 |                   | -seed 生成种子数据。 | names 可以指定表 |

11. 添加schema 命令; 根据tableinfo.json 中的 tableSchema 字段信息生成 tableList字段内的内容，规则如下：
    1.  table中 表名^表描述^表详细信息
    2.  column中 字段名^字段描述^数据属性

#### 1.0.1
1. 指定tableInfo.json 位置，可以多工程工作，修复相关bug

#### 1.0.0 
1. java、admin目录能正常生成内容并正常工作