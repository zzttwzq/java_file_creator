package .repository;

import .model.Rfid_change;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Rfid_changeRepository extends JpaRepository <Rfid_change,Long>  {}

