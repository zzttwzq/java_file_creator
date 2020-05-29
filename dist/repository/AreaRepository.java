package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Area;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AreaRepository extends JpaRepository <Area,Long>  {}

