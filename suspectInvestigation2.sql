CREATE PROCEDURE suspectsInvestigation2()
BEGIN
    select id, name, surname from Suspect where height <= 170 or name not like 'B%' or surname not like 'Gre_n' order by id asc;
END
