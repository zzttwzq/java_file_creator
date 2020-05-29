package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Dev_answer;
import java.util.Map;

public class Dev_answerProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,title,cause,tips,create_at,update_at,delete_at from dev_answer limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,title,cause,tips,create_at,update_at,delete_at from dev_answer where dev_answer.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_answer where id = #{id}";
    }

    public String insertOne(Dev_answer dev_answer) {

        String key = "";
        String value = "";
        if (dev_answer.getId() != null && dev_answer.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_answer.getTitle() != null && !dev_answer.getTitle().isEmpty()) {
           key += "title,";
           value += "#{title},";
        }

        if (dev_answer.getCause() != null && !dev_answer.getCause().isEmpty()) {
           key += "cause,";
           value += "#{cause},";
        }

        if (dev_answer.getTips() != null && !dev_answer.getTips().isEmpty()) {
           key += "tips,";
           value += "#{tips},";
        }

        if (dev_answer.getCreate_at() != null && dev_answer.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_answer.getUpdate_at() != null && dev_answer.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_answer.getDelete_at() != null && dev_answer.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_answer (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_answer dev_answer) {

        String sql = "";
        if (dev_answer.getId() != null && dev_answer.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_answer.getTitle() != null && !dev_answer.getTitle().isEmpty()) {
           sql += "title = #{title},";
        }

        if (dev_answer.getCause() != null && !dev_answer.getCause().isEmpty()) {
           sql += "cause = #{cause},";
        }

        if (dev_answer.getTips() != null && !dev_answer.getTips().isEmpty()) {
           sql += "tips = #{tips},";
        }

        if (dev_answer.getCreate_at() != null && dev_answer.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_answer.getUpdate_at() != null && dev_answer.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_answer.getDelete_at() != null && dev_answer.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_answer set " + sql + " where id = #{id}";
    }
}
