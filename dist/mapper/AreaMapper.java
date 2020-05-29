package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Area;
import com.qlzw.smartwc.provider.AreaProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "areaMapper")
@Mapper
public interface AreaMapper {

    @SelectProvider(type = AreaProvider.class,method = "selectAll")
    public List<Area> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = AreaProvider.class,method = "selectOne")
    public Area show(@Param("id") Long id);

    @InsertProvider(type = AreaProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Area area);

    @DeleteProvider(type = AreaProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = AreaProvider.class,method = "updateOne")
    public Boolean update(Area area);

}