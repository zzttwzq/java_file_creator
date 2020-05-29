package .mapper;

import .model.Dev_action;
import .provider.Dev_actionProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_actionMapper")
@Mapper
public interface Dev_actionMapper {

    @SelectProvider(type = Dev_actionProvider.class,method = "selectAll")
    public List<Dev_action> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_actionProvider.class,method = "selectOne")
    public Dev_action show(@Param("id") Long id);

    @InsertProvider(type = Dev_actionProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_action dev_action);

    @DeleteProvider(type = Dev_actionProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_actionProvider.class,method = "updateOne")
    public Boolean update(Dev_action dev_action);

}