create database cloudification;
use cloudification;

CREATE TABLE users (     
    id int PRIMARY KEY auto_increment,     
    first_name varchar(50),     
    last_name varchar(50),     
    age int,     gender int,     
    pregnancies int,     
    glucose float,     
    blood_pressure float,     
    skin_thickness float,     
    insulin float,     
    bmi float,     
    dpf int,     
    result int );
CREATE USER 'salim'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON cloudification.* TO 'salim'@'localhost';
FLUSH PRIVILEGES;
