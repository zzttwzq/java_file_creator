package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Dev_msg;
import java.util.Map;

public class Dev_msgProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,dev_id,last_time,status,snno,ccid,rfid,proportion,temperature,humidity,nh3,dayon,dayoff,nighton,nightoff,addwaternum,addwatertime,atomizerpwm,fanmin,fanmax,totaladdwater,hrev,srev,create_at,update_at,delete_at from dev_msg limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,dev_id,last_time,status,snno,ccid,rfid,proportion,temperature,humidity,nh3,dayon,dayoff,nighton,nightoff,addwaternum,addwatertime,atomizerpwm,fanmin,fanmax,totaladdwater,hrev,srev,create_at,update_at,delete_at from dev_msg where dev_msg.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_msg where id = #{id}";
    }

    public String insertOne(Dev_msg dev_msg) {

        String key = "";
        String value = "";
        if (dev_msg.getId() != null && dev_msg.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_msg.getDev_id() != null && dev_msg.getDev_id() > 0) {
           key += "dev_id,";
           value += "#{dev_id},";
        }

        if (dev_msg.getLast_time() != null && dev_msg.getLast_time() > 0) {
           key += "last_time,";
           value += "#{last_time},";
        }

        if (dev_msg.getStatus() != null && dev_msg.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (dev_msg.getSnno() != null && !dev_msg.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (dev_msg.getCcid() != null && !dev_msg.getCcid().isEmpty()) {
           key += "ccid,";
           value += "#{ccid},";
        }

        if (dev_msg.getRfid() != null && !dev_msg.getRfid().isEmpty()) {
           key += "rfid,";
           value += "#{rfid},";
        }

        if (dev_msg.getProportion() != null && !dev_msg.getProportion().isEmpty()) {
           key += "proportion,";
           value += "#{proportion},";
        }

        if (dev_msg.getTemperature() != null && dev_msg.getTemperature() > 0) {
           key += "temperature,";
           value += "#{temperature},";
        }

        if (dev_msg.getHumidity() != null && dev_msg.getHumidity() > 0) {
           key += "humidity,";
           value += "#{humidity},";
        }

        if (dev_msg.getNh3() != null && dev_msg.getNh3() > 0) {
           key += "nh3,";
           value += "#{nh3},";
        }

        if (dev_msg.getDayon() != null && dev_msg.getDayon() > 0) {
           key += "dayon,";
           value += "#{dayon},";
        }

        if (dev_msg.getDayoff() != null && dev_msg.getDayoff() > 0) {
           key += "dayoff,";
           value += "#{dayoff},";
        }

        if (dev_msg.getNighton() != null && dev_msg.getNighton() > 0) {
           key += "nighton,";
           value += "#{nighton},";
        }

        if (dev_msg.getNightoff() != null && dev_msg.getNightoff() > 0) {
           key += "nightoff,";
           value += "#{nightoff},";
        }

        if (dev_msg.getAddwaternum() != null && dev_msg.getAddwaternum() > 0) {
           key += "addwaternum,";
           value += "#{addwaternum},";
        }

        if (dev_msg.getAddwatertime() != null && dev_msg.getAddwatertime() > 0) {
           key += "addwatertime,";
           value += "#{addwatertime},";
        }

        if (dev_msg.getAtomizerpwm() != null && dev_msg.getAtomizerpwm() > 0) {
           key += "atomizerpwm,";
           value += "#{atomizerpwm},";
        }

        if (dev_msg.getFanmin() != null && dev_msg.getFanmin() > 0) {
           key += "fanmin,";
           value += "#{fanmin},";
        }

        if (dev_msg.getFanmax() != null && dev_msg.getFanmax() > 0) {
           key += "fanmax,";
           value += "#{fanmax},";
        }

        if (dev_msg.getTotaladdwater() != null && dev_msg.getTotaladdwater() > 0) {
           key += "totaladdwater,";
           value += "#{totaladdwater},";
        }

        if (dev_msg.getHrev() != null && !dev_msg.getHrev().isEmpty()) {
           key += "hrev,";
           value += "#{hrev},";
        }

        if (dev_msg.getSrev() != null && !dev_msg.getSrev().isEmpty()) {
           key += "srev,";
           value += "#{srev},";
        }

        if (dev_msg.getCreate_at() != null && dev_msg.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_msg.getUpdate_at() != null && dev_msg.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_msg.getDelete_at() != null && dev_msg.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_msg (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_msg dev_msg) {

        String sql = "";
        if (dev_msg.getId() != null && dev_msg.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_msg.getDev_id() != null && dev_msg.getDev_id() > 0) {
           sql += "dev_id = #{dev_id},";
        }

        if (dev_msg.getLast_time() != null && dev_msg.getLast_time() > 0) {
           sql += "last_time = #{last_time},";
        }

        if (dev_msg.getStatus() != null && dev_msg.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (dev_msg.getSnno() != null && !dev_msg.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (dev_msg.getCcid() != null && !dev_msg.getCcid().isEmpty()) {
           sql += "ccid = #{ccid},";
        }

        if (dev_msg.getRfid() != null && !dev_msg.getRfid().isEmpty()) {
           sql += "rfid = #{rfid},";
        }

        if (dev_msg.getProportion() != null && !dev_msg.getProportion().isEmpty()) {
           sql += "proportion = #{proportion},";
        }

        if (dev_msg.getTemperature() != null && dev_msg.getTemperature() > 0) {
           sql += "temperature = #{temperature},";
        }

        if (dev_msg.getHumidity() != null && dev_msg.getHumidity() > 0) {
           sql += "humidity = #{humidity},";
        }

        if (dev_msg.getNh3() != null && dev_msg.getNh3() > 0) {
           sql += "nh3 = #{nh3},";
        }

        if (dev_msg.getDayon() != null && dev_msg.getDayon() > 0) {
           sql += "dayon = #{dayon},";
        }

        if (dev_msg.getDayoff() != null && dev_msg.getDayoff() > 0) {
           sql += "dayoff = #{dayoff},";
        }

        if (dev_msg.getNighton() != null && dev_msg.getNighton() > 0) {
           sql += "nighton = #{nighton},";
        }

        if (dev_msg.getNightoff() != null && dev_msg.getNightoff() > 0) {
           sql += "nightoff = #{nightoff},";
        }

        if (dev_msg.getAddwaternum() != null && dev_msg.getAddwaternum() > 0) {
           sql += "addwaternum = #{addwaternum},";
        }

        if (dev_msg.getAddwatertime() != null && dev_msg.getAddwatertime() > 0) {
           sql += "addwatertime = #{addwatertime},";
        }

        if (dev_msg.getAtomizerpwm() != null && dev_msg.getAtomizerpwm() > 0) {
           sql += "atomizerpwm = #{atomizerpwm},";
        }

        if (dev_msg.getFanmin() != null && dev_msg.getFanmin() > 0) {
           sql += "fanmin = #{fanmin},";
        }

        if (dev_msg.getFanmax() != null && dev_msg.getFanmax() > 0) {
           sql += "fanmax = #{fanmax},";
        }

        if (dev_msg.getTotaladdwater() != null && dev_msg.getTotaladdwater() > 0) {
           sql += "totaladdwater = #{totaladdwater},";
        }

        if (dev_msg.getHrev() != null && !dev_msg.getHrev().isEmpty()) {
           sql += "hrev = #{hrev},";
        }

        if (dev_msg.getSrev() != null && !dev_msg.getSrev().isEmpty()) {
           sql += "srev = #{srev},";
        }

        if (dev_msg.getCreate_at() != null && dev_msg.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_msg.getUpdate_at() != null && dev_msg.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_msg.getDelete_at() != null && dev_msg.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_msg set " + sql + " where id = #{id}";
    }
}
