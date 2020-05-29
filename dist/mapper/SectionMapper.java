package .mapper;

import .model.Section;
import .provider.SectionProvider;
import org.apache.ibatis.annotations.*;
import java.util.List;
import org.springframework.stereotype.Component;

@Component(value = "sectionMapper")
@Mapper
public interface SectionMapper {

    @SelectProvider(type = SectionProvider.class,method = "selectAll")
    public List<Section> list(@Param("page") Integer page,@Param("size") Integer size);

    @SelectProvider(type = SectionProvider.class,method = "selectOne")
    public Section show(@Param("id") Long id);

    @InsertProvider(type = SectionProvider.class,method = "insertOne")
    @Options(useGeneratedKeys = true,keyProperty = "id",keyColumn = "id")//加入该注解可以保持对象后，查看对象插入id
    public Boolean insert(Section section);

    @DeleteProvider(type = SectionProvider.class,method = "deleteOne")
    public Boolean delete(@Param("id") Long id);

    @UpdateProvider(type = SectionProvider.class,method = "updateOne")
    public Boolean update(Section section);

}