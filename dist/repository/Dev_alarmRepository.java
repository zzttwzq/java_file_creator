package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Dev_alarm;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_alarmRepository extends JpaRepository <Dev_alarm,Long>  {}

