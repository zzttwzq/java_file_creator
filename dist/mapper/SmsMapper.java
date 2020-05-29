package .mapper;

import .model.Sms;
import .provider.SmsProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "smsMapper")
@Mapper
public interface SmsMapper {

    @SelectProvider(type = SmsProvider.class,method = "selectAll")
    public List<Sms> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = SmsProvider.class,method = "selectOne")
    public Sms show(@Param("id") Long id);

    @InsertProvider(type = SmsProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Sms sms);

    @DeleteProvider(type = SmsProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = SmsProvider.class,method = "updateOne")
    public Boolean update(Sms sms);

}