package .repository;

import .model.Dev_msg;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_msgRepository extends JpaRepository <Dev_msg,Long>  {}

