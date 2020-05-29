package .mapper;

import .model.Api;
import .provider.ApiProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "apiMapper")
@Mapper
public interface ApiMapper {

    @SelectProvider(type = ApiProvider.class,method = "selectAll")
    public List<Api> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = ApiProvider.class,method = "selectOne")
    public Api show(@Param("id") Long id);

    @InsertProvider(type = ApiProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Api api);

    @DeleteProvider(type = ApiProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = ApiProvider.class,method = "updateOne")
    public Boolean update(Api api);

}