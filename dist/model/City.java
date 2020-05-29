package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class City {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private Integer code; // 对应代码 
    private Integer province_code; // 所属省份 
    private String name; // 名称 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public City(Long id,Integer code,Integer province_code,String name,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.code=code;
        this.province_code=province_code;
        this.name=name;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public City() {}

    public Long getId () { return this.id;}

    public Integer getCode () { return this.code;}

    public Integer getProvince_code () { return this.province_code;}

    public String getName () { return this.name;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setCode (Integer code) { this.code = code;}

    public void setProvince_code (Integer province_code) { this.province_code = province_code;}

    public void setName (String name) { this.name = name;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <City> {id = " + id + " " +
                "code = " + code + " " +
                "province_code = " + province_code + " " +
                "name = '" + name + "' " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}