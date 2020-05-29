package .repository;

import .model.Dev_update_msg;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_update_msgRepository extends JpaRepository <Dev_update_msg,Long>  {}

