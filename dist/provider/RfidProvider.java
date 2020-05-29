package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Rfid;
import java.util.Map;

public class RfidProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,no,liquid_time,create_at,update_at,delete_at from rfid limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,no,liquid_time,create_at,update_at,delete_at from rfid where rfid.id=#{id}";
    }

    public String deleteOne() {

        return "delete from rfid where id = #{id}";
    }

    public String insertOne(Rfid rfid) {

        String key = "";
        String value = "";
        if (rfid.getId() != null && rfid.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (rfid.getNo() != null && !rfid.getNo().isEmpty()) {
           key += "no,";
           value += "#{no},";
        }

        if (rfid.getLiquid_time() != null && rfid.getLiquid_time() > 0) {
           key += "liquid_time,";
           value += "#{liquid_time},";
        }

        if (rfid.getCreate_at() != null && rfid.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (rfid.getUpdate_at() != null && rfid.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (rfid.getDelete_at() != null && rfid.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into rfid (" + key + ") values (" + value + ")";
    }

    public String updateOne(Rfid rfid) {

        String sql = "";
        if (rfid.getId() != null && rfid.getId() > 0) {
           sql += "id = #{id},";
        }

        if (rfid.getNo() != null && !rfid.getNo().isEmpty()) {
           sql += "no = #{no},";
        }

        if (rfid.getLiquid_time() != null && rfid.getLiquid_time() > 0) {
           sql += "liquid_time = #{liquid_time},";
        }

        if (rfid.getCreate_at() != null && rfid.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (rfid.getUpdate_at() != null && rfid.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (rfid.getDelete_at() != null && rfid.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update rfid set " + sql + " where id = #{id}";
    }
}
