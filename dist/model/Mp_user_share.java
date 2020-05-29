package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Mp_user_share {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private Integer mp_user_id; // 分享的用户 
    private String title; // 内容标题 
    private Integer data_id; // 数据id 
    private Integer type; // 类型 0：首页 1：产品列表 2：产品详情 3：问答 4：公司简介 5：联系我们 6：解决方案 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Mp_user_share(Long id,Integer mp_user_id,String title,Integer data_id,Integer type,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.mp_user_id=mp_user_id;
        this.title=title;
        this.data_id=data_id;
        this.type=type;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Mp_user_share() {}

    public Long getId () { return this.id;}

    public Integer getMp_user_id () { return this.mp_user_id;}

    public String getTitle () { return this.title;}

    public Integer getData_id () { return this.data_id;}

    public Integer getType () { return this.type;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setMp_user_id (Integer mp_user_id) { this.mp_user_id = mp_user_id;}

    public void setTitle (String title) { this.title = title;}

    public void setData_id (Integer data_id) { this.data_id = data_id;}

    public void setType (Integer type) { this.type = type;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Mp_user_share> {id = " + id + " " +
                "mp_user_id = " + mp_user_id + " " +
                "title = '" + title + "' " +
                "data_id = " + data_id + " " +
                "type = " + type + " " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}