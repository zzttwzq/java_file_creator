package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.City;
import java.util.Map;

public class CityProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,code,province_code,name,create_at,update_at,delete_at from city limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,code,province_code,name,create_at,update_at,delete_at from city where city.id=#{id}";
    }

    public String deleteOne() {

        return "delete from city where id = #{id}";
    }

    public String insertOne(City city) {

        String key = "";
        String value = "";
        if (city.getId() != null && city.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (city.getCode() != null && city.getCode() > 0) {
           key += "code,";
           value += "#{code},";
        }

        if (city.getProvince_code() != null && city.getProvince_code() > 0) {
           key += "province_code,";
           value += "#{province_code},";
        }

        if (city.getName() != null && !city.getName().isEmpty()) {
           key += "name,";
           value += "#{name},";
        }

        if (city.getCreate_at() != null && city.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (city.getUpdate_at() != null && city.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (city.getDelete_at() != null && city.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into city (" + key + ") values (" + value + ")";
    }

    public String updateOne(City city) {

        String sql = "";
        if (city.getId() != null && city.getId() > 0) {
           sql += "id = #{id},";
        }

        if (city.getCode() != null && city.getCode() > 0) {
           sql += "code = #{code},";
        }

        if (city.getProvince_code() != null && city.getProvince_code() > 0) {
           sql += "province_code = #{province_code},";
        }

        if (city.getName() != null && !city.getName().isEmpty()) {
           sql += "name = #{name},";
        }

        if (city.getCreate_at() != null && city.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (city.getUpdate_at() != null && city.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (city.getDelete_at() != null && city.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update city set " + sql + " where id = #{id}";
    }
}
