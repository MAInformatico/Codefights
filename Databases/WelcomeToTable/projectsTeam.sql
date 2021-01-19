CREATE PROCEDURE projectsTeam()
BEGIN
	select name from projectLog group by name;
END
