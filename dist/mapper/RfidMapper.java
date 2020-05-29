package .mapper;

import .model.Rfid;
import .provider.RfidProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "rfidMapper")
@Mapper
public interface RfidMapper {

    @SelectProvider(type = RfidProvider.class,method = "selectAll")
    public List<Rfid> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = RfidProvider.class,method = "selectOne")
    public Rfid show(@Param("id") Long id);

    @InsertProvider(type = RfidProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Rfid rfid);

    @DeleteProvider(type = RfidProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = RfidProvider.class,method = "updateOne")
    public Boolean update(Rfid rfid);

}