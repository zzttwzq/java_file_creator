package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Mp_user;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Mp_userRepository extends JpaRepository <Mp_user,Long>  {}

