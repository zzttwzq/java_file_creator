package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Email_send;
import com.qlzw.smartwc.provider.Email_sendProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "email_sendMapper")
@Mapper
public interface Email_sendMapper {

    @SelectProvider(type = Email_sendProvider.class,method = "selectAll")
    public List<Email_send> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Email_sendProvider.class,method = "selectOne")
    public Email_send show(@Param("id") Long id);

    @InsertProvider(type = Email_sendProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Email_send email_send);

    @DeleteProvider(type = Email_sendProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Email_sendProvider.class,method = "updateOne")
    public Boolean update(Email_send email_send);

}