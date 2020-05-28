package com.smartwc.qlzw.com.repository;

import com.smartwc.qlzw.com.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository <User,Long>  {}

