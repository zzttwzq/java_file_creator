package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Email_send;
import java.util.Map;

public class Email_sendProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,send_user_id,snno,to_email,subject,message,alarmnumber,status,create_at,update_at,delete_at from email_send limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,send_user_id,snno,to_email,subject,message,alarmnumber,status,create_at,update_at,delete_at from email_send where email_send.id=#{id}";
    }

    public String deleteOne() {

        return "delete from email_send where id = #{id}";
    }

    public String insertOne(Email_send email_send) {

        String key = "";
        String value = "";
        if (email_send.getId() != null && email_send.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (email_send.getSend_user_id() != null && email_send.getSend_user_id() > 0) {
           key += "send_user_id,";
           value += "#{send_user_id},";
        }

        if (email_send.getSnno() != null && !email_send.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (email_send.getTo_email() != null && !email_send.getTo_email().isEmpty()) {
           key += "to_email,";
           value += "#{to_email},";
        }

        if (email_send.getSubject() != null && !email_send.getSubject().isEmpty()) {
           key += "subject,";
           value += "#{subject},";
        }

        if (email_send.getMessage() != null && !email_send.getMessage().isEmpty()) {
           key += "message,";
           value += "#{message},";
        }

        if (email_send.getAlarmnumber() != null && !email_send.getAlarmnumber().isEmpty()) {
           key += "alarmnumber,";
           value += "#{alarmnumber},";
        }

        if (email_send.getStatus() != null && email_send.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (email_send.getCreate_at() != null && email_send.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (email_send.getUpdate_at() != null && email_send.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (email_send.getDelete_at() != null && email_send.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into email_send (" + key + ") values (" + value + ")";
    }

    public String updateOne(Email_send email_send) {

        String sql = "";
        if (email_send.getId() != null && email_send.getId() > 0) {
           sql += "id = #{id},";
        }

        if (email_send.getSend_user_id() != null && email_send.getSend_user_id() > 0) {
           sql += "send_user_id = #{send_user_id},";
        }

        if (email_send.getSnno() != null && !email_send.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (email_send.getTo_email() != null && !email_send.getTo_email().isEmpty()) {
           sql += "to_email = #{to_email},";
        }

        if (email_send.getSubject() != null && !email_send.getSubject().isEmpty()) {
           sql += "subject = #{subject},";
        }

        if (email_send.getMessage() != null && !email_send.getMessage().isEmpty()) {
           sql += "message = #{message},";
        }

        if (email_send.getAlarmnumber() != null && !email_send.getAlarmnumber().isEmpty()) {
           sql += "alarmnumber = #{alarmnumber},";
        }

        if (email_send.getStatus() != null && email_send.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (email_send.getCreate_at() != null && email_send.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (email_send.getUpdate_at() != null && email_send.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (email_send.getDelete_at() != null && email_send.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update email_send set " + sql + " where id = #{id}";
    }
}
