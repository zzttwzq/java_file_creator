package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Msg_log;
import java.util.Map;

public class Msg_logProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,snno,method,sendto,params,create_at,update_at,delete_at from msg_log limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,snno,method,sendto,params,create_at,update_at,delete_at from msg_log where msg_log.id=#{id}";
    }

    public String deleteOne() {

        return "delete from msg_log where id = #{id}";
    }

    public String insertOne(Msg_log msg_log) {

        String key = "";
        String value = "";
        if (msg_log.getId() != null && msg_log.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (msg_log.getSnno() != null && !msg_log.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (msg_log.getMethod() != null && !msg_log.getMethod().isEmpty()) {
           key += "method,";
           value += "#{method},";
        }

        if (msg_log.getSendto() != null && !msg_log.getSendto().isEmpty()) {
           key += "sendto,";
           value += "#{sendto},";
        }

        if (msg_log.getParams() != null && !msg_log.getParams().isEmpty()) {
           key += "params,";
           value += "#{params},";
        }

        if (msg_log.getCreate_at() != null && msg_log.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (msg_log.getUpdate_at() != null && msg_log.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (msg_log.getDelete_at() != null && msg_log.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into msg_log (" + key + ") values (" + value + ")";
    }

    public String updateOne(Msg_log msg_log) {

        String sql = "";
        if (msg_log.getId() != null && msg_log.getId() > 0) {
           sql += "id = #{id},";
        }

        if (msg_log.getSnno() != null && !msg_log.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (msg_log.getMethod() != null && !msg_log.getMethod().isEmpty()) {
           sql += "method = #{method},";
        }

        if (msg_log.getSendto() != null && !msg_log.getSendto().isEmpty()) {
           sql += "sendto = #{sendto},";
        }

        if (msg_log.getParams() != null && !msg_log.getParams().isEmpty()) {
           sql += "params = #{params},";
        }

        if (msg_log.getCreate_at() != null && msg_log.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (msg_log.getUpdate_at() != null && msg_log.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (msg_log.getDelete_at() != null && msg_log.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update msg_log set " + sql + " where id = #{id}";
    }
}
