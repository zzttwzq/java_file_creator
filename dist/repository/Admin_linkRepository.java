package .repository;

import .model.Admin_link;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Admin_linkRepository extends JpaRepository <Admin_link,Long>  {}

