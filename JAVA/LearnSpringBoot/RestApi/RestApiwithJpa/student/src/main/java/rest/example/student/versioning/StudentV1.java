package rest.example.student.versioning;

public class StudentV1 {
    private String name;

    public StudentV1() {
        super();
    }

    public StudentV1(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
