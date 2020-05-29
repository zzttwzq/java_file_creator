package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Dev_action;
import java.util.Map;

public class Dev_actionProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,snno,method,proportion,temperature,humidity,nh3,dayon,dayoff,nighton,nightoff,addwaternum,addwatertime,atomizerpwm,fanmin,fanmax,addtime,totaladdwater,create_at,update_at,delete_at from dev_action limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,snno,method,proportion,temperature,humidity,nh3,dayon,dayoff,nighton,nightoff,addwaternum,addwatertime,atomizerpwm,fanmin,fanmax,addtime,totaladdwater,create_at,update_at,delete_at from dev_action where dev_action.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_action where id = #{id}";
    }

    public String insertOne(Dev_action dev_action) {

        String key = "";
        String value = "";
        if (dev_action.getId() != null && dev_action.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_action.getSnno() != null && !dev_action.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (dev_action.getMethod() != null && !dev_action.getMethod().isEmpty()) {
           key += "method,";
           value += "#{method},";
        }

        if (dev_action.getProportion() != null && !dev_action.getProportion().isEmpty()) {
           key += "proportion,";
           value += "#{proportion},";
        }

        if (dev_action.getTemperature() != null && dev_action.getTemperature() > 0) {
           key += "temperature,";
           value += "#{temperature},";
        }

        if (dev_action.getHumidity() != null && dev_action.getHumidity() > 0) {
           key += "humidity,";
           value += "#{humidity},";
        }

        if (dev_action.getNh3() != null && dev_action.getNh3() > 0) {
           key += "nh3,";
           value += "#{nh3},";
        }

        if (dev_action.getDayon() != null && dev_action.getDayon() > 0) {
           key += "dayon,";
           value += "#{dayon},";
        }

        if (dev_action.getDayoff() != null && dev_action.getDayoff() > 0) {
           key += "dayoff,";
           value += "#{dayoff},";
        }

        if (dev_action.getNighton() != null && dev_action.getNighton() > 0) {
           key += "nighton,";
           value += "#{nighton},";
        }

        if (dev_action.getNightoff() != null && dev_action.getNightoff() > 0) {
           key += "nightoff,";
           value += "#{nightoff},";
        }

        if (dev_action.getAddwaternum() != null && dev_action.getAddwaternum() > 0) {
           key += "addwaternum,";
           value += "#{addwaternum},";
        }

        if (dev_action.getAddwatertime() != null && dev_action.getAddwatertime() > 0) {
           key += "addwatertime,";
           value += "#{addwatertime},";
        }

        if (dev_action.getAtomizerpwm() != null && dev_action.getAtomizerpwm() > 0) {
           key += "atomizerpwm,";
           value += "#{atomizerpwm},";
        }

        if (dev_action.getFanmin() != null && dev_action.getFanmin() > 0) {
           key += "fanmin,";
           value += "#{fanmin},";
        }

        if (dev_action.getFanmax() != null && dev_action.getFanmax() > 0) {
           key += "fanmax,";
           value += "#{fanmax},";
        }

        if (dev_action.getAddtime() != null && dev_action.getAddtime() > 0) {
           key += "addtime,";
           value += "#{addtime},";
        }

        if (dev_action.getTotaladdwater() != null && dev_action.getTotaladdwater() > 0) {
           key += "totaladdwater,";
           value += "#{totaladdwater},";
        }

        if (dev_action.getCreate_at() != null && dev_action.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_action.getUpdate_at() != null && dev_action.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_action.getDelete_at() != null && dev_action.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_action (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_action dev_action) {

        String sql = "";
        if (dev_action.getId() != null && dev_action.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_action.getSnno() != null && !dev_action.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (dev_action.getMethod() != null && !dev_action.getMethod().isEmpty()) {
           sql += "method = #{method},";
        }

        if (dev_action.getProportion() != null && !dev_action.getProportion().isEmpty()) {
           sql += "proportion = #{proportion},";
        }

        if (dev_action.getTemperature() != null && dev_action.getTemperature() > 0) {
           sql += "temperature = #{temperature},";
        }

        if (dev_action.getHumidity() != null && dev_action.getHumidity() > 0) {
           sql += "humidity = #{humidity},";
        }

        if (dev_action.getNh3() != null && dev_action.getNh3() > 0) {
           sql += "nh3 = #{nh3},";
        }

        if (dev_action.getDayon() != null && dev_action.getDayon() > 0) {
           sql += "dayon = #{dayon},";
        }

        if (dev_action.getDayoff() != null && dev_action.getDayoff() > 0) {
           sql += "dayoff = #{dayoff},";
        }

        if (dev_action.getNighton() != null && dev_action.getNighton() > 0) {
           sql += "nighton = #{nighton},";
        }

        if (dev_action.getNightoff() != null && dev_action.getNightoff() > 0) {
           sql += "nightoff = #{nightoff},";
        }

        if (dev_action.getAddwaternum() != null && dev_action.getAddwaternum() > 0) {
           sql += "addwaternum = #{addwaternum},";
        }

        if (dev_action.getAddwatertime() != null && dev_action.getAddwatertime() > 0) {
           sql += "addwatertime = #{addwatertime},";
        }

        if (dev_action.getAtomizerpwm() != null && dev_action.getAtomizerpwm() > 0) {
           sql += "atomizerpwm = #{atomizerpwm},";
        }

        if (dev_action.getFanmin() != null && dev_action.getFanmin() > 0) {
           sql += "fanmin = #{fanmin},";
        }

        if (dev_action.getFanmax() != null && dev_action.getFanmax() > 0) {
           sql += "fanmax = #{fanmax},";
        }

        if (dev_action.getAddtime() != null && dev_action.getAddtime() > 0) {
           sql += "addtime = #{addtime},";
        }

        if (dev_action.getTotaladdwater() != null && dev_action.getTotaladdwater() > 0) {
           sql += "totaladdwater = #{totaladdwater},";
        }

        if (dev_action.getCreate_at() != null && dev_action.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_action.getUpdate_at() != null && dev_action.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_action.getDelete_at() != null && dev_action.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_action set " + sql + " where id = #{id}";
    }
}
