package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Mp_link;
import java.util.Map;

public class Mp_linkProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,parent_admin_id,area_id,mp_id,status,create_at,update_at,delete_at from mp_link limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,parent_admin_id,area_id,mp_id,status,create_at,update_at,delete_at from mp_link where mp_link.id=#{id}";
    }

    public String deleteOne() {

        return "delete from mp_link where id = #{id}";
    }

    public String insertOne(Mp_link mp_link) {

        String key = "";
        String value = "";
        if (mp_link.getId() != null && mp_link.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (mp_link.getParent_admin_id() != null && mp_link.getParent_admin_id() > 0) {
           key += "parent_admin_id,";
           value += "#{parent_admin_id},";
        }

        if (mp_link.getArea_id() != null && mp_link.getArea_id() > 0) {
           key += "area_id,";
           value += "#{area_id},";
        }

        if (mp_link.getMp_id() != null && mp_link.getMp_id() > 0) {
           key += "mp_id,";
           value += "#{mp_id},";
        }

        if (mp_link.getStatus() != null && mp_link.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (mp_link.getCreate_at() != null && mp_link.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (mp_link.getUpdate_at() != null && mp_link.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (mp_link.getDelete_at() != null && mp_link.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into mp_link (" + key + ") values (" + value + ")";
    }

    public String updateOne(Mp_link mp_link) {

        String sql = "";
        if (mp_link.getId() != null && mp_link.getId() > 0) {
           sql += "id = #{id},";
        }

        if (mp_link.getParent_admin_id() != null && mp_link.getParent_admin_id() > 0) {
           sql += "parent_admin_id = #{parent_admin_id},";
        }

        if (mp_link.getArea_id() != null && mp_link.getArea_id() > 0) {
           sql += "area_id = #{area_id},";
        }

        if (mp_link.getMp_id() != null && mp_link.getMp_id() > 0) {
           sql += "mp_id = #{mp_id},";
        }

        if (mp_link.getStatus() != null && mp_link.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (mp_link.getCreate_at() != null && mp_link.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (mp_link.getUpdate_at() != null && mp_link.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (mp_link.getDelete_at() != null && mp_link.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update mp_link set " + sql + " where id = #{id}";
    }
}
