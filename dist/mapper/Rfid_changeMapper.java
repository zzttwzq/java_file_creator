package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Rfid_change;
import com.qlzw.smartwc.provider.Rfid_changeProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "rfid_changeMapper")
@Mapper
public interface Rfid_changeMapper {

    @SelectProvider(type = Rfid_changeProvider.class,method = "selectAll")
    public List<Rfid_change> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Rfid_changeProvider.class,method = "selectOne")
    public Rfid_change show(@Param("id") Long id);

    @InsertProvider(type = Rfid_changeProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Rfid_change rfid_change);

    @DeleteProvider(type = Rfid_changeProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Rfid_changeProvider.class,method = "updateOne")
    public Boolean update(Rfid_change rfid_change);

}