package com.qlzw.smartwc.controller;

import com.qlzw.smartwc.model.Dev_cmd;

import com.qlzw.smartwc.mapper.Dev_cmdMapper;
import com.qlzw.smartwc.repository.Dev_cmdRepository;
import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.utils.RESPONSE_STATUS;
import com.qlzw.smartwc.utils.ResponseStatusGennerator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.*;
@RequestMapping("/dev_cmd")

@RestController
public class Dev_cmdController {

    @Autowired
    private Dev_cmdMapper dev_cmdMapper; 

    @Autowired
    private Dev_cmdRepository dev_cmdRepository; 

    @Autowired
    private ResponseStatusGennerator responseStatus; 

    // 获取列表
    @GetMapping
    public HashMap<String, Object> list(Pager page,@Validated Dev_cmd dev_cmd) {
        
        List<Dev_cmd> list = dev_cmdMapper.list(page.getPage(),page.getSize());
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", list);
        return map;
    }

    // 删除
    @GetMapping("/delete/{id}")
    public HashMap<String, Object> delete(@PathVariable("id") Long id) {
        
        dev_cmdMapper.delete(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", null);
        return map;
    }

    // 查看详情
    @GetMapping("/{id}")
    public HashMap<String, Object> show(@PathVariable("id") Long id) {
        
        Dev_cmd dev_cmd = dev_cmdMapper.show(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", dev_cmd);
        return map;
    }

    // 插入，保存
    @PostMapping
    public HashMap<String, Object> store(@Validated Dev_cmd dev_cmd) {
        
        Long id = dev_cmd.getId() != null ? dev_cmd.getId() : 0;
        
        if (id > 0) {
        
            dev_cmdMapper.update(dev_cmd);
        } else {
        
            dev_cmdMapper.insert(dev_cmd);
        }
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", dev_cmd);
        return map;
    }

}

