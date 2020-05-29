package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Mp_user_share;
import com.qlzw.smartwc.provider.Mp_user_shareProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "mp_user_shareMapper")
@Mapper
public interface Mp_user_shareMapper {

    @SelectProvider(type = Mp_user_shareProvider.class,method = "selectAll")
    public List<Mp_user_share> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Mp_user_shareProvider.class,method = "selectOne")
    public Mp_user_share show(@Param("id") Long id);

    @InsertProvider(type = Mp_user_shareProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Mp_user_share mp_user_share);

    @DeleteProvider(type = Mp_user_shareProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Mp_user_shareProvider.class,method = "updateOne")
    public Boolean update(Mp_user_share mp_user_share);

}