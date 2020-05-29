package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Dev_cmd;
import java.util.Map;

public class Dev_cmdProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,snno,method,params,ischecked,isouttime,create_at,update_at,delete_at from dev_cmd limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,snno,method,params,ischecked,isouttime,create_at,update_at,delete_at from dev_cmd where dev_cmd.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_cmd where id = #{id}";
    }

    public String insertOne(Dev_cmd dev_cmd) {

        String key = "";
        String value = "";
        if (dev_cmd.getId() != null && dev_cmd.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_cmd.getSnno() != null && !dev_cmd.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (dev_cmd.getMethod() != null && !dev_cmd.getMethod().isEmpty()) {
           key += "method,";
           value += "#{method},";
        }

        if (dev_cmd.getParams() != null && !dev_cmd.getParams().isEmpty()) {
           key += "params,";
           value += "#{params},";
        }

        if (dev_cmd.getIschecked() != null && dev_cmd.getIschecked() > 0) {
           key += "ischecked,";
           value += "#{ischecked},";
        }

        if (dev_cmd.getIsouttime() != null && dev_cmd.getIsouttime() > 0) {
           key += "isouttime,";
           value += "#{isouttime},";
        }

        if (dev_cmd.getCreate_at() != null && dev_cmd.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_cmd.getUpdate_at() != null && dev_cmd.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_cmd.getDelete_at() != null && dev_cmd.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_cmd (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_cmd dev_cmd) {

        String sql = "";
        if (dev_cmd.getId() != null && dev_cmd.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_cmd.getSnno() != null && !dev_cmd.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (dev_cmd.getMethod() != null && !dev_cmd.getMethod().isEmpty()) {
           sql += "method = #{method},";
        }

        if (dev_cmd.getParams() != null && !dev_cmd.getParams().isEmpty()) {
           sql += "params = #{params},";
        }

        if (dev_cmd.getIschecked() != null && dev_cmd.getIschecked() > 0) {
           sql += "ischecked = #{ischecked},";
        }

        if (dev_cmd.getIsouttime() != null && dev_cmd.getIsouttime() > 0) {
           sql += "isouttime = #{isouttime},";
        }

        if (dev_cmd.getCreate_at() != null && dev_cmd.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_cmd.getUpdate_at() != null && dev_cmd.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_cmd.getDelete_at() != null && dev_cmd.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_cmd set " + sql + " where id = #{id}";
    }
}
