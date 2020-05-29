package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Admin_link;
import java.util.Map;

public class Admin_linkProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,parent_admin_id,area_id,admin_id,status,create_at,update_at,delete_at from admin_link limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,parent_admin_id,area_id,admin_id,status,create_at,update_at,delete_at from admin_link where admin_link.id=#{id}";
    }

    public String deleteOne() {

        return "delete from admin_link where id = #{id}";
    }

    public String insertOne(Admin_link admin_link) {

        String key = "";
        String value = "";
        if (admin_link.getId() != null && admin_link.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (admin_link.getParent_admin_id() != null && admin_link.getParent_admin_id() > 0) {
           key += "parent_admin_id,";
           value += "#{parent_admin_id},";
        }

        if (admin_link.getArea_id() != null && admin_link.getArea_id() > 0) {
           key += "area_id,";
           value += "#{area_id},";
        }

        if (admin_link.getAdmin_id() != null && admin_link.getAdmin_id() > 0) {
           key += "admin_id,";
           value += "#{admin_id},";
        }

        if (admin_link.getStatus() != null && admin_link.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (admin_link.getCreate_at() != null && admin_link.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (admin_link.getUpdate_at() != null && admin_link.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (admin_link.getDelete_at() != null && admin_link.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into admin_link (" + key + ") values (" + value + ")";
    }

    public String updateOne(Admin_link admin_link) {

        String sql = "";
        if (admin_link.getId() != null && admin_link.getId() > 0) {
           sql += "id = #{id},";
        }

        if (admin_link.getParent_admin_id() != null && admin_link.getParent_admin_id() > 0) {
           sql += "parent_admin_id = #{parent_admin_id},";
        }

        if (admin_link.getArea_id() != null && admin_link.getArea_id() > 0) {
           sql += "area_id = #{area_id},";
        }

        if (admin_link.getAdmin_id() != null && admin_link.getAdmin_id() > 0) {
           sql += "admin_id = #{admin_id},";
        }

        if (admin_link.getStatus() != null && admin_link.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (admin_link.getCreate_at() != null && admin_link.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (admin_link.getUpdate_at() != null && admin_link.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (admin_link.getDelete_at() != null && admin_link.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update admin_link set " + sql + " where id = #{id}";
    }
}
