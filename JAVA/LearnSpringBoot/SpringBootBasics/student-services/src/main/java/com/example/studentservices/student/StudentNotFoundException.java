package com.example.studentservices.student;

public class StudentNotFoundException extends RuntimeException{
    public StudentNotFoundException(String exception){
        super(exception);
    }
}
