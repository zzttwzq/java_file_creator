package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Dev_cmd;
import com.qlzw.smartwc.provider.Dev_cmdProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_cmdMapper")
@Mapper
public interface Dev_cmdMapper {

    @SelectProvider(type = Dev_cmdProvider.class,method = "selectAll")
    public List<Dev_cmd> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_cmdProvider.class,method = "selectOne")
    public Dev_cmd show(@Param("id") Long id);

    @InsertProvider(type = Dev_cmdProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_cmd dev_cmd);

    @DeleteProvider(type = Dev_cmdProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_cmdProvider.class,method = "updateOne")
    public Boolean update(Dev_cmd dev_cmd);

}