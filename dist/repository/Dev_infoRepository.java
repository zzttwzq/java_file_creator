package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Dev_info;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_infoRepository extends JpaRepository <Dev_info,Long>  {}

