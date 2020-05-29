package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Dev_update;
import com.qlzw.smartwc.provider.Dev_updateProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_updateMapper")
@Mapper
public interface Dev_updateMapper {

    @SelectProvider(type = Dev_updateProvider.class,method = "selectAll")
    public List<Dev_update> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_updateProvider.class,method = "selectOne")
    public Dev_update show(@Param("id") Long id);

    @InsertProvider(type = Dev_updateProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_update dev_update);

    @DeleteProvider(type = Dev_updateProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_updateProvider.class,method = "updateOne")
    public Boolean update(Dev_update dev_update);

}