
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
create view Team_Overalls
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

\copy (SELECT * FROM Team_Overalls) to 'Team_Overalls.csv' DELIMITER ',' CSV HEADER;



5) Player_Averages

create view Player_Averages as 
SELECT t.team_name, p.player_name,f.format_name, c.category_name, e.element_name, pa.*
FROM team t, player p, format f, category c, element e, player_average pa
WHERE p.team_id = t.team_id and f.format_id = pa.format_id
and c.category_id = pa.category_id and e.element_id = pa.element_id
and p.player_id=pa.player_id
order by t.team_name


\copy (SELECT * FROM Player_Averages) to 'Player_Averages.csv' DELIMITER ',' CSV HEADER;


create view sum_lineups as 
select t.team_name,l.lineup_players,sum(min) as min,sum(l.plusminus) plusminus,sum(l.fga) fga,sum(l.fta) fta,
sum(l.offreb) offreb,sum(l.turnover) turnover,sum(l.oppo_fga) oppo_fga,sum(l.oppo_fta) oppo_fta,
sum(l.oppo_offreb) oppo_offreb,sum(l.oppo_turnover) oppo_turnover from lineup l, team t 
where t.team_id=l.team_id
group by t.team_name,l.lineup_players;



6) game_breakdown
create view iit_games_name as 
select g.game_id,  concat_ws(' vs ',t1.team_name,t2.team_name) as game_name
from team t1, team t2, game g
where t1.team_id = g.home_team_id
and t2.team_id = g.away_team_id
and t1.team_name='Illinois Tech Scarlet Hawks'
union
select g.game_id,concat_ws(' at ',t2.team_name,t1.team_name) as game_name
from team t1, team t2, game g
where t1.team_id = g.home_team_id
and t2.team_id = g.away_team_id
and t2.team_name='Illinois Tech Scarlet Hawks'



create view game_breakdown as
with lineup_track as(
select l.*,gt.score_difference,gt.time from lineup l
left join game_track gt
on l.game_id = gt.game_id                                                                
and l.session_number = gt.session_number
and l.started >= gt.time
and l.ended <= gt.time)
select ign.game_name,lt.* from lineup_track lt, iit_games_name ign
where lt.game_id = ign.game_id


create view game_lineups as
select ign.game_name, l.* from lineup l, iit_games_name ign
where ign.game_id = l.game_id   


create view game_score_difference as
select ign.game_name, gt.score_difference,gt.time from game_track gt, iit_games_name ign
where ign.game_id = gt.game_id;  



