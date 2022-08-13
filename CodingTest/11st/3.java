import org.springframework.stereotype.Service;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.beans.factory.annotation.Autowired;

import javax.persistence.Entity;
import javax.persistence.EntityManager;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.List;


@Table(name = "person")
@Entity
public class Person {

    private static final String BLANK = " ";

    @Id
    private Long id;

    private String firstName;

    private String lastName;


    public String getFullName() {
        return firstName + BLANK + lastName;
    }
}


@Service
class PersonService {

    private final PersonRepository personRepository;

    @Autowired
    public PersonService(PersonRepository personRepository) {
        this.personRepository = personRepository;
    }

    List<Person> findAll() {
        return personRepository.findAll();
    }
}

interface PersonRepository extends JpaRepository<Person, Long> {
}
