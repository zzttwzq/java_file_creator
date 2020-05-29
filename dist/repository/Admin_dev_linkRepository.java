package .repository;

import .model.Admin_dev_link;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Admin_dev_linkRepository extends JpaRepository <Admin_dev_link,Long>  {}

