package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Role {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private String name; // 角色名称 
    private Integer edit_admin_user; // 是否可以编辑管理后台用户 
    private Integer edit_mp_user; // 是否可以编辑小程序用户 
    private Integer edit_role; // 是否可以编辑用户角色 
    private Integer edit_area; // 是否可以编辑用户区域 
    private Integer edit_device; // 是否可以编辑设备 
    private Integer edit_rfid; // 是否可以编辑rfid 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Role(Long id,String name,Integer edit_admin_user,Integer edit_mp_user,Integer edit_role,Integer edit_area,Integer edit_device,Integer edit_rfid,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.name=name;
        this.edit_admin_user=edit_admin_user;
        this.edit_mp_user=edit_mp_user;
        this.edit_role=edit_role;
        this.edit_area=edit_area;
        this.edit_device=edit_device;
        this.edit_rfid=edit_rfid;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Role() {}

    public Long getId () { return this.id;}

    public String getName () { return this.name;}

    public Integer getEdit_admin_user () { return this.edit_admin_user;}

    public Integer getEdit_mp_user () { return this.edit_mp_user;}

    public Integer getEdit_role () { return this.edit_role;}

    public Integer getEdit_area () { return this.edit_area;}

    public Integer getEdit_device () { return this.edit_device;}

    public Integer getEdit_rfid () { return this.edit_rfid;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setName (String name) { this.name = name;}

    public void setEdit_admin_user (Integer edit_admin_user) { this.edit_admin_user = edit_admin_user;}

    public void setEdit_mp_user (Integer edit_mp_user) { this.edit_mp_user = edit_mp_user;}

    public void setEdit_role (Integer edit_role) { this.edit_role = edit_role;}

    public void setEdit_area (Integer edit_area) { this.edit_area = edit_area;}

    public void setEdit_device (Integer edit_device) { this.edit_device = edit_device;}

    public void setEdit_rfid (Integer edit_rfid) { this.edit_rfid = edit_rfid;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Role> {id = " + id + " " +
                "name = '" + name + "' " +
                "edit_admin_user = " + edit_admin_user + " " +
                "edit_mp_user = " + edit_mp_user + " " +
                "edit_role = " + edit_role + " " +
                "edit_area = " + edit_area + " " +
                "edit_device = " + edit_device + " " +
                "edit_rfid = " + edit_rfid + " " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}