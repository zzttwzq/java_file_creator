package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Rfid {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private String no; // rfid编号 
    private Integer liquid_time; // 上次更新液体时间 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Rfid(Long id,String no,Integer liquid_time,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.no=no;
        this.liquid_time=liquid_time;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Rfid() {}

    public Long getId () { return this.id;}

    public String getNo () { return this.no;}

    public Integer getLiquid_time () { return this.liquid_time;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setNo (String no) { this.no = no;}

    public void setLiquid_time (Integer liquid_time) { this.liquid_time = liquid_time;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Rfid> {id = " + id + " " +
                "no = '" + no + "' " +
                "liquid_time = " + liquid_time + ", " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}