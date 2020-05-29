package com.qlzw.smartwc.mapper;

import com.qlzw.smartwc.model.Dev_answer;
import com.qlzw.smartwc.provider.Dev_answerProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "dev_answerMapper")
@Mapper
public interface Dev_answerMapper {

    @SelectProvider(type = Dev_answerProvider.class,method = "selectAll")
    public List<Dev_answer> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = Dev_answerProvider.class,method = "selectOne")
    public Dev_answer show(@Param("id") Long id);

    @InsertProvider(type = Dev_answerProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Dev_answer dev_answer);

    @DeleteProvider(type = Dev_answerProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = Dev_answerProvider.class,method = "updateOne")
    public Boolean update(Dev_answer dev_answer);

}