package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Mp_dev_link;
import java.util.Map;

public class Mp_dev_linkProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,mp_user_id,dev_id,status,create_at,update_at,delete_at from mp_dev_link limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,mp_user_id,dev_id,status,create_at,update_at,delete_at from mp_dev_link where mp_dev_link.id=#{id}";
    }

    public String deleteOne() {

        return "delete from mp_dev_link where id = #{id}";
    }

    public String insertOne(Mp_dev_link mp_dev_link) {

        String key = "";
        String value = "";
        if (mp_dev_link.getId() != null && mp_dev_link.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (mp_dev_link.getMp_user_id() != null && mp_dev_link.getMp_user_id() > 0) {
           key += "mp_user_id,";
           value += "#{mp_user_id},";
        }

        if (mp_dev_link.getDev_id() != null && mp_dev_link.getDev_id() > 0) {
           key += "dev_id,";
           value += "#{dev_id},";
        }

        if (mp_dev_link.getStatus() != null && mp_dev_link.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (mp_dev_link.getCreate_at() != null && mp_dev_link.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (mp_dev_link.getUpdate_at() != null && mp_dev_link.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (mp_dev_link.getDelete_at() != null && mp_dev_link.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into mp_dev_link (" + key + ") values (" + value + ")";
    }

    public String updateOne(Mp_dev_link mp_dev_link) {

        String sql = "";
        if (mp_dev_link.getId() != null && mp_dev_link.getId() > 0) {
           sql += "id = #{id},";
        }

        if (mp_dev_link.getMp_user_id() != null && mp_dev_link.getMp_user_id() > 0) {
           sql += "mp_user_id = #{mp_user_id},";
        }

        if (mp_dev_link.getDev_id() != null && mp_dev_link.getDev_id() > 0) {
           sql += "dev_id = #{dev_id},";
        }

        if (mp_dev_link.getStatus() != null && mp_dev_link.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (mp_dev_link.getCreate_at() != null && mp_dev_link.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (mp_dev_link.getUpdate_at() != null && mp_dev_link.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (mp_dev_link.getDelete_at() != null && mp_dev_link.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update mp_dev_link set " + sql + " where id = #{id}";
    }
}
