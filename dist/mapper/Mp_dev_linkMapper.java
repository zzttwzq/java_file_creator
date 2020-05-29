package .mapper;

import .model.Mp_dev_link;
import .provider.Mp_dev_linkProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "mp_dev_linkMapper")
@Mapper
public interface Mp_dev_linkMapper {

    @SelectProvider(type = Mp_dev_linkProvider.class,method = "selectAll")
    public List<Mp_dev_link> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Mp_dev_linkProvider.class,method = "selectOne")
    public Mp_dev_link show(@Param("id") Long id);

    @InsertProvider(type = Mp_dev_linkProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Mp_dev_link mp_dev_link);

    @DeleteProvider(type = Mp_dev_linkProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Mp_dev_linkProvider.class,method = "updateOne")
    public Boolean update(Mp_dev_link mp_dev_link);

}