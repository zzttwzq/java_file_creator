package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Province;
import com.qlzw.smartwc.provider.ProvinceProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "provinceMapper")
@Mapper
public interface ProvinceMapper {

    @SelectProvider(type = ProvinceProvider.class,method = "selectAll")
    public List<Province> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = ProvinceProvider.class,method = "selectOne")
    public Province show(@Param("id") Long id);

    @InsertProvider(type = ProvinceProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Province province);

    @DeleteProvider(type = ProvinceProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = ProvinceProvider.class,method = "updateOne")
    public Boolean update(Province province);

}