CREATE PROCEDURE suspectsInvestigation()
BEGIN
    select id, name, surname from Suspect where height <= 170 and name like 'B%' and surname like 'Gre_n' order by id asc;    
END
