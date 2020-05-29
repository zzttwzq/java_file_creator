package .repository;

import .model.Mp_link;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Mp_linkRepository extends JpaRepository <Mp_link,Long>  {}

