package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Mp_user;
import com.qlzw.smartwc.provider.Mp_userProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "mp_userMapper")
@Mapper
public interface Mp_userMapper {

    @SelectProvider(type = Mp_userProvider.class,method = "selectAll")
    public List<Mp_user> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Mp_userProvider.class,method = "selectOne")
    public Mp_user show(@Param("id") Long id);

    @InsertProvider(type = Mp_userProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Mp_user mp_user);

    @DeleteProvider(type = Mp_userProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Mp_userProvider.class,method = "updateOne")
    public Boolean update(Mp_user mp_user);

}