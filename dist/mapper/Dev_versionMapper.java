package .mapper;

import .model.Dev_version;
import .provider.Dev_versionProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_versionMapper")
@Mapper
public interface Dev_versionMapper {

    @SelectProvider(type = Dev_versionProvider.class,method = "selectAll")
    public List<Dev_version> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_versionProvider.class,method = "selectOne")
    public Dev_version show(@Param("id") Long id);

    @InsertProvider(type = Dev_versionProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_version dev_version);

    @DeleteProvider(type = Dev_versionProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_versionProvider.class,method = "updateOne")
    public Boolean update(Dev_version dev_version);

}