package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Province;
import java.util.Map;

public class ProvinceProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,code,name,create_at,update_at,delete_at from province limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,code,name,create_at,update_at,delete_at from province where province.id=#{id}";
    }

    public String deleteOne() {

        return "delete from province where id = #{id}";
    }

    public String insertOne(Province province) {

        String key = "";
        String value = "";
        if (province.getId() != null && province.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (province.getCode() != null && province.getCode() > 0) {
           key += "code,";
           value += "#{code},";
        }

        if (province.getName() != null && !province.getName().isEmpty()) {
           key += "name,";
           value += "#{name},";
        }

        if (province.getCreate_at() != null && province.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (province.getUpdate_at() != null && province.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (province.getDelete_at() != null && province.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into province (" + key + ") values (" + value + ")";
    }

    public String updateOne(Province province) {

        String sql = "";
        if (province.getId() != null && province.getId() > 0) {
           sql += "id = #{id},";
        }

        if (province.getCode() != null && province.getCode() > 0) {
           sql += "code = #{code},";
        }

        if (province.getName() != null && !province.getName().isEmpty()) {
           sql += "name = #{name},";
        }

        if (province.getCreate_at() != null && province.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (province.getUpdate_at() != null && province.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (province.getDelete_at() != null && province.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update province set " + sql + " where id = #{id}";
    }
}
