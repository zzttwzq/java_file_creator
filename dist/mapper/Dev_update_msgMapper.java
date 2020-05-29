package .mapper;

import .model.Dev_update_msg;
import .provider.Dev_update_msgProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_update_msgMapper")
@Mapper
public interface Dev_update_msgMapper {

    @SelectProvider(type = Dev_update_msgProvider.class,method = "selectAll")
    public List<Dev_update_msg> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_update_msgProvider.class,method = "selectOne")
    public Dev_update_msg show(@Param("id") Long id);

    @InsertProvider(type = Dev_update_msgProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_update_msg dev_update_msg);

    @DeleteProvider(type = Dev_update_msgProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_update_msgProvider.class,method = "updateOne")
    public Boolean update(Dev_update_msg dev_update_msg);

}