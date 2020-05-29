package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Dev_update;
import java.util.Map;

public class Dev_updateProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,dev_id,snno,status,ipaddress,hrev,srev,create_at,update_at,delete_at from dev_update limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,dev_id,snno,status,ipaddress,hrev,srev,create_at,update_at,delete_at from dev_update where dev_update.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_update where id = #{id}";
    }

    public String insertOne(Dev_update dev_update) {

        String key = "";
        String value = "";
        if (dev_update.getId() != null && dev_update.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_update.getDev_id() != null && dev_update.getDev_id() > 0) {
           key += "dev_id,";
           value += "#{dev_id},";
        }

        if (dev_update.getSnno() != null && !dev_update.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (dev_update.getStatus() != null && dev_update.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (dev_update.getIpaddress() != null && !dev_update.getIpaddress().isEmpty()) {
           key += "ipaddress,";
           value += "#{ipaddress},";
        }

        if (dev_update.getHrev() != null && !dev_update.getHrev().isEmpty()) {
           key += "hrev,";
           value += "#{hrev},";
        }

        if (dev_update.getSrev() != null && !dev_update.getSrev().isEmpty()) {
           key += "srev,";
           value += "#{srev},";
        }

        if (dev_update.getCreate_at() != null && dev_update.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_update.getUpdate_at() != null && dev_update.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_update.getDelete_at() != null && dev_update.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_update (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_update dev_update) {

        String sql = "";
        if (dev_update.getId() != null && dev_update.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_update.getDev_id() != null && dev_update.getDev_id() > 0) {
           sql += "dev_id = #{dev_id},";
        }

        if (dev_update.getSnno() != null && !dev_update.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (dev_update.getStatus() != null && dev_update.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (dev_update.getIpaddress() != null && !dev_update.getIpaddress().isEmpty()) {
           sql += "ipaddress = #{ipaddress},";
        }

        if (dev_update.getHrev() != null && !dev_update.getHrev().isEmpty()) {
           sql += "hrev = #{hrev},";
        }

        if (dev_update.getSrev() != null && !dev_update.getSrev().isEmpty()) {
           sql += "srev = #{srev},";
        }

        if (dev_update.getCreate_at() != null && dev_update.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_update.getUpdate_at() != null && dev_update.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_update.getDelete_at() != null && dev_update.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_update set " + sql + " where id = #{id}";
    }
}
