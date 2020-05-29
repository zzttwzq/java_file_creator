package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Mp_user;
import java.util.Map;

public class Mp_userProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,name,nick_name,token,open_id,address,city_name,mobile,cover,share,sex,email,admin_user_id,password,create_at,update_at,delete_at from mp_user limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,name,nick_name,token,open_id,address,city_name,mobile,cover,share,sex,email,admin_user_id,password,create_at,update_at,delete_at from mp_user where mp_user.id=#{id}";
    }

    public String deleteOne() {

        return "delete from mp_user where id = #{id}";
    }

    public String insertOne(Mp_user mp_user) {

        String key = "";
        String value = "";
        if (mp_user.getId() != null && mp_user.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (mp_user.getName() != null && !mp_user.getName().isEmpty()) {
           key += "name,";
           value += "#{name},";
        }

        if (mp_user.getNick_name() != null && !mp_user.getNick_name().isEmpty()) {
           key += "nick_name,";
           value += "#{nick_name},";
        }

        if (mp_user.getToken() != null && !mp_user.getToken().isEmpty()) {
           key += "token,";
           value += "#{token},";
        }

        if (mp_user.getOpen_id() != null && !mp_user.getOpen_id().isEmpty()) {
           key += "open_id,";
           value += "#{open_id},";
        }

        if (mp_user.getAddress() != null && !mp_user.getAddress().isEmpty()) {
           key += "address,";
           value += "#{address},";
        }

        if (mp_user.getCity_name() != null && !mp_user.getCity_name().isEmpty()) {
           key += "city_name,";
           value += "#{city_name},";
        }

        if (mp_user.getMobile() != null && mp_user.getMobile() > 0) {
           key += "mobile,";
           value += "#{mobile},";
        }

        if (mp_user.getCover() != null && !mp_user.getCover().isEmpty()) {
           key += "cover,";
           value += "#{cover},";
        }

        if (mp_user.getShare() != null && mp_user.getShare() > 0) {
           key += "share,";
           value += "#{share},";
        }

        if (mp_user.getSex() != null && mp_user.getSex() > 0) {
           key += "sex,";
           value += "#{sex},";
        }

        if (mp_user.getEmail() != null && !mp_user.getEmail().isEmpty()) {
           key += "email,";
           value += "#{email},";
        }

        if (mp_user.getAdmin_user_id() != null && mp_user.getAdmin_user_id() > 0) {
           key += "admin_user_id,";
           value += "#{admin_user_id},";
        }

        if (mp_user.getPassword() != null && !mp_user.getPassword().isEmpty()) {
           key += "password,";
           value += "#{password},";
        }

        if (mp_user.getCreate_at() != null && mp_user.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (mp_user.getUpdate_at() != null && mp_user.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (mp_user.getDelete_at() != null && mp_user.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into mp_user (" + key + ") values (" + value + ")";
    }

    public String updateOne(Mp_user mp_user) {

        String sql = "";
        if (mp_user.getId() != null && mp_user.getId() > 0) {
           sql += "id = #{id},";
        }

        if (mp_user.getName() != null && !mp_user.getName().isEmpty()) {
           sql += "name = #{name},";
        }

        if (mp_user.getNick_name() != null && !mp_user.getNick_name().isEmpty()) {
           sql += "nick_name = #{nick_name},";
        }

        if (mp_user.getToken() != null && !mp_user.getToken().isEmpty()) {
           sql += "token = #{token},";
        }

        if (mp_user.getOpen_id() != null && !mp_user.getOpen_id().isEmpty()) {
           sql += "open_id = #{open_id},";
        }

        if (mp_user.getAddress() != null && !mp_user.getAddress().isEmpty()) {
           sql += "address = #{address},";
        }

        if (mp_user.getCity_name() != null && !mp_user.getCity_name().isEmpty()) {
           sql += "city_name = #{city_name},";
        }

        if (mp_user.getMobile() != null && mp_user.getMobile() > 0) {
           sql += "mobile = #{mobile},";
        }

        if (mp_user.getCover() != null && !mp_user.getCover().isEmpty()) {
           sql += "cover = #{cover},";
        }

        if (mp_user.getShare() != null && mp_user.getShare() > 0) {
           sql += "share = #{share},";
        }

        if (mp_user.getSex() != null && mp_user.getSex() > 0) {
           sql += "sex = #{sex},";
        }

        if (mp_user.getEmail() != null && !mp_user.getEmail().isEmpty()) {
           sql += "email = #{email},";
        }

        if (mp_user.getAdmin_user_id() != null && mp_user.getAdmin_user_id() > 0) {
           sql += "admin_user_id = #{admin_user_id},";
        }

        if (mp_user.getPassword() != null && !mp_user.getPassword().isEmpty()) {
           sql += "password = #{password},";
        }

        if (mp_user.getCreate_at() != null && mp_user.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (mp_user.getUpdate_at() != null && mp_user.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (mp_user.getDelete_at() != null && mp_user.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update mp_user set " + sql + " where id = #{id}";
    }
}
