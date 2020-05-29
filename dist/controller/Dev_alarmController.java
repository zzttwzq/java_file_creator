package .controller;

import .model.Dev_alarm;

import .mapper.Dev_alarmMapper;
import .repository.Dev_alarmRepository;
import com.smartwc.qlzw.com.utils.Pager;
import com.smartwc.qlzw.com.utils.RESPONSE_STATUS;
import com.smartwc.qlzw.com.utils.ResponseStatusGennerator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.*;
@RequestMapping("/dev_alarm")

@RestController
public class Dev_alarmController {

    @Autowired
    private Dev_alarmMapper dev_alarmMapper; 

    @Autowired
    private Dev_alarmRepository dev_alarmRepository; 

    @Autowired
    private ResponseStatusGennerator responseStatus; 

    // 获取列表
    @GetMapping
    public HashMap<String, Object> list(Pager page,@Validated Dev_alarm dev_alarm) {
        
        List<Dev_alarm> list = dev_alarmMapper.list(page.getPage(),page.getSize());
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", list);
        return map;
    }

    // 删除
    @GetMapping("/delete/{id}")
    public HashMap<String, Object> delete(@PathVariable("id") Long id) {
        
        dev_alarmMapper.delete(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", null);
        return map;
    }

    // 查看详情
    @GetMapping("/{id}")
    public HashMap<String, Object> show(@PathVariable("id") Long id) {
        
        Dev_alarm dev_alarm = dev_alarmMapper.show(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", dev_alarm);
        return map;
    }

    // 插入，保存
    @PostMapping
    public HashMap<String, Object> store(@Validated Dev_alarm dev_alarm) {
        
        Long id = dev_alarm.getId() != null ? dev_alarm.getId() : 0;
        
        if (id > 0) {
        
            dev_alarmMapper.update(dev_alarm);
        } else {
        
            dev_alarmMapper.insert(dev_alarm);
        }
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", dev_alarm);
        return map;
    }

}

