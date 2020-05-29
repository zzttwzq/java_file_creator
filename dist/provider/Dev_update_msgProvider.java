package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Dev_update_msg;
import java.util.Map;

public class Dev_update_msgProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,dev_id,snno,msg,ipaddress,create_at,update_at,delete_at from dev_update_msg limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,dev_id,snno,msg,ipaddress,create_at,update_at,delete_at from dev_update_msg where dev_update_msg.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_update_msg where id = #{id}";
    }

    public String insertOne(Dev_update_msg dev_update_msg) {

        String key = "";
        String value = "";
        if (dev_update_msg.getId() != null && dev_update_msg.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_update_msg.getDev_id() != null && dev_update_msg.getDev_id() > 0) {
           key += "dev_id,";
           value += "#{dev_id},";
        }

        if (dev_update_msg.getSnno() != null && !dev_update_msg.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (dev_update_msg.getMsg() != null && !dev_update_msg.getMsg().isEmpty()) {
           key += "msg,";
           value += "#{msg},";
        }

        if (dev_update_msg.getIpaddress() != null && !dev_update_msg.getIpaddress().isEmpty()) {
           key += "ipaddress,";
           value += "#{ipaddress},";
        }

        if (dev_update_msg.getCreate_at() != null && dev_update_msg.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_update_msg.getUpdate_at() != null && dev_update_msg.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_update_msg.getDelete_at() != null && dev_update_msg.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_update_msg (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_update_msg dev_update_msg) {

        String sql = "";
        if (dev_update_msg.getId() != null && dev_update_msg.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_update_msg.getDev_id() != null && dev_update_msg.getDev_id() > 0) {
           sql += "dev_id = #{dev_id},";
        }

        if (dev_update_msg.getSnno() != null && !dev_update_msg.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (dev_update_msg.getMsg() != null && !dev_update_msg.getMsg().isEmpty()) {
           sql += "msg = #{msg},";
        }

        if (dev_update_msg.getIpaddress() != null && !dev_update_msg.getIpaddress().isEmpty()) {
           sql += "ipaddress = #{ipaddress},";
        }

        if (dev_update_msg.getCreate_at() != null && dev_update_msg.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_update_msg.getUpdate_at() != null && dev_update_msg.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_update_msg.getDelete_at() != null && dev_update_msg.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_update_msg set " + sql + " where id = #{id}";
    }
}
