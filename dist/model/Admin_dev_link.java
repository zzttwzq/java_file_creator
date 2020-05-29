package .model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Admin_dev_link {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private Integer admin_user_id; // 后台管理用户id 
    private Integer dev_id; // 设备id 
    private Integer status; // 状态 0：取消关联 1：建立关联 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Admin_dev_link(Long id,Integer admin_user_id,Integer dev_id,Integer status,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.admin_user_id=admin_user_id;
        this.dev_id=dev_id;
        this.status=status;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Admin_dev_link() {}

    public Long getId () { return this.id;}

    public Integer getAdmin_user_id () { return this.admin_user_id;}

    public Integer getDev_id () { return this.dev_id;}

    public Integer getStatus () { return this.status;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setAdmin_user_id (Integer admin_user_id) { this.admin_user_id = admin_user_id;}

    public void setDev_id (Integer dev_id) { this.dev_id = dev_id;}

    public void setStatus (Integer status) { this.status = status;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Admin_dev_link> {id = " + id + " " +
                "admin_user_id = " + admin_user_id + " " +
                "dev_id = " + dev_id + " " +
                "status = " + status + " " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}