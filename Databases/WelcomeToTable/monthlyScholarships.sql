CREATE PROCEDURE monthlyScholarships()
BEGIN
	select id, scholarship/12 sho from scholarships;
END
