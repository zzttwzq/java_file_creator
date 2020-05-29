package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Api;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ApiRepository extends JpaRepository <Api,Long>  {}

