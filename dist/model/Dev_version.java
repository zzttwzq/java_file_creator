package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Dev_version {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private String soft_version; // 设备软件版本号 
    private String hard_version; // 设备硬件版本号 
    private String file_path; // 文件名 
    private Integer status; // 状态 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Dev_version(Long id,String soft_version,String hard_version,String file_path,Integer status,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.soft_version=soft_version;
        this.hard_version=hard_version;
        this.file_path=file_path;
        this.status=status;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Dev_version() {}

    public Long getId () { return this.id;}

    public String getSoft_version () { return this.soft_version;}

    public String getHard_version () { return this.hard_version;}

    public String getFile_path () { return this.file_path;}

    public Integer getStatus () { return this.status;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setSoft_version (String soft_version) { this.soft_version = soft_version;}

    public void setHard_version (String hard_version) { this.hard_version = hard_version;}

    public void setFile_path (String file_path) { this.file_path = file_path;}

    public void setStatus (Integer status) { this.status = status;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Dev_version> {id = " + id + " " +
                "soft_version = '" + soft_version + "' " +
                "hard_version = '" + hard_version + "' " +
                "file_path = '" + file_path + "' " +
                "status = " + status + " " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}