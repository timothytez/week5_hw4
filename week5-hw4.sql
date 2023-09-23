
CREATE PROCEDURE find_customer(IN f_name VARCHAR(45), IN l_name VARCHAR (45))

BEGIN
	SELECT *
	FROM customers
	WHERE first_name = f_name AND last_name = l_name;
END 


CALL find_customer("Tim", "Crooms");