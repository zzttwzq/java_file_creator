package .mapper;

import .model.Dev_msg;
import .provider.Dev_msgProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_msgMapper")
@Mapper
public interface Dev_msgMapper {

    @SelectProvider(type = Dev_msgProvider.class,method = "selectAll")
    public List<Dev_msg> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_msgProvider.class,method = "selectOne")
    public Dev_msg show(@Param("id") Long id);

    @InsertProvider(type = Dev_msgProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_msg dev_msg);

    @DeleteProvider(type = Dev_msgProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_msgProvider.class,method = "updateOne")
    public Boolean update(Dev_msg dev_msg);

}