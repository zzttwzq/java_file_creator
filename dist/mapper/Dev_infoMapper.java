package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Dev_info;
import com.qlzw.smartwc.provider.Dev_infoProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_infoMapper")
@Mapper
public interface Dev_infoMapper {

    @SelectProvider(type = Dev_infoProvider.class,method = "selectAll")
    public List<Dev_info> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_infoProvider.class,method = "selectOne")
    public Dev_info show(@Param("id") Long id);

    @InsertProvider(type = Dev_infoProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_info dev_info);

    @DeleteProvider(type = Dev_infoProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_infoProvider.class,method = "updateOne")
    public Boolean update(Dev_info dev_info);

}