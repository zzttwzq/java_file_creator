package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Mp_user_share;
import java.util.Map;

public class Mp_user_shareProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,mp_user_id,title,data_id,type,create_at,update_at,delete_at from mp_user_share limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,mp_user_id,title,data_id,type,create_at,update_at,delete_at from mp_user_share where mp_user_share.id=#{id}";
    }

    public String deleteOne() {

        return "delete from mp_user_share where id = #{id}";
    }

    public String insertOne(Mp_user_share mp_user_share) {

        String key = "";
        String value = "";
        if (mp_user_share.getId() != null && mp_user_share.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (mp_user_share.getMp_user_id() != null && mp_user_share.getMp_user_id() > 0) {
           key += "mp_user_id,";
           value += "#{mp_user_id},";
        }

        if (mp_user_share.getTitle() != null && !mp_user_share.getTitle().isEmpty()) {
           key += "title,";
           value += "#{title},";
        }

        if (mp_user_share.getData_id() != null && mp_user_share.getData_id() > 0) {
           key += "data_id,";
           value += "#{data_id},";
        }

        if (mp_user_share.getType() != null && mp_user_share.getType() > 0) {
           key += "type,";
           value += "#{type},";
        }

        if (mp_user_share.getCreate_at() != null && mp_user_share.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (mp_user_share.getUpdate_at() != null && mp_user_share.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (mp_user_share.getDelete_at() != null && mp_user_share.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into mp_user_share (" + key + ") values (" + value + ")";
    }

    public String updateOne(Mp_user_share mp_user_share) {

        String sql = "";
        if (mp_user_share.getId() != null && mp_user_share.getId() > 0) {
           sql += "id = #{id},";
        }

        if (mp_user_share.getMp_user_id() != null && mp_user_share.getMp_user_id() > 0) {
           sql += "mp_user_id = #{mp_user_id},";
        }

        if (mp_user_share.getTitle() != null && !mp_user_share.getTitle().isEmpty()) {
           sql += "title = #{title},";
        }

        if (mp_user_share.getData_id() != null && mp_user_share.getData_id() > 0) {
           sql += "data_id = #{data_id},";
        }

        if (mp_user_share.getType() != null && mp_user_share.getType() > 0) {
           sql += "type = #{type},";
        }

        if (mp_user_share.getCreate_at() != null && mp_user_share.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (mp_user_share.getUpdate_at() != null && mp_user_share.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (mp_user_share.getDelete_at() != null && mp_user_share.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update mp_user_share set " + sql + " where id = #{id}";
    }
}
