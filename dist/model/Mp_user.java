package .model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
public class Mp_user {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 记录ID 
    private String name; // 小程序用户登录名 
    private String nick_name; // 小程序用户昵称 
    private String token; // 小程序用户token 
    private String open_id; // 小程序账号唯一id 
    private String address; // 小程序用户地址 
    private String city_name; // 城市名 
    private Integer mobile; // 小程序用户手机号 
    private String cover; // 小程序用户头像 
    private Integer share; // 小程序用户分享信息 
    private Integer sex; // 小程序用户性别 
    private String email; // 小程序用户邮箱 
    private Integer admin_user_id; // 关联后台管理用户id 
    private String password; // 密码 
    private Integer create_at; // 创建于 
    private Integer update_at; // 更新于 
    private Integer delete_at; // 删除于 

    public Mp_user(Long id,String name,String nick_name,String token,String open_id,String address,String city_name,Integer mobile,String cover,Integer share,Integer sex,String email,Integer admin_user_id,String password,Integer create_at,Integer update_at,Integer delete_at) {
        this.id=id;
        this.name=name;
        this.nick_name=nick_name;
        this.token=token;
        this.open_id=open_id;
        this.address=address;
        this.city_name=city_name;
        this.mobile=mobile;
        this.cover=cover;
        this.share=share;
        this.sex=sex;
        this.email=email;
        this.admin_user_id=admin_user_id;
        this.password=password;
        this.create_at=create_at;
        this.update_at=update_at;
        this.delete_at=delete_at;
    }

    public Mp_user() {}

    public Long getId () { return this.id;}

    public String getName () { return this.name;}

    public String getNick_name () { return this.nick_name;}

    public String getToken () { return this.token;}

    public String getOpen_id () { return this.open_id;}

    public String getAddress () { return this.address;}

    public String getCity_name () { return this.city_name;}

    public Integer getMobile () { return this.mobile;}

    public String getCover () { return this.cover;}

    public Integer getShare () { return this.share;}

    public Integer getSex () { return this.sex;}

    public String getEmail () { return this.email;}

    public Integer getAdmin_user_id () { return this.admin_user_id;}

    public String getPassword () { return this.password;}

    public Integer getCreate_at () { return this.create_at;}

    public Integer getUpdate_at () { return this.update_at;}

    public Integer getDelete_at () { return this.delete_at;}

    public void setId (Long id) { this.id = id;}

    public void setName (String name) { this.name = name;}

    public void setNick_name (String nick_name) { this.nick_name = nick_name;}

    public void setToken (String token) { this.token = token;}

    public void setOpen_id (String open_id) { this.open_id = open_id;}

    public void setAddress (String address) { this.address = address;}

    public void setCity_name (String city_name) { this.city_name = city_name;}

    public void setMobile (Integer mobile) { this.mobile = mobile;}

    public void setCover (String cover) { this.cover = cover;}

    public void setShare (Integer share) { this.share = share;}

    public void setSex (Integer sex) { this.sex = sex;}

    public void setEmail (String email) { this.email = email;}

    public void setAdmin_user_id (Integer admin_user_id) { this.admin_user_id = admin_user_id;}

    public void setPassword (String password) { this.password = password;}

    public void setCreate_at (Integer create_at) { this.create_at = create_at;}

    public void setUpdate_at (Integer update_at) { this.update_at = update_at;}

    public void setDelete_at (Integer delete_at) { this.delete_at = delete_at;}

    public String toString() {

        return " <Mp_user> {id = " + id + " " +
                "name = '" + name + "' " +
                "nick_name = '" + nick_name + "' " +
                "token = '" + token + "' " +
                "open_id = '" + open_id + "' " +
                "address = '" + address + "' " +
                "city_name = '" + city_name + "' " +
                "mobile = " + mobile + " " +
                "cover = '" + cover + "' " +
                "share = " + share + " " +
                "sex = " + sex + " " +
                "email = '" + email + "' " +
                "admin_user_id = " + admin_user_id + " " +
                "password = '" + password + "' " +
                "create_at = " + create_at + " " +
                "update_at = " + update_at + " " +
                "delete_at = " + delete_at + " " + "}";
    }
}