
1) offensive and defensive overall

SELECT t.team_name, ta1.ppp as offensive, ta2.ppp as defensive    
FROM team t, team_average ta1,category c1, format f1, element e1
WHERE t.team_id=ta1.team_id and ta1.category_id = c1.category_id 
and e1.element_id=ta1.element_id and f1.format_id = ta1.format_id 
c.category_name = 'Overall Offense' and e.element_name = 'Overall'
and t.team_id=ta2.team_id and ta2.category_id = c2.category_id 
and e2.element_id=ta2.element_id and f2.format_id = ta2.format_id 
c.category_name = 'Overall Defense' and e.element_name = 'Overall'

\copy (SELECT * FROM off_def_overall) to 'def_off.csv' DELIMITER ',' CSV HEADER;


2) player game
select t.team_name,p.player_name,pg.*,l.*
from team t, player p, player_game pg,lineup l
where t.team_id=p.team_id and pg.player_id=p.player_id
and pg.game_id=l.game_id and pg.lineup_id=l.lineup_id and l.team_id=p.team_id

3) lineup
select l.*
from lineup l, team t 
where t.team_id = l.team_id
and team_name = 'Illinois Tech Scarlet Hawks'

4) team overalls
create view Team_Overalls_1223_and_109
AS
(
SELECT t.team_name, f.format_name, c.category_name, e.element_name, ta.*
FROM team t, format f, category c, element e, team_average ta
WHERE t.team_id = ta.team_id and f.format_id = ta.format_id
and c.category_id = ta.category_id and e.element_id = ta.element_id
and c.category_name = 'Overall Defense'
order by format_name
)
union
(
SELECT t.team_name, f.format_name, c.category_name, e.element_name, ta.*
FROM team t, format f, category c, element e, team_average ta
WHERE t.team_id = ta.team_id and f.format_id = ta.format_id
and c.category_id = ta.category_id and e.element_id = ta.element_id
and c.category_name = 'Overall Offense'
order by format_name
)

\copy (SELECT * FROM Team_Overalls_1223_and_109) to 'Team_Averages_1223_and_109.csv' DELIMITER ',' CSV HEADER;



5) Player_Averages

create view Player_Averages as 
SELECT t.team_name, p.player_name,f.format_name, c.category_name, e.element_name, pa.*
FROM team t, player p, format f, category c, element e, player_average pa
WHERE p.team_id = t.team_id and f.format_id = pa.format_id
and c.category_id = pa.category_id and e.element_id = pa.element_id
and p.player_id=pa.player_id
order by t.team_name


\copy (SELECT * FROM Player_Averages) to 'Player_Averages.csv' DELIMITER ',' CSV HEADER;

