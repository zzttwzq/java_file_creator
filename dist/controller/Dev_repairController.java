package .controller;

import .model.Dev_repair;

import .mapper.Dev_repairMapper;
import .repository.Dev_repairRepository;
import com.smartwc.qlzw.com.utils.Pager;
import com.smartwc.qlzw.com.utils.RESPONSE_STATUS;
import com.smartwc.qlzw.com.utils.ResponseStatusGennerator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.*;
@RequestMapping("/dev_repair")

@RestController
public class Dev_repairController {

    @Autowired
    private Dev_repairMapper dev_repairMapper; 

    @Autowired
    private Dev_repairRepository dev_repairRepository; 

    @Autowired
    private ResponseStatusGennerator responseStatus; 

    // 获取列表
    @GetMapping
    public HashMap<String, Object> list(Pager page,@Validated Dev_repair dev_repair) {
        
        List<Dev_repair> list = dev_repairMapper.list(page.getPage(),page.getSize());
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", list);
        return map;
    }

    // 删除
    @GetMapping("/delete/{id}")
    public HashMap<String, Object> delete(@PathVariable("id") Long id) {
        
        dev_repairMapper.delete(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", null);
        return map;
    }

    // 查看详情
    @GetMapping("/{id}")
    public HashMap<String, Object> show(@PathVariable("id") Long id) {
        
        Dev_repair dev_repair = dev_repairMapper.show(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", dev_repair);
        return map;
    }

    // 插入，保存
    @PostMapping
    public HashMap<String, Object> store(@Validated Dev_repair dev_repair) {
        
        Long id = dev_repair.getId() != null ? dev_repair.getId() : 0;
        
        if (id > 0) {
        
            dev_repairMapper.update(dev_repair);
        } else {
        
            dev_repairMapper.insert(dev_repair);
        }
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", dev_repair);
        return map;
    }

}

