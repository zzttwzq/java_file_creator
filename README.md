# java_file_creator
快速生成controller,mapper,dao,respository等文件

使用方法:

1. 在tableinfo.ini文件中定义表内容

  [表名] ;注释
  字段名1 : varchar(100)... . 用户名
  ...
  
  [user] ;用户
  name : varchar(100) . 用户名称
  age : int . 用户年龄

2. 进入命令行
      python3 _cmd.py all_file #生成所有文件(controller,pojo,mapper,provider,respository)
      
      python3 _cmd.py controller #生成 controller 文件
      
      python3 _cmd.py repository #生成 repository 文件
      
      python3 _cmd.py mapper #生成 mapper 文件
      
      python3 _cmd.py provider #生成 provider 文件
      
      python3 _cmd.py dao #生成 pojo 文件
      
      python3 _cmd.py table #在数据库中快速生成表
      
      python3 _cmd.py clear #清除生成的文件
 
 文件在dist目录下
 
 
================

pom.xml 依赖配置

		<!--mybatis提供的启动器-->
		<dependency>
			<groupId>org.mybatis.spring.boot</groupId>
			<artifactId>mybatis-spring-boot-starter</artifactId>
			<version>2.1.1</version>
		</dependency>

		<!--druid依赖-->
		<dependency>
			<groupId>com.alibaba</groupId>
			<artifactId>druid</artifactId>
			<version>1.1.9</version>
		</dependency>

		<!-- 数据连接池 -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-jdbc</artifactId>
		</dependency>

		<!-- springboot启动器 -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<!-- mysql连接器 -->
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<scope>runtime</scope>
		</dependency>

		<!-- json库 -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-json</artifactId>
			<scope>compile</scope>
		</dependency>

		<!-- DATA JPA -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-jpa</artifactId>
		</dependency>

		<!-- fast json -->
		<dependency>
			<groupId>com.alibaba</groupId>
			<artifactId>fastjson</artifactId>
			<version>1.2.5</version>
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

================

application.properties 配置

#配置数据源
server.port=7700
spring.datasource.url=jdbc:mysql://localhost:3306/runoob_db?characterEncoding=utf-8&userSSL=false&serverTimezone=GMT%2B8
spring.datasource.username=root
spring.datasource.password=1111

spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
spring.datasource.initialSize=10
spring.datasource.maxActive=20
spring.datasource.minIdle=5

# mybatis 配置
mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
