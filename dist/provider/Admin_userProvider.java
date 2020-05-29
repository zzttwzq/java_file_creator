package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Admin_user;
import java.util.Map;

public class Admin_userProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,name,nick_name,admin_token,api_token,email,role_id,area_id,province_code,city_code,section_code,is_single,password,create_at,update_at,delete_at from admin_user limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,name,nick_name,admin_token,api_token,email,role_id,area_id,province_code,city_code,section_code,is_single,password,create_at,update_at,delete_at from admin_user where admin_user.id=#{id}";
    }

    public String deleteOne() {

        return "delete from admin_user where id = #{id}";
    }

    public String insertOne(Admin_user admin_user) {

        String key = "";
        String value = "";
        if (admin_user.getId() != null && admin_user.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (admin_user.getName() != null && !admin_user.getName().isEmpty()) {
           key += "name,";
           value += "#{name},";
        }

        if (admin_user.getNick_name() != null && !admin_user.getNick_name().isEmpty()) {
           key += "nick_name,";
           value += "#{nick_name},";
        }

        if (admin_user.getAdmin_token() != null && !admin_user.getAdmin_token().isEmpty()) {
           key += "admin_token,";
           value += "#{admin_token},";
        }

        if (admin_user.getApi_token() != null && !admin_user.getApi_token().isEmpty()) {
           key += "api_token,";
           value += "#{api_token},";
        }

        if (admin_user.getEmail() != null && !admin_user.getEmail().isEmpty()) {
           key += "email,";
           value += "#{email},";
        }

        if (admin_user.getRole_id() != null && admin_user.getRole_id() > 0) {
           key += "role_id,";
           value += "#{role_id},";
        }

        if (admin_user.getArea_id() != null && admin_user.getArea_id() > 0) {
           key += "area_id,";
           value += "#{area_id},";
        }

        if (admin_user.getProvince_code() != null && admin_user.getProvince_code() > 0) {
           key += "province_code,";
           value += "#{province_code},";
        }

        if (admin_user.getCity_code() != null && admin_user.getCity_code() > 0) {
           key += "city_code,";
           value += "#{city_code},";
        }

        if (admin_user.getSection_code() != null && admin_user.getSection_code() > 0) {
           key += "section_code,";
           value += "#{section_code},";
        }

        if (admin_user.getIs_single() != null && admin_user.getIs_single() > 0) {
           key += "is_single,";
           value += "#{is_single},";
        }

        if (admin_user.getPassword() != null && !admin_user.getPassword().isEmpty()) {
           key += "password,";
           value += "#{password},";
        }

        if (admin_user.getCreate_at() != null && admin_user.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (admin_user.getUpdate_at() != null && admin_user.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (admin_user.getDelete_at() != null && admin_user.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into admin_user (" + key + ") values (" + value + ")";
    }

    public String updateOne(Admin_user admin_user) {

        String sql = "";
        if (admin_user.getId() != null && admin_user.getId() > 0) {
           sql += "id = #{id},";
        }

        if (admin_user.getName() != null && !admin_user.getName().isEmpty()) {
           sql += "name = #{name},";
        }

        if (admin_user.getNick_name() != null && !admin_user.getNick_name().isEmpty()) {
           sql += "nick_name = #{nick_name},";
        }

        if (admin_user.getAdmin_token() != null && !admin_user.getAdmin_token().isEmpty()) {
           sql += "admin_token = #{admin_token},";
        }

        if (admin_user.getApi_token() != null && !admin_user.getApi_token().isEmpty()) {
           sql += "api_token = #{api_token},";
        }

        if (admin_user.getEmail() != null && !admin_user.getEmail().isEmpty()) {
           sql += "email = #{email},";
        }

        if (admin_user.getRole_id() != null && admin_user.getRole_id() > 0) {
           sql += "role_id = #{role_id},";
        }

        if (admin_user.getArea_id() != null && admin_user.getArea_id() > 0) {
           sql += "area_id = #{area_id},";
        }

        if (admin_user.getProvince_code() != null && admin_user.getProvince_code() > 0) {
           sql += "province_code = #{province_code},";
        }

        if (admin_user.getCity_code() != null && admin_user.getCity_code() > 0) {
           sql += "city_code = #{city_code},";
        }

        if (admin_user.getSection_code() != null && admin_user.getSection_code() > 0) {
           sql += "section_code = #{section_code},";
        }

        if (admin_user.getIs_single() != null && admin_user.getIs_single() > 0) {
           sql += "is_single = #{is_single},";
        }

        if (admin_user.getPassword() != null && !admin_user.getPassword().isEmpty()) {
           sql += "password = #{password},";
        }

        if (admin_user.getCreate_at() != null && admin_user.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (admin_user.getUpdate_at() != null && admin_user.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (admin_user.getDelete_at() != null && admin_user.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update admin_user set " + sql + " where id = #{id}";
    }
}
