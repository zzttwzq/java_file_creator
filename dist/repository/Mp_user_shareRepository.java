package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Mp_user_share;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Mp_user_shareRepository extends JpaRepository <Mp_user_share,Long>  {}

