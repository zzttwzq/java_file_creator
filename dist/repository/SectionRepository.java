package com.qlzw.smartwc.repository;

import com.qlzw.smartwc.model.Section;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SectionRepository extends JpaRepository <Section,Long>  {}

