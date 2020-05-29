package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Dev_version;
import java.util.Map;

public class Dev_versionProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,soft_version,hard_version,file_path,status,create_at,update_at,delete_at from dev_version limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,soft_version,hard_version,file_path,status,create_at,update_at,delete_at from dev_version where dev_version.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_version where id = #{id}";
    }

    public String insertOne(Dev_version dev_version) {

        String key = "";
        String value = "";
        if (dev_version.getId() != null && dev_version.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_version.getSoft_version() != null && !dev_version.getSoft_version().isEmpty()) {
           key += "soft_version,";
           value += "#{soft_version},";
        }

        if (dev_version.getHard_version() != null && !dev_version.getHard_version().isEmpty()) {
           key += "hard_version,";
           value += "#{hard_version},";
        }

        if (dev_version.getFile_path() != null && !dev_version.getFile_path().isEmpty()) {
           key += "file_path,";
           value += "#{file_path},";
        }

        if (dev_version.getStatus() != null && dev_version.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (dev_version.getCreate_at() != null && dev_version.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_version.getUpdate_at() != null && dev_version.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_version.getDelete_at() != null && dev_version.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_version (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_version dev_version) {

        String sql = "";
        if (dev_version.getId() != null && dev_version.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_version.getSoft_version() != null && !dev_version.getSoft_version().isEmpty()) {
           sql += "soft_version = #{soft_version},";
        }

        if (dev_version.getHard_version() != null && !dev_version.getHard_version().isEmpty()) {
           sql += "hard_version = #{hard_version},";
        }

        if (dev_version.getFile_path() != null && !dev_version.getFile_path().isEmpty()) {
           sql += "file_path = #{file_path},";
        }

        if (dev_version.getStatus() != null && dev_version.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (dev_version.getCreate_at() != null && dev_version.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_version.getUpdate_at() != null && dev_version.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_version.getDelete_at() != null && dev_version.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_version set " + sql + " where id = #{id}";
    }
}
