Q20: CREATE A LIMITED-PRIVILEGE MYSQL USER
CREATE USER 'lab10_user'@'localhost' IDENTIFIED BY 'change_this_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON lab10_app.* TO 'lab10_user'@'localhost';
FLUSH PRIVILEGES;
-- Do not use root in the application. Set the same credentials in config/config.php.
-- Use a stronger unique password and restrict host/network access in production.
