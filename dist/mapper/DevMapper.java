package .mapper;

import .model.Dev;
import .provider.DevProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "devMapper")
@Mapper
public interface DevMapper {

    @SelectProvider(type = DevProvider.class,method = "selectAll")
    public List<Dev> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = DevProvider.class,method = "selectOne")
    public Dev show(@Param("id") Long id);

    @InsertProvider(type = DevProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev dev);

    @DeleteProvider(type = DevProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = DevProvider.class,method = "updateOne")
    public Boolean update(Dev dev);

}