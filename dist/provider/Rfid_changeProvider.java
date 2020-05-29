package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Rfid_change;
import java.util.Map;

public class Rfid_changeProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,snno,newrfid,create_at,update_at,delete_at from rfid_change limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,snno,newrfid,create_at,update_at,delete_at from rfid_change where rfid_change.id=#{id}";
    }

    public String deleteOne() {

        return "delete from rfid_change where id = #{id}";
    }

    public String insertOne(Rfid_change rfid_change) {

        String key = "";
        String value = "";
        if (rfid_change.getId() != null && rfid_change.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (rfid_change.getSnno() != null && !rfid_change.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (rfid_change.getNewrfid() != null && !rfid_change.getNewrfid().isEmpty()) {
           key += "newrfid,";
           value += "#{newrfid},";
        }

        if (rfid_change.getCreate_at() != null && rfid_change.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (rfid_change.getUpdate_at() != null && rfid_change.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (rfid_change.getDelete_at() != null && rfid_change.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into rfid_change (" + key + ") values (" + value + ")";
    }

    public String updateOne(Rfid_change rfid_change) {

        String sql = "";
        if (rfid_change.getId() != null && rfid_change.getId() > 0) {
           sql += "id = #{id},";
        }

        if (rfid_change.getSnno() != null && !rfid_change.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (rfid_change.getNewrfid() != null && !rfid_change.getNewrfid().isEmpty()) {
           sql += "newrfid = #{newrfid},";
        }

        if (rfid_change.getCreate_at() != null && rfid_change.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (rfid_change.getUpdate_at() != null && rfid_change.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (rfid_change.getDelete_at() != null && rfid_change.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update rfid_change set " + sql + " where id = #{id}";
    }
}
