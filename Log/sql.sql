
#[2020-05-27 17:04:57] 创建表:user
 CREATE TABLE user (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,`name` varchar(100) ,`age` int ,`create_at` DATETIME ,`update_at` DATETIME ,`delete_at` DATETIME) ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:dev
 CREATE TABLE dev (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100)  COMMENT ' 设备名称',`snno` varchar(40) unique  COMMENT ' 设备编号',`position` varchar(2000)  COMMENT ' 设备经纬度',`address` varchar(2000)  COMMENT ' 设备地址',`dev_info_id` int  COMMENT ' 设备信息id',`rfid_id` int  COMMENT ' 关联的rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:dev_update
 CREATE TABLE dev_update (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`snno` varchar(40) unique  COMMENT ' 设备编号',`status` int  COMMENT ' 设备升级状态',`ipaddress` varchar(40)  COMMENT ' 客户端ip',`hrev` varchar(20)  COMMENT ' 硬件版本',`srev` varchar(20)  COMMENT ' 软件版本',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:dev_info
 CREATE TABLE dev_info (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`last_time` datetime  COMMENT ' 最后更新时间',`status` int  COMMENT ' 设备状态',`snno` varchar(40) unique  COMMENT ' 设备编号',`ccid` varchar(50)  COMMENT ' 设备ccid',`rfid` varchar(50)  COMMENT ' 设备rfid',`proportion` varchar(20)  COMMENT ' 液体配比',`temperature` float  COMMENT ' 设备温度',`humidity` int  COMMENT ' 设备湿度',`nh3` float  COMMENT ' 设备氨气值',`dayon` int  COMMENT ' 白天工作时间',`dayoff` int  COMMENT ' 白天停止时间',`nighton` int  COMMENT ' 晚上工作时间',`nightoff` int  COMMENT ' 晚上停止时间',`addwaternum` int  COMMENT ' 总加液次数',`addwatertime` int  COMMENT ' 单次加液时间',`atomizerpwm` int  COMMENT ' 雾化强度',`fanmin` int  COMMENT ' 风扇最小转速',`fanmax` int  COMMENT ' 风扇最大转速',`totaladdwater` float  COMMENT ' 累计加水量',`alarmnumber` varchar(20)  COMMENT ' 错误代码',`rfid_status` varchar(20)  COMMENT ' rfid状态',`hrev` varchar(20)  COMMENT ' 硬件版本',`srev` varchar(20)  COMMENT ' 软件版本',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:email_send
 CREATE TABLE email_send (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`send_user_id` int  COMMENT ' 发送人id',`snno` varchar(100)  COMMENT ' 设备编号',`to_email` varchar(100)  COMMENT ' 发送的邮箱地址',`subject` varchar(200)  COMMENT ' 发送的标题',`message` varchar(2000)  COMMENT ' 发送的内容',`alarmnumber` varchar(200)  COMMENT ' 错误类型',`status` int  COMMENT ' 是否发送',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:rfid
 CREATE TABLE rfid (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`no` varchar(100) unique  COMMENT ' rfid编号',`liquid_time` datetime  COMMENT ' 上次更新液体时间',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:area
 CREATE TABLE area (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(40)  COMMENT ' 区域名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:admin_dev_link
 CREATE TABLE admin_dev_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`admin_user_id` int  COMMENT ' 后台管理用户id',`dev_id` int  COMMENT ' 设备id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:admin_link
 CREATE TABLE admin_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`parent_admin_id` int  COMMENT ' 关联账户id',`area_id` int  COMMENT ' 关联账户区域id',`admin_id` int  COMMENT ' 账户id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:mp_dev_link
 CREATE TABLE mp_dev_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`mp_user_id` int  COMMENT ' 小程序用户id',`dev_id` int  COMMENT ' 设备id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:mp_link
 CREATE TABLE mp_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`parent_admin_id` int  COMMENT ' 关联账户id',`area_id` int  COMMENT ' 关联账户区域id',`mp_id` int  COMMENT ' 小程序账户id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:dev_version
 CREATE TABLE dev_version (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`soft_version` varchar(200)  COMMENT ' 设备软件版本号',`hard_version` varchar(200)  COMMENT ' 设备硬件版本号',`file_path` varchar(200)  COMMENT ' 文件名',`status` tinyint  COMMENT ' 状态',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:mp_user_share
 CREATE TABLE mp_user_share (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`mp_user_id` int  COMMENT ' 分享的用户',`title` varchar(200)  COMMENT ' 内容标题',`data_id` int  COMMENT ' 数据id',`type` tinyint  COMMENT ' 类型 0：首页 1：产品列表 2：产品详情 3：问答 4：公司简介 5：联系我们 6：解决方案',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:province
 CREATE TABLE province (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`code` int  COMMENT ' 对应代码',`name` varchar(200)  COMMENT ' 名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:city
 CREATE TABLE city (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`code` int  COMMENT ' 对应代码',`province_code` int  COMMENT ' 所属省份',`name` varchar(200)  COMMENT ' 名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:section
 CREATE TABLE section (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`code` int  COMMENT ' 对应代码',`city_code` int  COMMENT ' 所属区',`name` varchar(200)  COMMENT ' 名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:sms
 CREATE TABLE sms (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`user_id` int  COMMENT ' 用户信息',`phone` varchar(11)  COMMENT ' 手机号',`type` int  COMMENT ' 短信类型 0-验证码 1-告警',`status` int  COMMENT ' 状态',`code` varchar(200)  COMMENT ' 验证码',`snno` varchar(200)  COMMENT ' 设备号码',`dev_name` varchar(200)  COMMENT ' 设备名称',`alarm` varchar(200)  COMMENT ' 报警信息',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:api
 CREATE TABLE api (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(40)  COMMENT ' api名称',`router` varchar(40)  COMMENT ' api',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:api_link
 CREATE TABLE api_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`user_id` int  COMMENT ' 用户id',`api_id` int  COMMENT ' api id',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:role
 CREATE TABLE role (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(40)  COMMENT ' 角色名称',`edit_admin_user` tinyint  COMMENT ' 是否可以编辑管理后台用户',`edit_mp_user` tinyint  COMMENT ' 是否可以编辑小程序用户',`edit_role` tinyint  COMMENT ' 是否可以编辑用户角色',`edit_area` tinyint  COMMENT ' 是否可以编辑用户区域',`edit_device` tinyint  COMMENT ' 是否可以编辑设备',`edit_rfid` tinyint  COMMENT ' 是否可以编辑rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:admin_user
 CREATE TABLE admin_user (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100) unique  COMMENT ' 后台管理登录用户',`nick_name` varchar(200)  COMMENT ' 后台管理用户名称',`admin_token` varchar(200)  COMMENT ' 后台管理用户token',`api_token` varchar(200)  COMMENT ' api用户token',`email` varchar(200)  COMMENT ' 用户邮箱',`role_id` int  COMMENT ' 用户角色id',`area_id` int  COMMENT ' 用户区域id',`province_code` int  COMMENT ' 对应的省code',`city_code` int  COMMENT ' 对应的城市code',`section_code` int  COMMENT ' 对应的区域code',`is_single` int  COMMENT ' 是否是个体户，如果是个体户，区域将不起作用',`password` varchar(40)  COMMENT ' 密码',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:mp_user
 CREATE TABLE mp_user (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100) unique  COMMENT ' 小程序用户登录名',`nick_name` varchar(200)  COMMENT ' 小程序用户昵称',`token` varchar(200)  COMMENT ' 小程序用户token',`open_id` varchar(200)  COMMENT ' 小程序账号唯一id',`address` varchar(200)  COMMENT ' 小程序用户地址',`city_name` varchar(200)  COMMENT ' 城市名',`mobile` int  COMMENT ' 小程序用户手机号',`cover` varchar(200)  COMMENT ' 小程序用户头像',`share` int  COMMENT ' 小程序用户分享信息',`sex` int  COMMENT ' 小程序用户性别',`email` varchar(200)  COMMENT ' 小程序用户邮箱',`admin_user_id` int  COMMENT ' 关联后台管理用户id',`password` varchar(40)  COMMENT ' 密码',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:dev_repair
 CREATE TABLE dev_repair (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`title` varchar(2000)  COMMENT ' 报修标题',`content` varchar(5000)  COMMENT ' 报修详情',`err_type` tinyint  COMMENT ' 保修类型 0：设备故障 1：设备缺液 2：质量问题 3：其他',`images` varchar(2000)  COMMENT ' 报修图片',`dev_info` varchar(2000)  COMMENT ' 设备信息',`phone` varchar(20)  COMMENT ' 联系电话',`position` varchar(200)  COMMENT ' 经纬度',`address` varchar(1000)  COMMENT ' 地址',`admin_user_id` int  COMMENT ' 关联的用户id',`status` tinyint  COMMENT ' 报修状态 0：等待受理 1：受理中 2：受理完成',`time_out` tinyint  COMMENT ' 是否过期',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:dev_repair_link
 CREATE TABLE dev_repair_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`admin_user_id` int  COMMENT ' 关联的用户id',`repair_id` int  COMMENT ' 关联的维修id',`status` tinyint  COMMENT ' 操作状态',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:45] 创建表:dev_answer
 CREATE TABLE dev_answer (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`title` varchar(2000)  COMMENT ' 问题名称',`cause` varchar(5000)  COMMENT ' 导致问题的可能原因',`tips` varchar(5000)  COMMENT ' 维修详情',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:46] 创建表:dev_update_msg
 CREATE TABLE dev_update_msg (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`snno` varchar(40)  COMMENT ' 设备编号',`msg` varchar(40)  COMMENT ' 设备升级状态',`ipaddress` varchar(40)  COMMENT ' 客户端ip',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:46] 创建表:dev_msg
 CREATE TABLE dev_msg (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`last_time` datetime  COMMENT ' 最后更新时间',`status` int  COMMENT ' 设备状态',`snno` varchar(50)  COMMENT ' 设备snno',`ccid` varchar(50)  COMMENT ' 设备ccid',`rfid` varchar(50)  COMMENT ' 设备rfid',`proportion` varchar(20)  COMMENT ' 液体配比',`temperature` float  COMMENT ' 设备温度',`humidity` int  COMMENT ' 设备湿度',`nh3` float  COMMENT ' 设备氨气值',`dayon` int  COMMENT ' 白天工作时间',`dayoff` int  COMMENT ' 白天停止时间',`nighton` int  COMMENT ' 晚上工作时间',`nightoff` int  COMMENT ' 晚上停止时间',`addwaternum` int  COMMENT ' 总加液次数',`addwatertime` int  COMMENT ' 单次加液时间',`atomizerpwm` int  COMMENT ' 雾化强度',`fanmin` int  COMMENT ' 风扇最小转速',`fanmax` int  COMMENT ' 风扇最大转速',`totaladdwater` float  COMMENT ' 累计加水量',`hrev` varchar(20)  COMMENT ' 硬件版本',`srev` varchar(20)  COMMENT ' 软件版本',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:46] 创建表:dev_cmd
 CREATE TABLE dev_cmd (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`params` varchar(10000)  COMMENT ' 参数',`ischecked` tinyint  COMMENT ' 是否已经收到应答',`isouttime` tinyint  COMMENT ' 是否过期',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:46] 创建表:dev_alarm
 CREATE TABLE dev_alarm (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`alarmnumber` varchar(20)  COMMENT ' 错误代码',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:46] 创建表:dev_action
 CREATE TABLE dev_action (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`proportion` varchar(20)  COMMENT ' 液体配比',`temperature` float  COMMENT ' 设备温度',`humidity` int  COMMENT ' 设备湿度',`nh3` float  COMMENT ' 设备氨气值',`dayon` int  COMMENT ' 白天工作时间',`dayoff` int  COMMENT ' 白天停止时间',`nighton` int  COMMENT ' 晚上工作时间',`nightoff` int  COMMENT ' 晚上停止时间',`addwaternum` int  COMMENT ' 总加液次数',`addwatertime` int  COMMENT ' 单次加液时间',`atomizerpwm` int  COMMENT ' 雾化强度',`fanmin` int  COMMENT ' 风扇最小转速',`fanmax` int  COMMENT ' 风扇最大转速',`addtime` int  COMMENT ' 加液次数',`totaladdwater` float  COMMENT ' 累计加水量',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:46] 创建表:dev_connect
 CREATE TABLE dev_connect (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(20)  COMMENT ' 设备方法',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:46] 创建表:rfid_change
 CREATE TABLE rfid_change (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`newrfid` varchar(50)  COMMENT ' 新的rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:46:46] 创建表:msg_log
 CREATE TABLE msg_log (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`sendto` varchar(20)  COMMENT ' 接受对象',`params` varchar(30000)  COMMENT ' 参数',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:13] 创建表:dev
 CREATE TABLE dev (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100)  COMMENT ' 设备名称',`snno` varchar(40) unique  COMMENT ' 设备编号',`position` varchar(2000)  COMMENT ' 设备经纬度',`address` varchar(2000)  COMMENT ' 设备地址',`dev_info_id` int  COMMENT ' 设备信息id',`rfid_id` int  COMMENT ' 关联的rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev
 CREATE TABLE dev (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100)  COMMENT ' 设备名称',`snno` varchar(40) unique  COMMENT ' 设备编号',`position` varchar(2000)  COMMENT ' 设备经纬度',`address` varchar(2000)  COMMENT ' 设备地址',`dev_info_id` int  COMMENT ' 设备信息id',`rfid_id` int  COMMENT ' 关联的rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_update
 CREATE TABLE dev_update (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`snno` varchar(40) unique  COMMENT ' 设备编号',`status` int  COMMENT ' 设备升级状态',`ipaddress` varchar(40)  COMMENT ' 客户端ip',`hrev` varchar(20)  COMMENT ' 硬件版本',`srev` varchar(20)  COMMENT ' 软件版本',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_info
 CREATE TABLE dev_info (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`last_time` datetime  COMMENT ' 最后更新时间',`status` int  COMMENT ' 设备状态',`snno` varchar(40) unique  COMMENT ' 设备编号',`ccid` varchar(50)  COMMENT ' 设备ccid',`rfid` varchar(50)  COMMENT ' 设备rfid',`proportion` varchar(20)  COMMENT ' 液体配比',`temperature` float  COMMENT ' 设备温度',`humidity` int  COMMENT ' 设备湿度',`nh3` float  COMMENT ' 设备氨气值',`dayon` int  COMMENT ' 白天工作时间',`dayoff` int  COMMENT ' 白天停止时间',`nighton` int  COMMENT ' 晚上工作时间',`nightoff` int  COMMENT ' 晚上停止时间',`addwaternum` int  COMMENT ' 总加液次数',`addwatertime` int  COMMENT ' 单次加液时间',`atomizerpwm` int  COMMENT ' 雾化强度',`fanmin` int  COMMENT ' 风扇最小转速',`fanmax` int  COMMENT ' 风扇最大转速',`totaladdwater` float  COMMENT ' 累计加水量',`alarmnumber` varchar(20)  COMMENT ' 错误代码',`rfid_status` varchar(20)  COMMENT ' rfid状态',`hrev` varchar(20)  COMMENT ' 硬件版本',`srev` varchar(20)  COMMENT ' 软件版本',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:email_send
 CREATE TABLE email_send (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`send_user_id` int  COMMENT ' 发送人id',`snno` varchar(100)  COMMENT ' 设备编号',`to_email` varchar(100)  COMMENT ' 发送的邮箱地址',`subject` varchar(200)  COMMENT ' 发送的标题',`message` varchar(2000)  COMMENT ' 发送的内容',`alarmnumber` varchar(200)  COMMENT ' 错误类型',`status` int  COMMENT ' 是否发送',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:rfid
 CREATE TABLE rfid (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`no` varchar(100) unique  COMMENT ' rfid编号',`liquid_time` datetime  COMMENT ' 上次更新液体时间',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:area
 CREATE TABLE area (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(40)  COMMENT ' 区域名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:admin_dev_link
 CREATE TABLE admin_dev_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`admin_user_id` int  COMMENT ' 后台管理用户id',`dev_id` int  COMMENT ' 设备id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:admin_link
 CREATE TABLE admin_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`parent_admin_id` int  COMMENT ' 关联账户id',`area_id` int  COMMENT ' 关联账户区域id',`admin_id` int  COMMENT ' 账户id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:mp_dev_link
 CREATE TABLE mp_dev_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`mp_user_id` int  COMMENT ' 小程序用户id',`dev_id` int  COMMENT ' 设备id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:mp_link
 CREATE TABLE mp_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`parent_admin_id` int  COMMENT ' 关联账户id',`area_id` int  COMMENT ' 关联账户区域id',`mp_id` int  COMMENT ' 小程序账户id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_version
 CREATE TABLE dev_version (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`soft_version` varchar(200)  COMMENT ' 设备软件版本号',`hard_version` varchar(200)  COMMENT ' 设备硬件版本号',`file_path` varchar(200)  COMMENT ' 文件名',`status` tinyint  COMMENT ' 状态',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:mp_user_share
 CREATE TABLE mp_user_share (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`mp_user_id` int  COMMENT ' 分享的用户',`title` varchar(200)  COMMENT ' 内容标题',`data_id` int  COMMENT ' 数据id',`type` tinyint  COMMENT ' 类型 0：首页 1：产品列表 2：产品详情 3：问答 4：公司简介 5：联系我们 6：解决方案',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:province
 CREATE TABLE province (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`code` int  COMMENT ' 对应代码',`name` varchar(200)  COMMENT ' 名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:city
 CREATE TABLE city (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`code` int  COMMENT ' 对应代码',`province_code` int  COMMENT ' 所属省份',`name` varchar(200)  COMMENT ' 名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:section
 CREATE TABLE section (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`code` int  COMMENT ' 对应代码',`city_code` int  COMMENT ' 所属区',`name` varchar(200)  COMMENT ' 名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:sms
 CREATE TABLE sms (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`user_id` int  COMMENT ' 用户信息',`phone` varchar(11)  COMMENT ' 手机号',`type` int  COMMENT ' 短信类型 0-验证码 1-告警',`status` int  COMMENT ' 状态',`code` varchar(200)  COMMENT ' 验证码',`snno` varchar(200)  COMMENT ' 设备号码',`dev_name` varchar(200)  COMMENT ' 设备名称',`alarm` varchar(200)  COMMENT ' 报警信息',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:api
 CREATE TABLE api (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(40)  COMMENT ' api名称',`router` varchar(40)  COMMENT ' api',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:api_link
 CREATE TABLE api_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`user_id` int  COMMENT ' 用户id',`api_id` int  COMMENT ' api id',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:role
 CREATE TABLE role (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(40)  COMMENT ' 角色名称',`edit_admin_user` tinyint  COMMENT ' 是否可以编辑管理后台用户',`edit_mp_user` tinyint  COMMENT ' 是否可以编辑小程序用户',`edit_role` tinyint  COMMENT ' 是否可以编辑用户角色',`edit_area` tinyint  COMMENT ' 是否可以编辑用户区域',`edit_device` tinyint  COMMENT ' 是否可以编辑设备',`edit_rfid` tinyint  COMMENT ' 是否可以编辑rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:admin_user
 CREATE TABLE admin_user (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100) unique  COMMENT ' 后台管理登录用户',`nick_name` varchar(200)  COMMENT ' 后台管理用户名称',`admin_token` varchar(200)  COMMENT ' 后台管理用户token',`api_token` varchar(200)  COMMENT ' api用户token',`email` varchar(200)  COMMENT ' 用户邮箱',`role_id` int  COMMENT ' 用户角色id',`area_id` int  COMMENT ' 用户区域id',`province_code` int  COMMENT ' 对应的省code',`city_code` int  COMMENT ' 对应的城市code',`section_code` int  COMMENT ' 对应的区域code',`is_single` int  COMMENT ' 是否是个体户，如果是个体户，区域将不起作用',`password` varchar(40)  COMMENT ' 密码',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:mp_user
 CREATE TABLE mp_user (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100) unique  COMMENT ' 小程序用户登录名',`nick_name` varchar(200)  COMMENT ' 小程序用户昵称',`token` varchar(200)  COMMENT ' 小程序用户token',`open_id` varchar(200)  COMMENT ' 小程序账号唯一id',`address` varchar(200)  COMMENT ' 小程序用户地址',`city_name` varchar(200)  COMMENT ' 城市名',`mobile` int  COMMENT ' 小程序用户手机号',`cover` varchar(200)  COMMENT ' 小程序用户头像',`share` int  COMMENT ' 小程序用户分享信息',`sex` int  COMMENT ' 小程序用户性别',`email` varchar(200)  COMMENT ' 小程序用户邮箱',`admin_user_id` int  COMMENT ' 关联后台管理用户id',`password` varchar(40)  COMMENT ' 密码',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_repair
 CREATE TABLE dev_repair (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`title` varchar(2000)  COMMENT ' 报修标题',`content` varchar(5000)  COMMENT ' 报修详情',`err_type` tinyint  COMMENT ' 保修类型 0：设备故障 1：设备缺液 2：质量问题 3：其他',`images` varchar(2000)  COMMENT ' 报修图片',`dev_info` varchar(2000)  COMMENT ' 设备信息',`phone` varchar(20)  COMMENT ' 联系电话',`position` varchar(200)  COMMENT ' 经纬度',`address` varchar(1000)  COMMENT ' 地址',`admin_user_id` int  COMMENT ' 关联的用户id',`status` tinyint  COMMENT ' 报修状态 0：等待受理 1：受理中 2：受理完成',`time_out` tinyint  COMMENT ' 是否过期',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_repair_link
 CREATE TABLE dev_repair_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`admin_user_id` int  COMMENT ' 关联的用户id',`repair_id` int  COMMENT ' 关联的维修id',`status` tinyint  COMMENT ' 操作状态',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_answer
 CREATE TABLE dev_answer (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`title` varchar(2000)  COMMENT ' 问题名称',`cause` varchar(5000)  COMMENT ' 导致问题的可能原因',`tips` varchar(5000)  COMMENT ' 维修详情',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_update_msg
 CREATE TABLE dev_update_msg (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`snno` varchar(40)  COMMENT ' 设备编号',`msg` varchar(40)  COMMENT ' 设备升级状态',`ipaddress` varchar(40)  COMMENT ' 客户端ip',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_msg
 CREATE TABLE dev_msg (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`last_time` datetime  COMMENT ' 最后更新时间',`status` int  COMMENT ' 设备状态',`snno` varchar(50)  COMMENT ' 设备snno',`ccid` varchar(50)  COMMENT ' 设备ccid',`rfid` varchar(50)  COMMENT ' 设备rfid',`proportion` varchar(20)  COMMENT ' 液体配比',`temperature` float  COMMENT ' 设备温度',`humidity` int  COMMENT ' 设备湿度',`nh3` float  COMMENT ' 设备氨气值',`dayon` int  COMMENT ' 白天工作时间',`dayoff` int  COMMENT ' 白天停止时间',`nighton` int  COMMENT ' 晚上工作时间',`nightoff` int  COMMENT ' 晚上停止时间',`addwaternum` int  COMMENT ' 总加液次数',`addwatertime` int  COMMENT ' 单次加液时间',`atomizerpwm` int  COMMENT ' 雾化强度',`fanmin` int  COMMENT ' 风扇最小转速',`fanmax` int  COMMENT ' 风扇最大转速',`totaladdwater` float  COMMENT ' 累计加水量',`hrev` varchar(20)  COMMENT ' 硬件版本',`srev` varchar(20)  COMMENT ' 软件版本',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_cmd
 CREATE TABLE dev_cmd (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`params` text(10000)  COMMENT ' 参数',`ischecked` tinyint  COMMENT ' 是否已经收到应答',`isouttime` tinyint  COMMENT ' 是否过期',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_alarm
 CREATE TABLE dev_alarm (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`alarmnumber` varchar(20)  COMMENT ' 错误代码',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_action
 CREATE TABLE dev_action (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`proportion` varchar(20)  COMMENT ' 液体配比',`temperature` float  COMMENT ' 设备温度',`humidity` int  COMMENT ' 设备湿度',`nh3` float  COMMENT ' 设备氨气值',`dayon` int  COMMENT ' 白天工作时间',`dayoff` int  COMMENT ' 白天停止时间',`nighton` int  COMMENT ' 晚上工作时间',`nightoff` int  COMMENT ' 晚上停止时间',`addwaternum` int  COMMENT ' 总加液次数',`addwatertime` int  COMMENT ' 单次加液时间',`atomizerpwm` int  COMMENT ' 雾化强度',`fanmin` int  COMMENT ' 风扇最小转速',`fanmax` int  COMMENT ' 风扇最大转速',`addtime` int  COMMENT ' 加液次数',`totaladdwater` float  COMMENT ' 累计加水量',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:dev_connect
 CREATE TABLE dev_connect (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(20)  COMMENT ' 设备方法',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:rfid_change
 CREATE TABLE rfid_change (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`newrfid` varchar(50)  COMMENT ' 新的rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:47:39] 创建表:msg_log
 CREATE TABLE msg_log (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`sendto` varchar(20)  COMMENT ' 接受对象',`params` varchar(30000)  COMMENT ' 参数',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev
 CREATE TABLE dev (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100)  COMMENT ' 设备名称',`snno` varchar(40) unique  COMMENT ' 设备编号',`position` varchar(2000)  COMMENT ' 设备经纬度',`address` varchar(2000)  COMMENT ' 设备地址',`dev_info_id` int  COMMENT ' 设备信息id',`rfid_id` int  COMMENT ' 关联的rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_update
 CREATE TABLE dev_update (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`snno` varchar(40) unique  COMMENT ' 设备编号',`status` int  COMMENT ' 设备升级状态',`ipaddress` varchar(40)  COMMENT ' 客户端ip',`hrev` varchar(20)  COMMENT ' 硬件版本',`srev` varchar(20)  COMMENT ' 软件版本',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_info
 CREATE TABLE dev_info (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`last_time` datetime  COMMENT ' 最后更新时间',`status` int  COMMENT ' 设备状态',`snno` varchar(40) unique  COMMENT ' 设备编号',`ccid` varchar(50)  COMMENT ' 设备ccid',`rfid` varchar(50)  COMMENT ' 设备rfid',`proportion` varchar(20)  COMMENT ' 液体配比',`temperature` float  COMMENT ' 设备温度',`humidity` int  COMMENT ' 设备湿度',`nh3` float  COMMENT ' 设备氨气值',`dayon` int  COMMENT ' 白天工作时间',`dayoff` int  COMMENT ' 白天停止时间',`nighton` int  COMMENT ' 晚上工作时间',`nightoff` int  COMMENT ' 晚上停止时间',`addwaternum` int  COMMENT ' 总加液次数',`addwatertime` int  COMMENT ' 单次加液时间',`atomizerpwm` int  COMMENT ' 雾化强度',`fanmin` int  COMMENT ' 风扇最小转速',`fanmax` int  COMMENT ' 风扇最大转速',`totaladdwater` float  COMMENT ' 累计加水量',`alarmnumber` varchar(20)  COMMENT ' 错误代码',`rfid_status` varchar(20)  COMMENT ' rfid状态',`hrev` varchar(20)  COMMENT ' 硬件版本',`srev` varchar(20)  COMMENT ' 软件版本',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:email_send
 CREATE TABLE email_send (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`send_user_id` int  COMMENT ' 发送人id',`snno` varchar(100)  COMMENT ' 设备编号',`to_email` varchar(100)  COMMENT ' 发送的邮箱地址',`subject` varchar(200)  COMMENT ' 发送的标题',`message` varchar(2000)  COMMENT ' 发送的内容',`alarmnumber` varchar(200)  COMMENT ' 错误类型',`status` int  COMMENT ' 是否发送',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:rfid
 CREATE TABLE rfid (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`no` varchar(100) unique  COMMENT ' rfid编号',`liquid_time` datetime  COMMENT ' 上次更新液体时间',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:area
 CREATE TABLE area (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(40)  COMMENT ' 区域名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:admin_dev_link
 CREATE TABLE admin_dev_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`admin_user_id` int  COMMENT ' 后台管理用户id',`dev_id` int  COMMENT ' 设备id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:admin_link
 CREATE TABLE admin_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`parent_admin_id` int  COMMENT ' 关联账户id',`area_id` int  COMMENT ' 关联账户区域id',`admin_id` int  COMMENT ' 账户id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:mp_dev_link
 CREATE TABLE mp_dev_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`mp_user_id` int  COMMENT ' 小程序用户id',`dev_id` int  COMMENT ' 设备id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:mp_link
 CREATE TABLE mp_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`parent_admin_id` int  COMMENT ' 关联账户id',`area_id` int  COMMENT ' 关联账户区域id',`mp_id` int  COMMENT ' 小程序账户id',`status` tinyint  COMMENT ' 状态 0：取消关联 1：建立关联',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_version
 CREATE TABLE dev_version (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`soft_version` varchar(200)  COMMENT ' 设备软件版本号',`hard_version` varchar(200)  COMMENT ' 设备硬件版本号',`file_path` varchar(200)  COMMENT ' 文件名',`status` tinyint  COMMENT ' 状态',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:mp_user_share
 CREATE TABLE mp_user_share (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`mp_user_id` int  COMMENT ' 分享的用户',`title` varchar(200)  COMMENT ' 内容标题',`data_id` int  COMMENT ' 数据id',`type` tinyint  COMMENT ' 类型 0：首页 1：产品列表 2：产品详情 3：问答 4：公司简介 5：联系我们 6：解决方案',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:province
 CREATE TABLE province (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`code` int  COMMENT ' 对应代码',`name` varchar(200)  COMMENT ' 名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:city
 CREATE TABLE city (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`code` int  COMMENT ' 对应代码',`province_code` int  COMMENT ' 所属省份',`name` varchar(200)  COMMENT ' 名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:section
 CREATE TABLE section (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`code` int  COMMENT ' 对应代码',`city_code` int  COMMENT ' 所属区',`name` varchar(200)  COMMENT ' 名称',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:sms
 CREATE TABLE sms (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`user_id` int  COMMENT ' 用户信息',`phone` varchar(11)  COMMENT ' 手机号',`type` int  COMMENT ' 短信类型 0-验证码 1-告警',`status` int  COMMENT ' 状态',`code` varchar(200)  COMMENT ' 验证码',`snno` varchar(200)  COMMENT ' 设备号码',`dev_name` varchar(200)  COMMENT ' 设备名称',`alarm` varchar(200)  COMMENT ' 报警信息',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:api
 CREATE TABLE api (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(40)  COMMENT ' api名称',`router` varchar(40)  COMMENT ' api',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:api_link
 CREATE TABLE api_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`user_id` int  COMMENT ' 用户id',`api_id` int  COMMENT ' api id',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:role
 CREATE TABLE role (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(40)  COMMENT ' 角色名称',`edit_admin_user` tinyint  COMMENT ' 是否可以编辑管理后台用户',`edit_mp_user` tinyint  COMMENT ' 是否可以编辑小程序用户',`edit_role` tinyint  COMMENT ' 是否可以编辑用户角色',`edit_area` tinyint  COMMENT ' 是否可以编辑用户区域',`edit_device` tinyint  COMMENT ' 是否可以编辑设备',`edit_rfid` tinyint  COMMENT ' 是否可以编辑rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:admin_user
 CREATE TABLE admin_user (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100) unique  COMMENT ' 后台管理登录用户',`nick_name` varchar(200)  COMMENT ' 后台管理用户名称',`admin_token` varchar(200)  COMMENT ' 后台管理用户token',`api_token` varchar(200)  COMMENT ' api用户token',`email` varchar(200)  COMMENT ' 用户邮箱',`role_id` int  COMMENT ' 用户角色id',`area_id` int  COMMENT ' 用户区域id',`province_code` int  COMMENT ' 对应的省code',`city_code` int  COMMENT ' 对应的城市code',`section_code` int  COMMENT ' 对应的区域code',`is_single` int  COMMENT ' 是否是个体户，如果是个体户，区域将不起作用',`password` varchar(40)  COMMENT ' 密码',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:mp_user
 CREATE TABLE mp_user (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`name` varchar(100) unique  COMMENT ' 小程序用户登录名',`nick_name` varchar(200)  COMMENT ' 小程序用户昵称',`token` varchar(200)  COMMENT ' 小程序用户token',`open_id` varchar(200)  COMMENT ' 小程序账号唯一id',`address` varchar(200)  COMMENT ' 小程序用户地址',`city_name` varchar(200)  COMMENT ' 城市名',`mobile` int  COMMENT ' 小程序用户手机号',`cover` varchar(200)  COMMENT ' 小程序用户头像',`share` int  COMMENT ' 小程序用户分享信息',`sex` int  COMMENT ' 小程序用户性别',`email` varchar(200)  COMMENT ' 小程序用户邮箱',`admin_user_id` int  COMMENT ' 关联后台管理用户id',`password` varchar(40)  COMMENT ' 密码',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_repair
 CREATE TABLE dev_repair (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`title` varchar(2000)  COMMENT ' 报修标题',`content` varchar(5000)  COMMENT ' 报修详情',`err_type` tinyint  COMMENT ' 保修类型 0：设备故障 1：设备缺液 2：质量问题 3：其他',`images` varchar(2000)  COMMENT ' 报修图片',`dev_info` varchar(2000)  COMMENT ' 设备信息',`phone` varchar(20)  COMMENT ' 联系电话',`position` varchar(200)  COMMENT ' 经纬度',`address` varchar(1000)  COMMENT ' 地址',`admin_user_id` int  COMMENT ' 关联的用户id',`status` tinyint  COMMENT ' 报修状态 0：等待受理 1：受理中 2：受理完成',`time_out` tinyint  COMMENT ' 是否过期',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_repair_link
 CREATE TABLE dev_repair_link (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`admin_user_id` int  COMMENT ' 关联的用户id',`repair_id` int  COMMENT ' 关联的维修id',`status` tinyint  COMMENT ' 操作状态',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_answer
 CREATE TABLE dev_answer (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`title` varchar(2000)  COMMENT ' 问题名称',`cause` varchar(5000)  COMMENT ' 导致问题的可能原因',`tips` varchar(5000)  COMMENT ' 维修详情',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_update_msg
 CREATE TABLE dev_update_msg (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`snno` varchar(40)  COMMENT ' 设备编号',`msg` varchar(40)  COMMENT ' 设备升级状态',`ipaddress` varchar(40)  COMMENT ' 客户端ip',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_msg
 CREATE TABLE dev_msg (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`dev_id` int  COMMENT ' 设备id',`last_time` datetime  COMMENT ' 最后更新时间',`status` int  COMMENT ' 设备状态',`snno` varchar(50)  COMMENT ' 设备snno',`ccid` varchar(50)  COMMENT ' 设备ccid',`rfid` varchar(50)  COMMENT ' 设备rfid',`proportion` varchar(20)  COMMENT ' 液体配比',`temperature` float  COMMENT ' 设备温度',`humidity` int  COMMENT ' 设备湿度',`nh3` float  COMMENT ' 设备氨气值',`dayon` int  COMMENT ' 白天工作时间',`dayoff` int  COMMENT ' 白天停止时间',`nighton` int  COMMENT ' 晚上工作时间',`nightoff` int  COMMENT ' 晚上停止时间',`addwaternum` int  COMMENT ' 总加液次数',`addwatertime` int  COMMENT ' 单次加液时间',`atomizerpwm` int  COMMENT ' 雾化强度',`fanmin` int  COMMENT ' 风扇最小转速',`fanmax` int  COMMENT ' 风扇最大转速',`totaladdwater` float  COMMENT ' 累计加水量',`hrev` varchar(20)  COMMENT ' 硬件版本',`srev` varchar(20)  COMMENT ' 软件版本',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_cmd
 CREATE TABLE dev_cmd (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`params` text(10000)  COMMENT ' 参数',`ischecked` tinyint  COMMENT ' 是否已经收到应答',`isouttime` tinyint  COMMENT ' 是否过期',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_alarm
 CREATE TABLE dev_alarm (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`alarmnumber` varchar(20)  COMMENT ' 错误代码',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_action
 CREATE TABLE dev_action (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`proportion` varchar(20)  COMMENT ' 液体配比',`temperature` float  COMMENT ' 设备温度',`humidity` int  COMMENT ' 设备湿度',`nh3` float  COMMENT ' 设备氨气值',`dayon` int  COMMENT ' 白天工作时间',`dayoff` int  COMMENT ' 白天停止时间',`nighton` int  COMMENT ' 晚上工作时间',`nightoff` int  COMMENT ' 晚上停止时间',`addwaternum` int  COMMENT ' 总加液次数',`addwatertime` int  COMMENT ' 单次加液时间',`atomizerpwm` int  COMMENT ' 雾化强度',`fanmin` int  COMMENT ' 风扇最小转速',`fanmax` int  COMMENT ' 风扇最大转速',`addtime` int  COMMENT ' 加液次数',`totaladdwater` float  COMMENT ' 累计加水量',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:dev_connect
 CREATE TABLE dev_connect (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(20)  COMMENT ' 设备方法',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:rfid_change
 CREATE TABLE rfid_change (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`newrfid` varchar(50)  COMMENT ' 新的rfid',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';

#[2020-05-29 11:48:15] 创建表:msg_log
 CREATE TABLE msg_log (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY  COMMENT ' 记录ID',`snno` varchar(40)  COMMENT ' 设备snno',`method` varchar(40)  COMMENT ' 上报方法',`sendto` varchar(20)  COMMENT ' 接受对象',`params` text(30000)  COMMENT ' 参数',`create_at` DATETIME  COMMENT ' 创建于',`update_at` DATETIME  COMMENT ' 更新于',`delete_at` DATETIME COMMENT ' 删除于') ENGINE=InnoDB DEFAULT CHARSET='utf8';
