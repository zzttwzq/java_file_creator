package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Sms;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SmsRepository extends JpaRepository <Sms,Long>  {}

