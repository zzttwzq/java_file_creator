package .mapper;

import .model.Admin_user;
import .provider.Admin_userProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "admin_userMapper")
@Mapper
public interface Admin_userMapper {

    @SelectProvider(type = Admin_userProvider.class,method = "selectAll")
    public List<Admin_user> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Admin_userProvider.class,method = "selectOne")
    public Admin_user show(@Param("id") Long id);

    @InsertProvider(type = Admin_userProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Admin_user admin_user);

    @DeleteProvider(type = Admin_userProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Admin_userProvider.class,method = "updateOne")
    public Boolean update(Admin_user admin_user);

}