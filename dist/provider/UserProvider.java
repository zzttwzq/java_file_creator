package com.smartwc.qlzw.com.provider;

import com.smartwc.qlzw.com.utils.Pager;
import com.smartwc.qlzw.com.model.User;
import java.util.Map;

public class UserProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,name,age,create_at,update_at,delete_at from user limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,name,age,create_at,update_at,delete_at from user where user.id=#{id}";
    }

    public String deleteOne() {

        return "delete from user where id = #{id}";
    }

    public String insertOne(User user) {

        String key = "";
        String value = "";
        if (user.getId() != null && user.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (user.getName() != null && !user.getName().isEmpty()) {
           key += "name,";
           value += "#{name},";
        }

        if (user.getAge() != null && user.getAge() > 0) {
           key += "age,";
           value += "#{age},";
        }

        if (user.getCreate_at() != null && user.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (user.getUpdate_at() != null && user.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (user.getDelete_at() != null && user.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into user (" + key + ") values (" + value + ")";
    }

    public String updateOne(User user) {

        String sql = "";
        if (user.getId() != null && user.getId() > 0) {
           sql += "id = #{id},";
        }

        if (user.getName() != null && !user.getName().isEmpty()) {
           sql += "name = #{name},";
        }

        if (user.getAge() != null && user.getAge() > 0) {
           sql += "age = #{age},";
        }

        if (user.getCreate_at() != null && user.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (user.getUpdate_at() != null && user.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (user.getDelete_at() != null && user.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update user set " + sql + " where id = #{id}";
    }
}
