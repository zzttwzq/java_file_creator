package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Dev_repair_link;
import java.util.Map;

public class Dev_repair_linkProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,admin_user_id,repair_id,status,create_at,update_at,delete_at from dev_repair_link limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,admin_user_id,repair_id,status,create_at,update_at,delete_at from dev_repair_link where dev_repair_link.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_repair_link where id = #{id}";
    }

    public String insertOne(Dev_repair_link dev_repair_link) {

        String key = "";
        String value = "";
        if (dev_repair_link.getId() != null && dev_repair_link.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_repair_link.getAdmin_user_id() != null && dev_repair_link.getAdmin_user_id() > 0) {
           key += "admin_user_id,";
           value += "#{admin_user_id},";
        }

        if (dev_repair_link.getRepair_id() != null && dev_repair_link.getRepair_id() > 0) {
           key += "repair_id,";
           value += "#{repair_id},";
        }

        if (dev_repair_link.getStatus() != null && dev_repair_link.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (dev_repair_link.getCreate_at() != null && dev_repair_link.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_repair_link.getUpdate_at() != null && dev_repair_link.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_repair_link.getDelete_at() != null && dev_repair_link.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_repair_link (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_repair_link dev_repair_link) {

        String sql = "";
        if (dev_repair_link.getId() != null && dev_repair_link.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_repair_link.getAdmin_user_id() != null && dev_repair_link.getAdmin_user_id() > 0) {
           sql += "admin_user_id = #{admin_user_id},";
        }

        if (dev_repair_link.getRepair_id() != null && dev_repair_link.getRepair_id() > 0) {
           sql += "repair_id = #{repair_id},";
        }

        if (dev_repair_link.getStatus() != null && dev_repair_link.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (dev_repair_link.getCreate_at() != null && dev_repair_link.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_repair_link.getUpdate_at() != null && dev_repair_link.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_repair_link.getDelete_at() != null && dev_repair_link.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_repair_link set " + sql + " where id = #{id}";
    }
}
