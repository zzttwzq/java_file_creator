package .mapper;

import .model.Dev_repair_link;
import .provider.Dev_repair_linkProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_repair_linkMapper")
@Mapper
public interface Dev_repair_linkMapper {

    @SelectProvider(type = Dev_repair_linkProvider.class,method = "selectAll")
    public List<Dev_repair_link> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_repair_linkProvider.class,method = "selectOne")
    public Dev_repair_link show(@Param("id") Long id);

    @InsertProvider(type = Dev_repair_linkProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_repair_link dev_repair_link);

    @DeleteProvider(type = Dev_repair_linkProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_repair_linkProvider.class,method = "updateOne")
    public Boolean update(Dev_repair_link dev_repair_link);

}