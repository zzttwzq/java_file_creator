package .repository;

import .model.Dev_answer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface Dev_answerRepository extends JpaRepository <Dev_answer,Long>  {}

