package .mapper;

import .model.Dev_alarm;
import .provider.Dev_alarmProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_alarmMapper")
@Mapper
public interface Dev_alarmMapper {

    @SelectProvider(type = Dev_alarmProvider.class,method = "selectAll")
    public List<Dev_alarm> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_alarmProvider.class,method = "selectOne")
    public Dev_alarm show(@Param("id") Long id);

    @InsertProvider(type = Dev_alarmProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_alarm dev_alarm);

    @DeleteProvider(type = Dev_alarmProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_alarmProvider.class,method = "updateOne")
    public Boolean update(Dev_alarm dev_alarm);

}