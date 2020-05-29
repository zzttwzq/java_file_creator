package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Email_send;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Email_sendRepository extends JpaRepository <Email_send,Long>  {}

