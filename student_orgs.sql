DROP DATABASE IF EXISTS student_orgs;
CREATE DATABASE IF NOT EXISTS student_orgs;
USE student_orgs;

CREATE TABLE orgs (
    org_id INT AUTO_INCREMENT PRIMARY KEY,
    org_name VARCHAR(40)
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(40)
);
