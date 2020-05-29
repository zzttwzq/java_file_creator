package .controller;

import .model.Mp_user_share;

import .mapper.Mp_user_shareMapper;
import .repository.Mp_user_shareRepository;
import com.smartwc.qlzw.com.utils.Pager;
import com.smartwc.qlzw.com.utils.RESPONSE_STATUS;
import com.smartwc.qlzw.com.utils.ResponseStatusGennerator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.*;
@RequestMapping("/mp_user_share")

@RestController
public class Mp_user_shareController {

    @Autowired
    private Mp_user_shareMapper mp_user_shareMapper; 

    @Autowired
    private Mp_user_shareRepository mp_user_shareRepository; 

    @Autowired
    private ResponseStatusGennerator responseStatus; 

    // 获取列表
    @GetMapping
    public HashMap<String, Object> list(Pager page,@Validated Mp_user_share mp_user_share) {
        
        List<Mp_user_share> list = mp_user_shareMapper.list(page.getPage(),page.getSize());
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", list);
        return map;
    }

    // 删除
    @GetMapping("/delete/{id}")
    public HashMap<String, Object> delete(@PathVariable("id") Long id) {
        
        mp_user_shareMapper.delete(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", null);
        return map;
    }

    // 查看详情
    @GetMapping("/{id}")
    public HashMap<String, Object> show(@PathVariable("id") Long id) {
        
        Mp_user_share mp_user_share = mp_user_shareMapper.show(id);
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", mp_user_share);
        return map;
    }

    // 插入，保存
    @PostMapping
    public HashMap<String, Object> store(@Validated Mp_user_share mp_user_share) {
        
        Long id = mp_user_share.getId() != null ? mp_user_share.getId() : 0;
        
        if (id > 0) {
        
            mp_user_shareMapper.update(mp_user_share);
        } else {
        
            mp_user_shareMapper.insert(mp_user_share);
        }
        
        HashMap<String, Object> map = new HashMap<>();
        map.put("code", responseStatus.getCode(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("msg", responseStatus.getMsg(RESPONSE_STATUS.RESPONSE_STATUS_SUCCESS));
        map.put("data", mp_user_share);
        return map;
    }

}

