-- sets up a new db and user for airbnb site

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
