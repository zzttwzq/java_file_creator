package .model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Sms {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private Integer user_id; // 用户信息 
    private String phone; // 手机号 
    private Integer type; // 短信类型 0-验证码 1-告警 
    private Integer status; // 状态 
    private String code; // 验证码 
    private String snno; // 设备号码 
    private String dev_name; // 设备名称 
    private String alarm; // 报警信息 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Sms(Long id,Integer user_id,String phone,Integer type,Integer status,String code,String snno,String dev_name,String alarm,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.user_id=user_id;
        this.phone=phone;
        this.type=type;
        this.status=status;
        this.code=code;
        this.snno=snno;
        this.dev_name=dev_name;
        this.alarm=alarm;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Sms() {}

    public Long getId () { return this.id;}

    public Integer getUser_id () { return this.user_id;}

    public String getPhone () { return this.phone;}

    public Integer getType () { return this.type;}

    public Integer getStatus () { return this.status;}

    public String getCode () { return this.code;}

    public String getSnno () { return this.snno;}

    public String getDev_name () { return this.dev_name;}

    public String getAlarm () { return this.alarm;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setUser_id (Integer user_id) { this.user_id = user_id;}

    public void setPhone (String phone) { this.phone = phone;}

    public void setType (Integer type) { this.type = type;}

    public void setStatus (Integer status) { this.status = status;}

    public void setCode (String code) { this.code = code;}

    public void setSnno (String snno) { this.snno = snno;}

    public void setDev_name (String dev_name) { this.dev_name = dev_name;}

    public void setAlarm (String alarm) { this.alarm = alarm;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Sms> {id = " + id + " " +
                "user_id = " + user_id + " " +
                "phone = '" + phone + "' " +
                "type = " + type + " " +
                "status = " + status + " " +
                "code = '" + code + "' " +
                "snno = '" + snno + "' " +
                "dev_name = '" + dev_name + "' " +
                "alarm = '" + alarm + "' " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}