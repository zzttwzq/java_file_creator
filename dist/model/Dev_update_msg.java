package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Dev_update_msg {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private Integer dev_id; // 设备id 
    private String snno; // 设备编号 
    private String msg; // 设备升级状态 
    private String ipaddress; // 客户端ip 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Dev_update_msg(Long id,Integer dev_id,String snno,String msg,String ipaddress,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.dev_id=dev_id;
        this.snno=snno;
        this.msg=msg;
        this.ipaddress=ipaddress;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Dev_update_msg() {}

    public Long getId () { return this.id;}

    public Integer getDev_id () { return this.dev_id;}

    public String getSnno () { return this.snno;}

    public String getMsg () { return this.msg;}

    public String getIpaddress () { return this.ipaddress;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setDev_id (Integer dev_id) { this.dev_id = dev_id;}

    public void setSnno (String snno) { this.snno = snno;}

    public void setMsg (String msg) { this.msg = msg;}

    public void setIpaddress (String ipaddress) { this.ipaddress = ipaddress;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Dev_update_msg> {id = " + id + " " +
                "dev_id = " + dev_id + " " +
                "snno = '" + snno + "' " +
                "msg = '" + msg + "' " +
                "ipaddress = '" + ipaddress + "' " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}