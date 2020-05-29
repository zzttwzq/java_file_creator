package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Dev_connect;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_connectRepository extends JpaRepository <Dev_connect,Long>  {}

