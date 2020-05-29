package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Dev;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DevRepository extends JpaRepository <Dev,Long>  {}

