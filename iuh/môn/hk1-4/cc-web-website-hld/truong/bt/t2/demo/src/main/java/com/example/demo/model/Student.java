package com.example.demo.model;

public class Student {
    private String name;
    private String mssv;
    private String avatar;

    public Student() {
    }

    public Student(String name, String mssv, String avatar) {
        this.name = name;
        this.mssv = mssv;
        this.avatar = avatar;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getMssv() {
        return mssv;
    }

    public void setMssv(String mssv) {
        this.mssv = mssv;
    }

    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }
}
