# java_file_creator
快速生成controller,mapper,dao,respository等文件

使用方法:
1.在tableinfo.ini文件中定义表内容
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
