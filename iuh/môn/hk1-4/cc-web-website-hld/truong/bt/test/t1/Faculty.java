package model;


import java.util.List;


import java.util.ArrayList;
import java.util.List;

public class Faculty {
    private Long id;
    private String name;
    private List<Student> students = new ArrayList<>();

    public Faculty() {// do not use
    }

    public Faculty(Long id, String name, List<Student> students) { //constructor with parameters
        this.id = id;
        this.name = name;
        this.students = students != null ? students : new ArrayList<>();
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Student> getStudents() {
        return students;
    }

    public void setStudents(List<Student> students) {
        this.students = students;
    }
}

//public class Faculty {
//    
//    private Long id;
//    private String name;
//    private List<Student> students;
//
//    public Faculty(Long id, String name, List<Student> students) {
//        this.id = id;
//        this.name = name;
//        this.students = students;
//    }
//
//    public Long getId() { return id; }
//    public void setId(Long id) { this.id = id; }
//    
//    public String getName() { return name; }
//    public void setName(String name) { this.name = name; }
//    
//    public List<Student> getStudents() { return students; }
//    public void setStudents(List<Student> students) { this.students = students; }
//}