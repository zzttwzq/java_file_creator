package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Role;
import java.util.Map;

public class RoleProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,name,edit_admin_user,edit_mp_user,edit_role,edit_area,edit_device,edit_rfid,create_at,update_at,delete_at from role limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,name,edit_admin_user,edit_mp_user,edit_role,edit_area,edit_device,edit_rfid,create_at,update_at,delete_at from role where role.id=#{id}";
    }

    public String deleteOne() {

        return "delete from role where id = #{id}";
    }

    public String insertOne(Role role) {

        String key = "";
        String value = "";
        if (role.getId() != null && role.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (role.getName() != null && !role.getName().isEmpty()) {
           key += "name,";
           value += "#{name},";
        }

        if (role.getEdit_admin_user() != null && role.getEdit_admin_user() > 0) {
           key += "edit_admin_user,";
           value += "#{edit_admin_user},";
        }

        if (role.getEdit_mp_user() != null && role.getEdit_mp_user() > 0) {
           key += "edit_mp_user,";
           value += "#{edit_mp_user},";
        }

        if (role.getEdit_role() != null && role.getEdit_role() > 0) {
           key += "edit_role,";
           value += "#{edit_role},";
        }

        if (role.getEdit_area() != null && role.getEdit_area() > 0) {
           key += "edit_area,";
           value += "#{edit_area},";
        }

        if (role.getEdit_device() != null && role.getEdit_device() > 0) {
           key += "edit_device,";
           value += "#{edit_device},";
        }

        if (role.getEdit_rfid() != null && role.getEdit_rfid() > 0) {
           key += "edit_rfid,";
           value += "#{edit_rfid},";
        }

        if (role.getCreate_at() != null && role.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (role.getUpdate_at() != null && role.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (role.getDelete_at() != null && role.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into role (" + key + ") values (" + value + ")";
    }

    public String updateOne(Role role) {

        String sql = "";
        if (role.getId() != null && role.getId() > 0) {
           sql += "id = #{id},";
        }

        if (role.getName() != null && !role.getName().isEmpty()) {
           sql += "name = #{name},";
        }

        if (role.getEdit_admin_user() != null && role.getEdit_admin_user() > 0) {
           sql += "edit_admin_user = #{edit_admin_user},";
        }

        if (role.getEdit_mp_user() != null && role.getEdit_mp_user() > 0) {
           sql += "edit_mp_user = #{edit_mp_user},";
        }

        if (role.getEdit_role() != null && role.getEdit_role() > 0) {
           sql += "edit_role = #{edit_role},";
        }

        if (role.getEdit_area() != null && role.getEdit_area() > 0) {
           sql += "edit_area = #{edit_area},";
        }

        if (role.getEdit_device() != null && role.getEdit_device() > 0) {
           sql += "edit_device = #{edit_device},";
        }

        if (role.getEdit_rfid() != null && role.getEdit_rfid() > 0) {
           sql += "edit_rfid = #{edit_rfid},";
        }

        if (role.getCreate_at() != null && role.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (role.getUpdate_at() != null && role.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (role.getDelete_at() != null && role.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update role set " + sql + " where id = #{id}";
    }
}
