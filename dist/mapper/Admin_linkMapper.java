package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Admin_link;
import com.qlzw.smartwc.provider.Admin_linkProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "admin_linkMapper")
@Mapper
public interface Admin_linkMapper {

    @SelectProvider(type = Admin_linkProvider.class,method = "selectAll")
    public List<Admin_link> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Admin_linkProvider.class,method = "selectOne")
    public Admin_link show(@Param("id") Long id);

    @InsertProvider(type = Admin_linkProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Admin_link admin_link);

    @DeleteProvider(type = Admin_linkProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Admin_linkProvider.class,method = "updateOne")
    public Boolean update(Admin_link admin_link);

}