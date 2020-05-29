package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Dev;
import java.util.Map;

public class DevProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,name,snno,position,address,dev_info_id,rfid_id,create_at,update_at,delete_at from dev limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,name,snno,position,address,dev_info_id,rfid_id,create_at,update_at,delete_at from dev where dev.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev where id = #{id}";
    }

    public String insertOne(Dev dev) {

        String key = "";
        String value = "";
        if (dev.getId() != null && dev.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev.getName() != null && !dev.getName().isEmpty()) {
           key += "name,";
           value += "#{name},";
        }

        if (dev.getSnno() != null && !dev.getSnno().isEmpty()) {
           key += "snno,";
           value += "#{snno},";
        }

        if (dev.getPosition() != null && !dev.getPosition().isEmpty()) {
           key += "position,";
           value += "#{position},";
        }

        if (dev.getAddress() != null && !dev.getAddress().isEmpty()) {
           key += "address,";
           value += "#{address},";
        }

        if (dev.getDev_info_id() != null && dev.getDev_info_id() > 0) {
           key += "dev_info_id,";
           value += "#{dev_info_id},";
        }

        if (dev.getRfid_id() != null && dev.getRfid_id() > 0) {
           key += "rfid_id,";
           value += "#{rfid_id},";
        }

        if (dev.getCreate_at() != null && dev.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev.getUpdate_at() != null && dev.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev.getDelete_at() != null && dev.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev dev) {

        String sql = "";
        if (dev.getId() != null && dev.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev.getName() != null && !dev.getName().isEmpty()) {
           sql += "name = #{name},";
        }

        if (dev.getSnno() != null && !dev.getSnno().isEmpty()) {
           sql += "snno = #{snno},";
        }

        if (dev.getPosition() != null && !dev.getPosition().isEmpty()) {
           sql += "position = #{position},";
        }

        if (dev.getAddress() != null && !dev.getAddress().isEmpty()) {
           sql += "address = #{address},";
        }

        if (dev.getDev_info_id() != null && dev.getDev_info_id() > 0) {
           sql += "dev_info_id = #{dev_info_id},";
        }

        if (dev.getRfid_id() != null && dev.getRfid_id() > 0) {
           sql += "rfid_id = #{rfid_id},";
        }

        if (dev.getCreate_at() != null && dev.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev.getUpdate_at() != null && dev.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev.getDelete_at() != null && dev.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev set " + sql + " where id = #{id}";
    }
}
