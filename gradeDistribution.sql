CREATE PROCEDURE gradeDistribution()
BEGIN
	SELECT t.name as Name, t.ID as ID
    FROM (
        SELECT name, ID, 
        (Midterm1*0.25)+(Midterm2*0.25) + (Final*0.5) as option_1,
        (Midterm1*0.5)+(Midterm2*0.5) as option_2,
        Final as option_3
        FROM Grades
        ) t
    WHERE t.option_3 > t.option_2 and t.option_3 > t.option_1
    ORDER by LEFT(name,3) asc, ID ASC ;
END
