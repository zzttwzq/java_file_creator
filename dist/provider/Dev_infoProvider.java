package com.qlzw.smartwc.provider;

import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.model.Dev_info;
import java.util.Map;

public class Dev_infoProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,dev_id,last_time,status,snno,ccid,rfid,proportion,temperature,humidity,nh3,dayon,dayoff,nighton,nightoff,addwaternum,addwatertime,atomizerpwm,fanmin,fanmax,totaladdwater,alarmnumber,rfid_status,hrev,srev,create_at,update_at,delete_at from dev_info limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,dev_id,last_time,status,snno,ccid,rfid,proportion,temperature,humidity,nh3,dayon,dayoff,nighton,nightoff,addwaternum,addwatertime,atomizerpwm,fanmin,fanmax,totaladdwater,alarmnumber,rfid_status,hrev,srev,create_at,update_at,delete_at from dev_info where dev_info.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_info where id = #{id}";
    }

    public String insertOne(Dev_info dev_info) {

        String key = "";
        String value = "";
        if (dev_info.getId() != null && dev_info.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_info.getDev_id() != null && dev_info.getDev_id() > 0) {
           key += "dev_id,";
           value += "#{dev_id},";
        }

        if (dev_info.getLast_time() != null && dev_info.getLast_time() > 0) {
           key += "last_time,";
           value += "#{last_time},";
        }

        if (dev_info.getStatus() != null && dev_info.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (dev_info.getSnno() != null && !dev_info.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (dev_info.getCcid() != null && !dev_info.getCcid().isEmpty()) {
           key += "ccid,";
           value += "#{ccid},";
        }

        if (dev_info.getRfid() != null && !dev_info.getRfid().isEmpty()) {
           key += "rfid,";
           value += "#{rfid},";
        }

        if (dev_info.getProportion() != null && !dev_info.getProportion().isEmpty()) {
           key += "proportion,";
           value += "#{proportion},";
        }

        if (dev_info.getTemperature() != null && dev_info.getTemperature() > 0) {
           key += "temperature,";
           value += "#{temperature},";
        }

        if (dev_info.getHumidity() != null && dev_info.getHumidity() > 0) {
           key += "humidity,";
           value += "#{humidity},";
        }

        if (dev_info.getNh3() != null && dev_info.getNh3() > 0) {
           key += "nh3,";
           value += "#{nh3},";
        }

        if (dev_info.getDayon() != null && dev_info.getDayon() > 0) {
           key += "dayon,";
           value += "#{dayon},";
        }

        if (dev_info.getDayoff() != null && dev_info.getDayoff() > 0) {
           key += "dayoff,";
           value += "#{dayoff},";
        }

        if (dev_info.getNighton() != null && dev_info.getNighton() > 0) {
           key += "nighton,";
           value += "#{nighton},";
        }

        if (dev_info.getNightoff() != null && dev_info.getNightoff() > 0) {
           key += "nightoff,";
           value += "#{nightoff},";
        }

        if (dev_info.getAddwaternum() != null && dev_info.getAddwaternum() > 0) {
           key += "addwaternum,";
           value += "#{addwaternum},";
        }

        if (dev_info.getAddwatertime() != null && dev_info.getAddwatertime() > 0) {
           key += "addwatertime,";
           value += "#{addwatertime},";
        }

        if (dev_info.getAtomizerpwm() != null && dev_info.getAtomizerpwm() > 0) {
           key += "atomizerpwm,";
           value += "#{atomizerpwm},";
        }

        if (dev_info.getFanmin() != null && dev_info.getFanmin() > 0) {
           key += "fanmin,";
           value += "#{fanmin},";
        }

        if (dev_info.getFanmax() != null && dev_info.getFanmax() > 0) {
           key += "fanmax,";
           value += "#{fanmax},";
        }

        if (dev_info.getTotaladdwater() != null && dev_info.getTotaladdwater() > 0) {
           key += "totaladdwater,";
           value += "#{totaladdwater},";
        }

        if (dev_info.getAlarmnumber() != null && !dev_info.getAlarmnumber().isEmpty()) {
           key += "alarmnumber,";
           value += "#{alarmnumber},";
        }

        if (dev_info.getRfid_status() != null && !dev_info.getRfid_status().isEmpty()) {
           key += "rfid_status,";
           value += "#{rfid_status},";
        }

        if (dev_info.getHrev() != null && !dev_info.getHrev().isEmpty()) {
           key += "hrev,";
           value += "#{hrev},";
        }

        if (dev_info.getSrev() != null && !dev_info.getSrev().isEmpty()) {
           key += "srev,";
           value += "#{srev},";
        }

        if (dev_info.getCreate_at() != null && dev_info.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_info.getUpdate_at() != null && dev_info.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_info.getDelete_at() != null && dev_info.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_info (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_info dev_info) {

        String sql = "";
        if (dev_info.getId() != null && dev_info.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_info.getDev_id() != null && dev_info.getDev_id() > 0) {
           sql += "dev_id = #{dev_id},";
        }

        if (dev_info.getLast_time() != null && dev_info.getLast_time() > 0) {
           sql += "last_time = #{last_time},";
        }

        if (dev_info.getStatus() != null && dev_info.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (dev_info.getSnno() != null && !dev_info.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (dev_info.getCcid() != null && !dev_info.getCcid().isEmpty()) {
           sql += "ccid = #{ccid},";
        }

        if (dev_info.getRfid() != null && !dev_info.getRfid().isEmpty()) {
           sql += "rfid = #{rfid},";
        }

        if (dev_info.getProportion() != null && !dev_info.getProportion().isEmpty()) {
           sql += "proportion = #{proportion},";
        }

        if (dev_info.getTemperature() != null && dev_info.getTemperature() > 0) {
           sql += "temperature = #{temperature},";
        }

        if (dev_info.getHumidity() != null && dev_info.getHumidity() > 0) {
           sql += "humidity = #{humidity},";
        }

        if (dev_info.getNh3() != null && dev_info.getNh3() > 0) {
           sql += "nh3 = #{nh3},";
        }

        if (dev_info.getDayon() != null && dev_info.getDayon() > 0) {
           sql += "dayon = #{dayon},";
        }

        if (dev_info.getDayoff() != null && dev_info.getDayoff() > 0) {
           sql += "dayoff = #{dayoff},";
        }

        if (dev_info.getNighton() != null && dev_info.getNighton() > 0) {
           sql += "nighton = #{nighton},";
        }

        if (dev_info.getNightoff() != null && dev_info.getNightoff() > 0) {
           sql += "nightoff = #{nightoff},";
        }

        if (dev_info.getAddwaternum() != null && dev_info.getAddwaternum() > 0) {
           sql += "addwaternum = #{addwaternum},";
        }

        if (dev_info.getAddwatertime() != null && dev_info.getAddwatertime() > 0) {
           sql += "addwatertime = #{addwatertime},";
        }

        if (dev_info.getAtomizerpwm() != null && dev_info.getAtomizerpwm() > 0) {
           sql += "atomizerpwm = #{atomizerpwm},";
        }

        if (dev_info.getFanmin() != null && dev_info.getFanmin() > 0) {
           sql += "fanmin = #{fanmin},";
        }

        if (dev_info.getFanmax() != null && dev_info.getFanmax() > 0) {
           sql += "fanmax = #{fanmax},";
        }

        if (dev_info.getTotaladdwater() != null && dev_info.getTotaladdwater() > 0) {
           sql += "totaladdwater = #{totaladdwater},";
        }

        if (dev_info.getAlarmnumber() != null && !dev_info.getAlarmnumber().isEmpty()) {
           sql += "alarmnumber = #{alarmnumber},";
        }

        if (dev_info.getRfid_status() != null && !dev_info.getRfid_status().isEmpty()) {
           sql += "rfid_status = #{rfid_status},";
        }

        if (dev_info.getHrev() != null && !dev_info.getHrev().isEmpty()) {
           sql += "hrev = #{hrev},";
        }

        if (dev_info.getSrev() != null && !dev_info.getSrev().isEmpty()) {
           sql += "srev = #{srev},";
        }

        if (dev_info.getCreate_at() != null && dev_info.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_info.getUpdate_at() != null && dev_info.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_info.getDelete_at() != null && dev_info.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_info set " + sql + " where id = #{id}";
    }
}
