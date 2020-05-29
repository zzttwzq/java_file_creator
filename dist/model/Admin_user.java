package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Admin_user {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private String name; // 后台管理登录用户 
    private String nick_name; // 后台管理用户名称 
    private String admin_token; // 后台管理用户token 
    private String api_token; // api用户token 
    private String email; // 用户邮箱 
    private Integer role_id; // 用户角色id 
    private Integer area_id; // 用户区域id 
    private Integer province_code; // 对应的省code 
    private Integer city_code; // 对应的城市code 
    private Integer section_code; // 对应的区域code 
    private Integer is_single; // 是否是个体户，如果是个体户，区域将不起作用 
    private String password; // 密码 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Admin_user(Long id,String name,String nick_name,String admin_token,String api_token,String email,Integer role_id,Integer area_id,Integer province_code,Integer city_code,Integer section_code,Integer is_single,String password,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.name=name;
        this.nick_name=nick_name;
        this.admin_token=admin_token;
        this.api_token=api_token;
        this.email=email;
        this.role_id=role_id;
        this.area_id=area_id;
        this.province_code=province_code;
        this.city_code=city_code;
        this.section_code=section_code;
        this.is_single=is_single;
        this.password=password;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Admin_user() {}

    public Long getId () { return this.id;}

    public String getName () { return this.name;}

    public String getNick_name () { return this.nick_name;}

    public String getAdmin_token () { return this.admin_token;}

    public String getApi_token () { return this.api_token;}

    public String getEmail () { return this.email;}

    public Integer getRole_id () { return this.role_id;}

    public Integer getArea_id () { return this.area_id;}

    public Integer getProvince_code () { return this.province_code;}

    public Integer getCity_code () { return this.city_code;}

    public Integer getSection_code () { return this.section_code;}

    public Integer getIs_single () { return this.is_single;}

    public String getPassword () { return this.password;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setName (String name) { this.name = name;}

    public void setNick_name (String nick_name) { this.nick_name = nick_name;}

    public void setAdmin_token (String admin_token) { this.admin_token = admin_token;}

    public void setApi_token (String api_token) { this.api_token = api_token;}

    public void setEmail (String email) { this.email = email;}

    public void setRole_id (Integer role_id) { this.role_id = role_id;}

    public void setArea_id (Integer area_id) { this.area_id = area_id;}

    public void setProvince_code (Integer province_code) { this.province_code = province_code;}

    public void setCity_code (Integer city_code) { this.city_code = city_code;}

    public void setSection_code (Integer section_code) { this.section_code = section_code;}

    public void setIs_single (Integer is_single) { this.is_single = is_single;}

    public void setPassword (String password) { this.password = password;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Admin_user> {id = " + id + " " +
                "name = '" + name + "' " +
                "nick_name = '" + nick_name + "' " +
                "admin_token = '" + admin_token + "' " +
                "api_token = '" + api_token + "' " +
                "email = '" + email + "' " +
                "role_id = " + role_id + " " +
                "area_id = " + area_id + " " +
                "province_code = " + province_code + " " +
                "city_code = " + city_code + " " +
                "section_code = " + section_code + " " +
                "is_single = " + is_single + " " +
                "password = '" + password + "' " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}