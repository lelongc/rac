package com.example.demo.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;

@Entity
@Table(name = "staffs")
public class Staff {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(nullable = false, length = 150)
    private String email;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "department_id", nullable = false)
    @JsonIgnoreProperties({"staffs", "hibernateLazyInitializer"})
    private Department department;

    @Transient
    private Long departmentId;

    public Staff() {}

    public Staff(String name, String email, Department department) {
        this.name = name;
        this.email = email;
        this.department = department;
    }

    public Staff(Long id, String name, String email, Department department) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.department = department;
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

    @JsonProperty("departmentId")
    public Long getDepartmentId() {
        if (department != null) {
            return department.getId();
        }
        return departmentId;
    }

    @JsonProperty("departmentId")
    public void setDepartmentId(Long departmentId) {
        this.departmentId = departmentId;
    }
}
