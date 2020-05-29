package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Email_send {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private Integer send_user_id; // 发送人id 
    private String snno; // 设备编号 
    private String to_email; // 发送的邮箱地址 
    private String subject; // 发送的标题 
    private String message; // 发送的内容 
    private String alarmnumber; // 错误类型 
    private Integer status; // 是否发送 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Email_send(Long id,Integer send_user_id,String snno,String to_email,String subject,String message,String alarmnumber,Integer status,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.send_user_id=send_user_id;
        this.snno=snno;
        this.to_email=to_email;
        this.subject=subject;
        this.message=message;
        this.alarmnumber=alarmnumber;
        this.status=status;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Email_send() {}

    public Long getId () { return this.id;}

    public Integer getSend_user_id () { return this.send_user_id;}

    public String getSnno () { return this.snno;}

    public String getTo_email () { return this.to_email;}

    public String getSubject () { return this.subject;}

    public String getMessage () { return this.message;}

    public String getAlarmnumber () { return this.alarmnumber;}

    public Integer getStatus () { return this.status;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setSend_user_id (Integer send_user_id) { this.send_user_id = send_user_id;}

    public void setSnno (String snno) { this.snno = snno;}

    public void setTo_email (String to_email) { this.to_email = to_email;}

    public void setSubject (String subject) { this.subject = subject;}

    public void setMessage (String message) { this.message = message;}

    public void setAlarmnumber (String alarmnumber) { this.alarmnumber = alarmnumber;}

    public void setStatus (Integer status) { this.status = status;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Email_send> {id = " + id + " " +
                "send_user_id = " + send_user_id + " " +
                "snno = '" + snno + "' " +
                "to_email = '" + to_email + "' " +
                "subject = '" + subject + "' " +
                "message = '" + message + "' " +
                "alarmnumber = '" + alarmnumber + "' " +
                "status = " + status + " " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}