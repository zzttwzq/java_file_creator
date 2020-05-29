package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Api_link;
import java.util.Map;

public class Api_linkProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,user_id,api_id,create_at,update_at,delete_at from api_link limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,user_id,api_id,create_at,update_at,delete_at from api_link where api_link.id=#{id}";
    }

    public String deleteOne() {

        return "delete from api_link where id = #{id}";
    }

    public String insertOne(Api_link api_link) {

        String key = "";
        String value = "";
        if (api_link.getId() != null && api_link.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (api_link.getUser_id() != null && api_link.getUser_id() > 0) {
           key += "user_id,";
           value += "#{user_id},";
        }

        if (api_link.getApi_id() != null && api_link.getApi_id() > 0) {
           key += "api_id,";
           value += "#{api_id},";
        }

        if (api_link.getCreate_at() != null && api_link.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (api_link.getUpdate_at() != null && api_link.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (api_link.getDelete_at() != null && api_link.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into api_link (" + key + ") values (" + value + ")";
    }

    public String updateOne(Api_link api_link) {

        String sql = "";
        if (api_link.getId() != null && api_link.getId() > 0) {
           sql += "id = #{id},";
        }

        if (api_link.getUser_id() != null && api_link.getUser_id() > 0) {
           sql += "user_id = #{user_id},";
        }

        if (api_link.getApi_id() != null && api_link.getApi_id() > 0) {
           sql += "api_id = #{api_id},";
        }

        if (api_link.getCreate_at() != null && api_link.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (api_link.getUpdate_at() != null && api_link.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (api_link.getDelete_at() != null && api_link.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update api_link set " + sql + " where id = #{id}";
    }
}
