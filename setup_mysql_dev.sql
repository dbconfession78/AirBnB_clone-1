-- creates MySQL database hbnb_dev_db only if not existing
-- and gives privileges to user hbnb_dev on 2 DB's
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
      TO hbnb_dev@localhost
      IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.*
      TO hbnb_dev@localhost
      IDENTIFIED BY 'hbnb_dev_pwd';
