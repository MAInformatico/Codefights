CREATE PROCEDURE securityBreach()
BEGIN
    select * from users where attribute like BINARY concat('_%\%',first_name,'\_',second_name,'\%%');
END
