package .mapper;

import .model.Api_link;
import .provider.Api_linkProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "api_linkMapper")
@Mapper
public interface Api_linkMapper {

    @SelectProvider(type = Api_linkProvider.class,method = "selectAll")
    public List<Api_link> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Api_linkProvider.class,method = "selectOne")
    public Api_link show(@Param("id") Long id);

    @InsertProvider(type = Api_linkProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Api_link api_link);

    @DeleteProvider(type = Api_linkProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Api_linkProvider.class,method = "updateOne")
    public Boolean update(Api_link api_link);

}