package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Msg_log;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Msg_logRepository extends JpaRepository <Msg_log,Long>  {}

