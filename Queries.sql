# 12.26 Plan

1) Offensive&Defensive Efficiencies
2) Strength and weaknesses
3) PER
4) Wis Lutheran Profiled

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