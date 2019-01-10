
-- 1. Team Summary 
create view Team_Overalls_1223
AS
(
SELECT t.team_name, f.format_name, c.category_name, e.element_name, ta.*
FROM team t, format f, category c, element e, team_average ta
WHERE t.team_id = ta.team_id and f.format_id = ta.format_id
and c.category_id = ta.category_id and e.element_id = ta.element_id
and c.category_name = 'Overall Defense'
and ta.uploaded_date='2018-12-23'
order by format_name
)union
(
SELECT t.team_name, f.format_name, c.category_name, e.element_name, ta.*
FROM team t, format f, category c, element e, team_average ta
WHERE t.team_id = ta.team_id and f.format_id = ta.format_id
and c.category_id = ta.category_id and e.element_id = ta.element_id
and c.category_name = 'Overall Offense'
and ta.uploaded_date='2018-12-23'
order by format_name
)

\copy (select * from Team_Overalls_1223) to 'Team_Overalls_1223.csv' DELIMITER ',' CSV HEADER;

