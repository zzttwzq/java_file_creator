package .repository;

import .model.Dev_cmd;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_cmdRepository extends JpaRepository <Dev_cmd,Long>  {}

