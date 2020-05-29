package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Area;
import java.util.Map;

public class AreaProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,name,create_at,update_at,delete_at from area limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,name,create_at,update_at,delete_at from area where area.id=#{id}";
    }

    public String deleteOne() {

        return "delete from area where id = #{id}";
    }

    public String insertOne(Area area) {

        String key = "";
        String value = "";
        if (area.getId() != null && area.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (area.getName() != null && !area.getName().isEmpty()) {
           key += "name,";
           value += "#{name},";
        }

        if (area.getCreate_at() != null && area.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (area.getUpdate_at() != null && area.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (area.getDelete_at() != null && area.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into area (" + key + ") values (" + value + ")";
    }

    public String updateOne(Area area) {

        String sql = "";
        if (area.getId() != null && area.getId() > 0) {
           sql += "id = #{id},";
        }

        if (area.getName() != null && !area.getName().isEmpty()) {
           sql += "name = #{name},";
        }

        if (area.getCreate_at() != null && area.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (area.getUpdate_at() != null && area.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (area.getDelete_at() != null && area.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update area set " + sql + " where id = #{id}";
    }
}
