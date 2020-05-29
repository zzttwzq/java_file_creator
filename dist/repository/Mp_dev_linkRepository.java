package .repository;

import .model.Mp_dev_link;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Mp_dev_linkRepository extends JpaRepository <Mp_dev_link,Long>  {}

