package rest.example.student.student;

public class StudentNotFoundException extends RuntimeException{

    public StudentNotFoundException(String exception) {
        super(exception);
    }
}
