package .model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Dev {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private String name; // 设备名称 
    private String snno; // 设备编号 
    private String position; // 设备经纬度 
    private String address; // 设备地址 
    private Integer dev_info_id; // 设备信息id 
    private Integer rfid_id; // 关联的rfid 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Dev(Long id,String name,String snno,String position,String address,Integer dev_info_id,Integer rfid_id,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.name=name;
        this.snno=snno;
        this.position=position;
        this.address=address;
        this.dev_info_id=dev_info_id;
        this.rfid_id=rfid_id;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Dev() {}

    public Long getId () { return this.id;}

    public String getName () { return this.name;}

    public String getSnno () { return this.snno;}

    public String getPosition () { return this.position;}

    public String getAddress () { return this.address;}

    public Integer getDev_info_id () { return this.dev_info_id;}

    public Integer getRfid_id () { return this.rfid_id;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setName (String name) { this.name = name;}

    public void setSnno (String snno) { this.snno = snno;}

    public void setPosition (String position) { this.position = position;}

    public void setAddress (String address) { this.address = address;}

    public void setDev_info_id (Integer dev_info_id) { this.dev_info_id = dev_info_id;}

    public void setRfid_id (Integer rfid_id) { this.rfid_id = rfid_id;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Dev> {id = " + id + " " +
                "name = '" + name + "' " +
                "snno = '" + snno + "' " +
                "position = '" + position + "' " +
                "address = '" + address + "' " +
                "dev_info_id = " + dev_info_id + " " +
                "rfid_id = " + rfid_id + " " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}