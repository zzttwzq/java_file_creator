package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Dev_alarm;
import java.util.Map;

public class Dev_alarmProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,snno,method,alarmnumber,create_at,update_at,delete_at from dev_alarm limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,snno,method,alarmnumber,create_at,update_at,delete_at from dev_alarm where dev_alarm.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_alarm where id = #{id}";
    }

    public String insertOne(Dev_alarm dev_alarm) {

        String key = "";
        String value = "";
        if (dev_alarm.getId() != null && dev_alarm.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_alarm.getSnno() != null && !dev_alarm.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (dev_alarm.getMethod() != null && !dev_alarm.getMethod().isEmpty()) {
           key += "method,";
           value += "#{method},";
        }

        if (dev_alarm.getAlarmnumber() != null && !dev_alarm.getAlarmnumber().isEmpty()) {
           key += "alarmnumber,";
           value += "#{alarmnumber},";
        }

        if (dev_alarm.getCreate_at() != null && dev_alarm.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_alarm.getUpdate_at() != null && dev_alarm.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_alarm.getDelete_at() != null && dev_alarm.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_alarm (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_alarm dev_alarm) {

        String sql = "";
        if (dev_alarm.getId() != null && dev_alarm.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_alarm.getSnno() != null && !dev_alarm.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (dev_alarm.getMethod() != null && !dev_alarm.getMethod().isEmpty()) {
           sql += "method = #{method},";
        }

        if (dev_alarm.getAlarmnumber() != null && !dev_alarm.getAlarmnumber().isEmpty()) {
           sql += "alarmnumber = #{alarmnumber},";
        }

        if (dev_alarm.getCreate_at() != null && dev_alarm.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_alarm.getUpdate_at() != null && dev_alarm.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_alarm.getDelete_at() != null && dev_alarm.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_alarm set " + sql + " where id = #{id}";
    }
}
