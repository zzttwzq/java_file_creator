package .controller;

import .model.Admin_dev_link;

import .mapper.Admin_dev_linkMapper;
import .repository.Admin_dev_linkRepository;
import com.smartwc.qlzw.com.utils.Pager;
import com.smartwc.qlzw.com.utils.RESPONSE_STATUS;
import com.smartwc.qlzw.com.utils.ResponseStatusGennerator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.*;
@RequestMapping("/admin_dev_link")

@RestController
public class Admin_dev_linkController {

    @Autowired
    private Admin_dev_linkMapper admin_dev_linkMapper; 

    @Autowired
    private Admin_dev_linkRepository admin_dev_linkRepository; 

    @Autowired
    private ResponseStatusGennerator responseStatus; 

    // 获取列表
    @GetMapping
    public HashMap<String, Object> list(Pager page,@Validated Admin_dev_link admin_dev_link) {
        
        List<Admin_dev_link> list = admin_dev_linkMapper.list(page.getPage(),page.getSize());
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", list);
        return map;
    }

    // 删除
    @GetMapping("/delete/{id}")
    public HashMap<String, Object> delete(@PathVariable("id") Long id) {
        
        admin_dev_linkMapper.delete(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", null);
        return map;
    }

    // 查看详情
    @GetMapping("/{id}")
    public HashMap<String, Object> show(@PathVariable("id") Long id) {
        
        Admin_dev_link admin_dev_link = admin_dev_linkMapper.show(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", admin_dev_link);
        return map;
    }

    // 插入，保存
    @PostMapping
    public HashMap<String, Object> store(@Validated Admin_dev_link admin_dev_link) {
        
        Long id = admin_dev_link.getId() != null ? admin_dev_link.getId() : 0;
        
        if (id > 0) {
        
            admin_dev_linkMapper.update(admin_dev_link);
        } else {
        
            admin_dev_linkMapper.insert(admin_dev_link);
        }
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", admin_dev_link);
        return map;
    }

}

