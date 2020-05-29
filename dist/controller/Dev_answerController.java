package com.qlzw.smartwc.controller;

import com.qlzw.smartwc.model.Dev_answer;

import com.qlzw.smartwc.mapper.Dev_answerMapper;
import com.qlzw.smartwc.repository.Dev_answerRepository;
import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.utils.RESPONSE_STATUS;
import com.qlzw.smartwc.utils.ResponseStatusGennerator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.*;
@RequestMapping("/dev_answer")

@RestController
public class Dev_answerController {

    @Autowired
    private Dev_answerMapper dev_answerMapper; 

    @Autowired
    private Dev_answerRepository dev_answerRepository; 

    @Autowired
    private ResponseStatusGennerator responseStatus; 

    // 获取列表
    @GetMapping
    public HashMap<String, Object> list(Pager page,@Validated Dev_answer dev_answer) {
        
        List<Dev_answer> list = dev_answerMapper.list(page.getPage(),page.getSize());
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", list);
        return map;
    }

    // 删除
    @GetMapping("/delete/{id}")
    public HashMap<String, Object> delete(@PathVariable("id") Long id) {
        
        dev_answerMapper.delete(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", null);
        return map;
    }

    // 查看详情
    @GetMapping("/{id}")
    public HashMap<String, Object> show(@PathVariable("id") Long id) {
        
        Dev_answer dev_answer = dev_answerMapper.show(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", dev_answer);
        return map;
    }

    // 插入，保存
    @PostMapping
    public HashMap<String, Object> store(@Validated Dev_answer dev_answer) {
        
        Long id = dev_answer.getId() != null ? dev_answer.getId() : 0;
        
        if (id > 0) {
        
            dev_answerMapper.update(dev_answer);
        } else {
        
            dev_answerMapper.insert(dev_answer);
        }
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", dev_answer);
        return map;
    }

}

