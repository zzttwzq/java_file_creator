package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Dev_repair;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_repairRepository extends JpaRepository <Dev_repair,Long>  {}

