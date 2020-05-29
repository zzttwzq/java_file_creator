package .repository;

import .model.Dev_version;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_versionRepository extends JpaRepository <Dev_version,Long>  {}

