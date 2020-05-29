package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Dev_connect;
import com.qlzw.smartwc.provider.Dev_connectProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_connectMapper")
@Mapper
public interface Dev_connectMapper {

    @SelectProvider(type = Dev_connectProvider.class,method = "selectAll")
    public List<Dev_connect> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_connectProvider.class,method = "selectOne")
    public Dev_connect show(@Param("id") Long id);

    @InsertProvider(type = Dev_connectProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_connect dev_connect);

    @DeleteProvider(type = Dev_connectProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_connectProvider.class,method = "updateOne")
    public Boolean update(Dev_connect dev_connect);

}