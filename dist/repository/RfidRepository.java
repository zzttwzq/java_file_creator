package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Rfid;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RfidRepository extends JpaRepository <Rfid,Long>  {}

