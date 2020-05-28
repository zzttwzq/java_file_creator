package com.smartwc.qlzw.com.mapper;

import com.smartwc.qlzw.com.model.User;
import com.smartwc.qlzw.com.provider.UserProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "userMapper")
@Mapper
public interface UserMapper {

    @SelectProvider(type = UserProvider.class,method = "selectAll")
    public List<User> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = UserProvider.class,method = "selectOne")
    public User show(@Param("id") Long id);

    @InsertProvider(type = UserProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(User user);

    @DeleteProvider(type = UserProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = UserProvider.class,method = "updateOne")
    public Boolean update(User user);

}