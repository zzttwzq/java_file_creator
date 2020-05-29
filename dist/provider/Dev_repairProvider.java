package .provider;

import com.smartwc.qlzw.com.utils.Pager;
import .model.Dev_repair;
import java.util.Map;

public class Dev_repairProvider {

    public String selectAll(Map<String, Object> parm) {

        return "select id,title,content,err_type,images,dev_info,phone,position,address,admin_user_id,status,time_out,create_at,update_at,delete_at from dev_repair limit #{page},#{size}";
    }

    public String selectOne() {

        return "select id,title,content,err_type,images,dev_info,phone,position,address,admin_user_id,status,time_out,create_at,update_at,delete_at from dev_repair where dev_repair.id=#{id}";
    }

    public String deleteOne() {

        return "delete from dev_repair where id = #{id}";
    }

    public String insertOne(Dev_repair dev_repair) {

        String key = "";
        String value = "";
        if (dev_repair.getId() != null && dev_repair.getId() > 0) {
           key += "id,";
           value += "#{id},";
        }

        if (dev_repair.getTitle() != null && !dev_repair.getTitle().isEmpty()) {
           key += "title,";
           value += "#{title},";
        }

        if (dev_repair.getContent() != null && !dev_repair.getContent().isEmpty()) {
           key += "content,";
           value += "#{content},";
        }

        if (dev_repair.getErr_type() != null && dev_repair.getErr_type() > 0) {
           key += "err_type,";
           value += "#{err_type},";
        }

        if (dev_repair.getImages() != null && !dev_repair.getImages().isEmpty()) {
           key += "images,";
           value += "#{images},";
        }

        if (dev_repair.getDev_info() != null && !dev_repair.getDev_info().isEmpty()) {
           key += "dev_info,";
           value += "#{dev_info},";
        }

        if (dev_repair.getPhone() != null && !dev_repair.getPhone().isEmpty()) {
           key += "phone,";
           value += "#{phone},";
        }

        if (dev_repair.getPosition() != null && !dev_repair.getPosition().isEmpty()) {
           key += "position,";
           value += "#{position},";
        }

        if (dev_repair.getAddress() != null && !dev_repair.getAddress().isEmpty()) {
           key += "address,";
           value += "#{address},";
        }

        if (dev_repair.getAdmin_user_id() != null && dev_repair.getAdmin_user_id() > 0) {
           key += "admin_user_id,";
           value += "#{admin_user_id},";
        }

        if (dev_repair.getStatus() != null && dev_repair.getStatus() > 0) {
           key += "status,";
           value += "#{status},";
        }

        if (dev_repair.getTime_out() != null && dev_repair.getTime_out() > 0) {
           key += "time_out,";
           value += "#{time_out},";
        }

        if (dev_repair.getCreate_at() != null && dev_repair.getCreate_at() > 0) {
           key += "create_at,";
           value += "#{create_at},";
        }

        if (dev_repair.getUpdate_at() != null && dev_repair.getUpdate_at() > 0) {
           key += "update_at,";
           value += "#{update_at},";
        }

        if (dev_repair.getDelete_at() != null && dev_repair.getDelete_at() > 0) {
           key += "delete_at,";
           value += "#{delete_at},";
        }

        key = key.substring(0,key.length()-1);
        value = value.substring(0,value.length()-1);

        return "insert into dev_repair (" + key + ") values (" + value + ")";
    }

    public String updateOne(Dev_repair dev_repair) {

        String sql = "";
        if (dev_repair.getId() != null && dev_repair.getId() > 0) {
           sql += "id = #{id},";
        }

        if (dev_repair.getTitle() != null && !dev_repair.getTitle().isEmpty()) {
           sql += "title = #{title},";
        }

        if (dev_repair.getContent() != null && !dev_repair.getContent().isEmpty()) {
           sql += "content = #{content},";
        }

        if (dev_repair.getErr_type() != null && dev_repair.getErr_type() > 0) {
           sql += "err_type = #{err_type},";
        }

        if (dev_repair.getImages() != null && !dev_repair.getImages().isEmpty()) {
           sql += "images = #{images},";
        }

        if (dev_repair.getDev_info() != null && !dev_repair.getDev_info().isEmpty()) {
           sql += "dev_info = #{dev_info},";
        }

        if (dev_repair.getPhone() != null && !dev_repair.getPhone().isEmpty()) {
           sql += "phone = #{phone},";
        }

        if (dev_repair.getPosition() != null && !dev_repair.getPosition().isEmpty()) {
           sql += "position = #{position},";
        }

        if (dev_repair.getAddress() != null && !dev_repair.getAddress().isEmpty()) {
           sql += "address = #{address},";
        }

        if (dev_repair.getAdmin_user_id() != null && dev_repair.getAdmin_user_id() > 0) {
           sql += "admin_user_id = #{admin_user_id},";
        }

        if (dev_repair.getStatus() != null && dev_repair.getStatus() > 0) {
           sql += "status = #{status},";
        }

        if (dev_repair.getTime_out() != null && dev_repair.getTime_out() > 0) {
           sql += "time_out = #{time_out},";
        }

        if (dev_repair.getCreate_at() != null && dev_repair.getCreate_at() > 0) {
           sql += "create_at = #{create_at},";
        }

        if (dev_repair.getUpdate_at() != null && dev_repair.getUpdate_at() > 0) {
           sql += "update_at = #{update_at},";
        }

        if (dev_repair.getDelete_at() != null && dev_repair.getDelete_at() > 0) {
           sql += "delete_at = #{delete_at},";
        }

        sql = sql.substring(0,sql.length()-1);

        return "update dev_repair set " + sql + " where id = #{id}";
    }
}
