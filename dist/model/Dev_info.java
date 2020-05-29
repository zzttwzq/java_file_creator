package com.qlzw.smartwc.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Dev_info {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private Integer dev_id; // 设备id 
    private Integer last_time; // 最后更新时间 
    private Integer status; // 设备状态 
    private String snno; // 设备编号 
    private String ccid; // 设备ccid 
    private String rfid; // 设备rfid 
    private String proportion; // 液体配比 
    private Float temperature; // 设备温度 
    private Integer humidity; // 设备湿度 
    private Float nh3; // 设备氨气值 
    private Integer dayon; // 白天工作时间 
    private Integer dayoff; // 白天停止时间 
    private Integer nighton; // 晚上工作时间 
    private Integer nightoff; // 晚上停止时间 
    private Integer addwaternum; // 总加液次数 
    private Integer addwatertime; // 单次加液时间 
    private Integer atomizerpwm; // 雾化强度 
    private Integer fanmin; // 风扇最小转速 
    private Integer fanmax; // 风扇最大转速 
    private Float totaladdwater; // 累计加水量 
    private String alarmnumber; // 错误代码 
    private String rfid_status; // rfid状态 
    private String hrev; // 硬件版本 
    private String srev; // 软件版本 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Dev_info(Long id,Integer dev_id,Integer last_time,Integer status,String snno,String ccid,String rfid,String proportion,Float temperature,Integer humidity,Float nh3,Integer dayon,Integer dayoff,Integer nighton,Integer nightoff,Integer addwaternum,Integer addwatertime,Integer atomizerpwm,Integer fanmin,Integer fanmax,Float totaladdwater,String alarmnumber,String rfid_status,String hrev,String srev,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.dev_id=dev_id;
        this.last_time=last_time;
        this.status=status;
        this.snno=snno;
        this.ccid=ccid;
        this.rfid=rfid;
        this.proportion=proportion;
        this.temperature=temperature;
        this.humidity=humidity;
        this.nh3=nh3;
        this.dayon=dayon;
        this.dayoff=dayoff;
        this.nighton=nighton;
        this.nightoff=nightoff;
        this.addwaternum=addwaternum;
        this.addwatertime=addwatertime;
        this.atomizerpwm=atomizerpwm;
        this.fanmin=fanmin;
        this.fanmax=fanmax;
        this.totaladdwater=totaladdwater;
        this.alarmnumber=alarmnumber;
        this.rfid_status=rfid_status;
        this.hrev=hrev;
        this.srev=srev;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Dev_info() {}

    public Long getId () { return this.id;}

    public Integer getDev_id () { return this.dev_id;}

    public Integer getLast_time () { return this.last_time;}

    public Integer getStatus () { return this.status;}

    public String getSnno () { return this.snno;}

    public String getCcid () { return this.ccid;}

    public String getRfid () { return this.rfid;}

    public String getProportion () { return this.proportion;}

    public Float getTemperature () { return this.temperature;}

    public Integer getHumidity () { return this.humidity;}

    public Float getNh3 () { return this.nh3;}

    public Integer getDayon () { return this.dayon;}

    public Integer getDayoff () { return this.dayoff;}

    public Integer getNighton () { return this.nighton;}

    public Integer getNightoff () { return this.nightoff;}

    public Integer getAddwaternum () { return this.addwaternum;}

    public Integer getAddwatertime () { return this.addwatertime;}

    public Integer getAtomizerpwm () { return this.atomizerpwm;}

    public Integer getFanmin () { return this.fanmin;}

    public Integer getFanmax () { return this.fanmax;}

    public Float getTotaladdwater () { return this.totaladdwater;}

    public String getAlarmnumber () { return this.alarmnumber;}

    public String getRfid_status () { return this.rfid_status;}

    public String getHrev () { return this.hrev;}

    public String getSrev () { return this.srev;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setDev_id (Integer dev_id) { this.dev_id = dev_id;}

    public void setLast_time (Integer last_time) { this.last_time = last_time;}

    public void setStatus (Integer status) { this.status = status;}

    public void setSnno (String snno) { this.snno = snno;}

    public void setCcid (String ccid) { this.ccid = ccid;}

    public void setRfid (String rfid) { this.rfid = rfid;}

    public void setProportion (String proportion) { this.proportion = proportion;}

public void setTemperature (Float temperature) { this.temperature = temperature;}

    public void setHumidity (Integer humidity) { this.humidity = humidity;}

public void setNh3 (Float nh3) { this.nh3 = nh3;}

    public void setDayon (Integer dayon) { this.dayon = dayon;}

    public void setDayoff (Integer dayoff) { this.dayoff = dayoff;}

    public void setNighton (Integer nighton) { this.nighton = nighton;}

    public void setNightoff (Integer nightoff) { this.nightoff = nightoff;}

    public void setAddwaternum (Integer addwaternum) { this.addwaternum = addwaternum;}

    public void setAddwatertime (Integer addwatertime) { this.addwatertime = addwatertime;}

    public void setAtomizerpwm (Integer atomizerpwm) { this.atomizerpwm = atomizerpwm;}

    public void setFanmin (Integer fanmin) { this.fanmin = fanmin;}

    public void setFanmax (Integer fanmax) { this.fanmax = fanmax;}

public void setTotaladdwater (Float totaladdwater) { this.totaladdwater = totaladdwater;}

    public void setAlarmnumber (String alarmnumber) { this.alarmnumber = alarmnumber;}

    public void setRfid_status (String rfid_status) { this.rfid_status = rfid_status;}

    public void setHrev (String hrev) { this.hrev = hrev;}

    public void setSrev (String srev) { this.srev = srev;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Dev_info> {id = " + id + " " +
                "dev_id = " + dev_id + " " +
                "last_time = " + last_time + ", " +
                "status = " + status + " " +
                "snno = '" + snno + "' " +
                "ccid = '" + ccid + "' " +
                "rfid = '" + rfid + "' " +
                "proportion = '" + proportion + "' " +
                "temperature = " + temperature + " " +
                "humidity = " + humidity + " " +
                "nh3 = " + nh3 + " " +
                "dayon = " + dayon + " " +
                "dayoff = " + dayoff + " " +
                "nighton = " + nighton + " " +
                "nightoff = " + nightoff + " " +
                "addwaternum = " + addwaternum + " " +
                "addwatertime = " + addwatertime + " " +
                "atomizerpwm = " + atomizerpwm + " " +
                "fanmin = " + fanmin + " " +
                "fanmax = " + fanmax + " " +
                "totaladdwater = " + totaladdwater + " " +
                "alarmnumber = '" + alarmnumber + "' " +
                "rfid_status = '" + rfid_status + "' " +
                "hrev = '" + hrev + "' " +
                "srev = '" + srev + "' " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}