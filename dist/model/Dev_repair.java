package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Dev_repair {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private String title; // 报修标题 
    private String content; // 报修详情 
    private Integer err_type; // 保修类型 0：设备故障 1：设备缺液 2：质量问题 3：其他 
    private String images; // 报修图片 
    private String dev_info; // 设备信息 
    private String phone; // 联系电话 
    private String position; // 经纬度 
    private String address; // 地址 
    private Integer admin_user_id; // 关联的用户id 
    private Integer status; // 报修状态 0：等待受理 1：受理中 2：受理完成 
    private Integer time_out; // 是否过期 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Dev_repair(Long id,String title,String content,Integer err_type,String images,String dev_info,String phone,String position,String address,Integer admin_user_id,Integer status,Integer time_out,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.title=title;
        this.content=content;
        this.err_type=err_type;
        this.images=images;
        this.dev_info=dev_info;
        this.phone=phone;
        this.position=position;
        this.address=address;
        this.admin_user_id=admin_user_id;
        this.status=status;
        this.time_out=time_out;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Dev_repair() {}

    public Long getId () { return this.id;}

    public String getTitle () { return this.title;}

    public String getContent () { return this.content;}

    public Integer getErr_type () { return this.err_type;}

    public String getImages () { return this.images;}

    public String getDev_info () { return this.dev_info;}

    public String getPhone () { return this.phone;}

    public String getPosition () { return this.position;}

    public String getAddress () { return this.address;}

    public Integer getAdmin_user_id () { return this.admin_user_id;}

    public Integer getStatus () { return this.status;}

    public Integer getTime_out () { return this.time_out;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setTitle (String title) { this.title = title;}

    public void setContent (String content) { this.content = content;}

    public void setErr_type (Integer err_type) { this.err_type = err_type;}

    public void setImages (String images) { this.images = images;}

    public void setDev_info (String dev_info) { this.dev_info = dev_info;}

    public void setPhone (String phone) { this.phone = phone;}

    public void setPosition (String position) { this.position = position;}

    public void setAddress (String address) { this.address = address;}

    public void setAdmin_user_id (Integer admin_user_id) { this.admin_user_id = admin_user_id;}

    public void setStatus (Integer status) { this.status = status;}

    public void setTime_out (Integer time_out) { this.time_out = time_out;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Dev_repair> {id = " + id + " " +
                "title = '" + title + "' " +
                "content = '" + content + "' " +
                "err_type = " + err_type + " " +
                "images = '" + images + "' " +
                "dev_info = '" + dev_info + "' " +
                "phone = '" + phone + "' " +
                "position = '" + position + "' " +
                "address = '" + address + "' " +
                "admin_user_id = " + admin_user_id + " " +
                "status = " + status + " " +
                "time_out = " + time_out + " " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}