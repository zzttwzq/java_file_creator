package .repository;

import .model.Dev_update;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_updateRepository extends JpaRepository <Dev_update,Long>  {}

