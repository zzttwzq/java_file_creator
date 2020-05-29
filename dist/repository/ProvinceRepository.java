package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Province;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProvinceRepository extends JpaRepository <Province,Long>  {}

