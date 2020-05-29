package .mapper;

import .model.Role;
import .provider.RoleProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "roleMapper")
@Mapper
public interface RoleMapper {

    @SelectProvider(type = RoleProvider.class,method = "selectAll")
    public List<Role> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = RoleProvider.class,method = "selectOne")
    public Role show(@Param("id") Long id);

    @InsertProvider(type = RoleProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Role role);

    @DeleteProvider(type = RoleProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = RoleProvider.class,method = "updateOne")
    public Boolean update(Role role);

}