package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Admin_user;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Admin_userRepository extends JpaRepository <Admin_user,Long>  {}

