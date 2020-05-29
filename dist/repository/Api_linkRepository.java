package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Api_link;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Api_linkRepository extends JpaRepository <Api_link,Long>  {}

