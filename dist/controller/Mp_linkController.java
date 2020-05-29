package com.qlzw.smartwc.controller;

import com.qlzw.smartwc.model.Mp_link;

import com.qlzw.smartwc.mapper.Mp_linkMapper;
import com.qlzw.smartwc.repository.Mp_linkRepository;
import com.qlzw.smartwc.utils.Pager;
import com.qlzw.smartwc.utils.RESPONSE_STATUS;
import com.qlzw.smartwc.utils.ResponseStatusGennerator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.*;
@RequestMapping("/mp_link")

@RestController
public class Mp_linkController {

    @Autowired
    private Mp_linkMapper mp_linkMapper; 

    @Autowired
    private Mp_linkRepository mp_linkRepository; 

    @Autowired
    private ResponseStatusGennerator responseStatus; 

    // 获取列表
    @GetMapping
    public HashMap<String, Object> list(Pager page,@Validated Mp_link mp_link) {
        
        List<Mp_link> list = mp_linkMapper.list(page.getPage(),page.getSize());
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", list);
        return map;
    }

    // 删除
    @GetMapping("/delete/{id}")
    public HashMap<String, Object> delete(@PathVariable("id") Long id) {
        
        mp_linkMapper.delete(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", null);
        return map;
    }

    // 查看详情
    @GetMapping("/{id}")
    public HashMap<String, Object> show(@PathVariable("id") Long id) {
        
        Mp_link mp_link = mp_linkMapper.show(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", mp_link);
        return map;
    }

    // 插入，保存
    @PostMapping
    public HashMap<String, Object> store(@Validated Mp_link mp_link) {
        
        Long id = mp_link.getId() != null ? mp_link.getId() : 0;
        
        if (id > 0) {
        
            mp_linkMapper.update(mp_link);
        } else {
        
            mp_linkMapper.insert(mp_link);
        }
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", mp_link);
        return map;
    }

}
