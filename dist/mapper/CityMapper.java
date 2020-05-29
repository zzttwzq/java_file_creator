package .mapper;

import .model.City;
import .provider.CityProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "cityMapper")
@Mapper
public interface CityMapper {

    @SelectProvider(type = CityProvider.class,method = "selectAll")
    public List<City> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = CityProvider.class,method = "selectOne")
    public City show(@Param("id") Long id);

    @InsertProvider(type = CityProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(City city);

    @DeleteProvider(type = CityProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = CityProvider.class,method = "updateOne")
    public Boolean update(City city);

}