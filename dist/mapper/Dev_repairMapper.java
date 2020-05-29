package .mapper;

import .model.Dev_repair;
import .provider.Dev_repairProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_repairMapper")
@Mapper
public interface Dev_repairMapper {

    @SelectProvider(type = Dev_repairProvider.class,method = "selectAll")
    public List<Dev_repair> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_repairProvider.class,method = "selectOne")
    public Dev_repair show(@Param("id") Long id);

    @InsertProvider(type = Dev_repairProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_repair dev_repair);

    @DeleteProvider(type = Dev_repairProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_repairProvider.class,method = "updateOne")
    public Boolean update(Dev_repair dev_repair);

}