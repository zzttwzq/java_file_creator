package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Section;
import java.util.Map;

public class SectionProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,code,city_code,name,create_at,update_at,delete_at from section limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,code,city_code,name,create_at,update_at,delete_at from section where section.id=#{id}";
    }

    public String deleteOne() {

        return "delete from section where id = #{id}";
    }

    public String insertOne(Section section) {

        String key = "";
        String value = "";
        if (section.getId() != null && section.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (section.getCode() != null && section.getCode() > 0) {
           key += "code,";
           value += "#{code},";
        }

        if (section.getCity_code() != null && section.getCity_code() > 0) {
           key += "city_code,";
           value += "#{city_code},";
        }

        if (section.getName() != null && !section.getName().isEmpty()) {
           key += "name,";
           value += "#{name},";
        }

        if (section.getCreate_at() != null && section.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (section.getUpdate_at() != null && section.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (section.getDelete_at() != null && section.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into section (" + key + ") values (" + value + ")";
    }

    public String updateOne(Section section) {

        String sql = "";
        if (section.getId() != null && section.getId() > 0) {
           sql += "id = #{id},";
        }

        if (section.getCode() != null && section.getCode() > 0) {
           sql += "code = #{code},";
        }

        if (section.getCity_code() != null && section.getCity_code() > 0) {
           sql += "city_code = #{city_code},";
        }

        if (section.getName() != null && !section.getName().isEmpty()) {
           sql += "name = #{name},";
        }

        if (section.getCreate_at() != null && section.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (section.getUpdate_at() != null && section.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (section.getDelete_at() != null && section.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update section set " + sql + " where id = #{id}";
    }
}
