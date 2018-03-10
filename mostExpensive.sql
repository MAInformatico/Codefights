CREATE PROCEDURE mostExpensive()
BEGIN
    SELECT f.name
    FROM(SELECT name, price, quantity, (price * quantity) as pq FROM Products ORDER BY pq desc, name asc limit 1) f;
END
