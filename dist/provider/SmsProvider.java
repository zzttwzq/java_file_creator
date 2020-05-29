package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Sms;
import java.util.Map;

public class SmsProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,user_id,phone,type,status,code,snno,dev_name,alarm,create_at,update_at,delete_at from sms limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,user_id,phone,type,status,code,snno,dev_name,alarm,create_at,update_at,delete_at from sms where sms.id=#{id}";
    }

    public String deleteOne() {

        return "delete from sms where id = #{id}";
    }

    public String insertOne(Sms sms) {

        String key = "";
        String value = "";
        if (sms.getId() != null && sms.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (sms.getUser_id() != null && sms.getUser_id() > 0) {
           key += "user_id,";
           value += "#{user_id},";
        }

        if (sms.getPhone() != null && !sms.getPhone().isEmpty()) {
           key += "phone,";
           value += "#{phone},";
        }

        if (sms.getType() != null && sms.getType() > 0) {
           key += "type,";
           value += "#{type},";
        }

        if (sms.getStatus() != null && sms.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (sms.getCode() != null && !sms.getCode().isEmpty()) {
           key += "code,";
           value += "#{code},";
        }

        if (sms.getSnno() != null && !sms.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (sms.getDev_name() != null && !sms.getDev_name().isEmpty()) {
           key += "dev_name,";
           value += "#{dev_name},";
        }

        if (sms.getAlarm() != null && !sms.getAlarm().isEmpty()) {
           key += "alarm,";
           value += "#{alarm},";
        }

        if (sms.getCreate_at() != null && sms.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (sms.getUpdate_at() != null && sms.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (sms.getDelete_at() != null && sms.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into sms (" + key + ") values (" + value + ")";
    }

    public String updateOne(Sms sms) {

        String sql = "";
        if (sms.getId() != null && sms.getId() > 0) {
           sql += "id = #{id},";
        }

        if (sms.getUser_id() != null && sms.getUser_id() > 0) {
           sql += "user_id = #{user_id},";
        }

        if (sms.getPhone() != null && !sms.getPhone().isEmpty()) {
           sql += "phone = #{phone},";
        }

        if (sms.getType() != null && sms.getType() > 0) {
           sql += "type = #{type},";
        }

        if (sms.getStatus() != null && sms.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (sms.getCode() != null && !sms.getCode().isEmpty()) {
           sql += "code = #{code},";
        }

        if (sms.getSnno() != null && !sms.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (sms.getDev_name() != null && !sms.getDev_name().isEmpty()) {
           sql += "dev_name = #{dev_name},";
        }

        if (sms.getAlarm() != null && !sms.getAlarm().isEmpty()) {
           sql += "alarm = #{alarm},";
        }

        if (sms.getCreate_at() != null && sms.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (sms.getUpdate_at() != null && sms.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (sms.getDelete_at() != null && sms.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update sms set " + sql + " where id = #{id}";
    }
}
