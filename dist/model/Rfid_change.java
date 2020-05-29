package .model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Rfid_change {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private String snno; // 设备snno 
    private String newrfid; // 新的rfid 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Rfid_change(Long id,String snno,String newrfid,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.snno=snno;
        this.newrfid=newrfid;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Rfid_change() {}

    public Long getId () { return this.id;}

    public String getSnno () { return this.snno;}

    public String getNewrfid () { return this.newrfid;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setSnno (String snno) { this.snno = snno;}

    public void setNewrfid (String newrfid) { this.newrfid = newrfid;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Rfid_change> {id = " + id + " " +
                "snno = '" + snno + "' " +
                "newrfid = '" + newrfid + "' " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}