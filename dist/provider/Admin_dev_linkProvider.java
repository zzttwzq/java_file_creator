package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Admin_dev_link;
import java.util.Map;

public class Admin_dev_linkProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,admin_user_id,dev_id,status,create_at,update_at,delete_at from admin_dev_link limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,admin_user_id,dev_id,status,create_at,update_at,delete_at from admin_dev_link where admin_dev_link.id=#{id}";
    }

    public String deleteOne() {

        return "delete from admin_dev_link where id = #{id}";
    }

    public String insertOne(Admin_dev_link admin_dev_link) {

        String key = "";
        String value = "";
        if (admin_dev_link.getId() != null && admin_dev_link.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (admin_dev_link.getAdmin_user_id() != null && admin_dev_link.getAdmin_user_id() > 0) {
           key += "admin_user_id,";
           value += "#{admin_user_id},";
        }

        if (admin_dev_link.getDev_id() != null && admin_dev_link.getDev_id() > 0) {
           key += "dev_id,";
           value += "#{dev_id},";
        }

        if (admin_dev_link.getStatus() != null && admin_dev_link.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (admin_dev_link.getCreate_at() != null && admin_dev_link.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (admin_dev_link.getUpdate_at() != null && admin_dev_link.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (admin_dev_link.getDelete_at() != null && admin_dev_link.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into admin_dev_link (" + key + ") values (" + value + ")";
    }

    public String updateOne(Admin_dev_link admin_dev_link) {

        String sql = "";
        if (admin_dev_link.getId() != null && admin_dev_link.getId() > 0) {
           sql += "id = #{id},";
        }

        if (admin_dev_link.getAdmin_user_id() != null && admin_dev_link.getAdmin_user_id() > 0) {
           sql += "admin_user_id = #{admin_user_id},";
        }

        if (admin_dev_link.getDev_id() != null && admin_dev_link.getDev_id() > 0) {
           sql += "dev_id = #{dev_id},";
        }

        if (admin_dev_link.getStatus() != null && admin_dev_link.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (admin_dev_link.getCreate_at() != null && admin_dev_link.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (admin_dev_link.getUpdate_at() != null && admin_dev_link.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (admin_dev_link.getDelete_at() != null && admin_dev_link.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update admin_dev_link set " + sql + " where id = #{id}";
    }
}
