package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Dev_action;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_actionRepository extends JpaRepository <Dev_action,Long>  {}

