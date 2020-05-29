package .model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Mp_link {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private Integer parent_admin_id; // 关联账户id 
    private Integer area_id; // 关联账户区域id 
    private Integer mp_id; // 小程序账户id 
    private Integer status; // 状态 0：取消关联 1：建立关联 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Mp_link(Long id,Integer parent_admin_id,Integer area_id,Integer mp_id,Integer status,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.parent_admin_id=parent_admin_id;
        this.area_id=area_id;
        this.mp_id=mp_id;
        this.status=status;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Mp_link() {}

    public Long getId () { return this.id;}

    public Integer getParent_admin_id () { return this.parent_admin_id;}

    public Integer getArea_id () { return this.area_id;}

    public Integer getMp_id () { return this.mp_id;}

    public Integer getStatus () { return this.status;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setParent_admin_id (Integer parent_admin_id) { this.parent_admin_id = parent_admin_id;}

    public void setArea_id (Integer area_id) { this.area_id = area_id;}

    public void setMp_id (Integer mp_id) { this.mp_id = mp_id;}

    public void setStatus (Integer status) { this.status = status;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Mp_link> {id = " + id + " " +
                "parent_admin_id = " + parent_admin_id + " " +
                "area_id = " + area_id + " " +
                "mp_id = " + mp_id + " " +
                "status = " + status + " " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}