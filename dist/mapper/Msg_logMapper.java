package .mapper;

import .model.Msg_log;
import .provider.Msg_logProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "msg_logMapper")
@Mapper
public interface Msg_logMapper {

    @SelectProvider(type = Msg_logProvider.class,method = "selectAll")
    public List<Msg_log> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Msg_logProvider.class,method = "selectOne")
    public Msg_log show(@Param("id") Long id);

    @InsertProvider(type = Msg_logProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Msg_log msg_log);

    @DeleteProvider(type = Msg_logProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Msg_logProvider.class,method = "updateOne")
    public Boolean update(Msg_log msg_log);

}