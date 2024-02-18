<<<<<<< HEAD
-- Create states table in hbtn_0e_0_usa with some data
=======
reate states table in hbtn_0e_0_usa with some data
>>>>>>> 8ab0db420820730e26b3e7617f81a1ef20c6a26b
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
