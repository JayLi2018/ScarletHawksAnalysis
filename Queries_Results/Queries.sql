
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
create view rockford_iit_lineups as 
select l.*
from lineup l, team t 
where t.team_id = l.team_id
and game_id = 20
union
select l.*
from lineup l, team t 
where t.team_id = l.team_id
and game_id = 14

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

\copy (select * from game_breakdown) to 'game_breakdown_2_18.csv' csv header;



create view game_lineups as
select ign.game_name, l.* from lineup l, iit_games_name ign
where ign.game_id = l.game_id 

\copy (select * from game_lineups) to 'game_lineups_2_16.csv' csv header;


create view game_score_difference as
select ign.game_name, gt.score_difference,gt.time from game_track gt, iit_games_name ign
where ign.game_id = gt.game_id;  

7) get shot ranges of teams 

select t.team_name, ta.*, c.category_name, e.element_name,f.format_name
from team t, team_average ta, category c, element e, format f
where ta.uploaded_date = '2019-01-26'
and ta.format_id = f.format_id
and ta.category_id = c.category_id
and ta.element_id = e.element_id
and ta.team_id = t.team_id
and c.category_id = 9;


8) iit vs rockford

(1) team level

create view team_play_types as 
(
select t.team_name,f.format_name,c.category_name,e.element_name,ta.*
from team t, format f, category c, element e,team_average ta
where ta.team_id = t.team_id and ta.format_id=f.format_id
and c.category_id = ta.category_id and e.element_id = ta.element_id
and uploaded_date = '2019-02-12'
and c.category_name = 'Play Types'
)
union
(
select t.team_name,f.format_name,c.category_name,e.element_name,ta.*
from team t, format f, category c, element e,team_average ta
where ta.team_id = t.team_id and ta.format_id=f.format_id
and c.category_id = ta.category_id and e.element_id = ta.element_id
and uploaded_date = '2019-02-12'
and e.element_name = 'Overall'
)

create view player_play_types as 
(
select t.team_name,p.player_name,f.format_name,c.category_name,e.element_name,pa.*
from team t, player p, format f, category c, element e,player_average pa
where p.team_id = t.team_id and pa.player_id = p.player_id and pa.format_id=f.format_id
and c.category_id = pa.category_id and e.element_id = pa.element_id
and uploaded_date = '2019-02-12'
and c.category_name = 'Play Types'
)
union
(
select t.team_name,p.player_name,f.format_name,c.category_name,e.element_name,pa.*
from team t, player p, format f, category c, element e,player_average pa
where p.team_id = t.team_id and pa.player_id = p.player_id and pa.format_id=f.format_id
and c.category_id = pa.category_id and e.element_id = pa.element_id
and uploaded_date = '2019-02-12'
and e.element_name = 'Overall'
);

\copy (select * from player_play_types where team_name like '%Illinois Tech%' or team_name like '%Milwaukee School%') to 'iit_msoe_players.csv' csv header;



(2) plater levels

create view iit_rockford_games as
( 
select p.player_name,ign.game_name,pg.* 
from iit_games_name ign, player_game pg, player p
where ign.game_id = pg.game_id
and p.player_id = pg.player_id 
and ign.game_name
like '%Scarlet Hawks vs Rockford%'

union

select p.player_name,ign.game_name,pg.* 
from iit_games_name ign, player_game pg, player p
where ign.game_id = pg.game_id
and p.player_id = pg.player_id 
and ign.game_name
like '%Scarlet Hawks at Rockford%'
);




9) Final Fours 

create view final_four_games as 
( 
select t.team_id,p.player_name,ign.game_name,pg.* 
from team t,iit_games_name ign, player_game pg, player p
where ign.game_id = pg.game_id
and t.team_id = p.team_id
and p.player_id = pg.player_id 
and ign.game_name
like '%Scarlet Hawks vs Milwaukee School%'

union

select t.team_id,p.player_name,ign.game_name,pg.* 
from team t,iit_games_name ign, player_game pg, player p
where ign.game_id = pg.game_id
and t.team_id = p.team_id
and p.player_id = pg.player_id 
and ign.game_name
like '%Scarlet Hawks at Milwaukee School%'

union 

select t.team_id,p.player_name,ign.game_name,pg.* 
from team t,iit_games_name ign, player_game pg, player p
where ign.game_id = pg.game_id
and t.team_id = p.team_id
and p.player_id = pg.player_id 
and ign.game_name
like '%Scarlet Hawks at Aurora%'

union

select t.team_id,p.player_name,ign.game_name,pg.* 
from team t,iit_games_name ign, player_game pg, player p
where ign.game_id = pg.game_id
and t.team_id = p.team_id
and p.player_id = pg.player_id 
and ign.game_name
like '%Scarlet Hawks vs Aurora%'

union

select t.team_id,p.player_name,ign.game_name,pg.* 
from team t,iit_games_name ign, player_game pg, player p
where ign.game_id = pg.game_id
and t.team_id = p.team_id
and p.player_id = pg.player_id 
and ign.game_name
like '%Scarlet Hawks at Concordia (WI) Falcons%'

union

select t.team_id,p.player_name,ign.game_name,pg.* 
from team t,iit_games_name ign, player_game pg, player p
where ign.game_id = pg.game_id
and t.team_id = p.team_id
and p.player_id = pg.player_id 
and ign.game_name
like '%Scarlet Hawks vs Concordia (WI) Falcons%'
);


create view final_four_lineups as 
select l.*
from lineup l, team t 
where t.team_id = l.team_id
and game_id = 2
union
select l.*
from lineup l, team t 
where t.team_id = l.team_id
and game_id = 4
union
select l.*
from lineup l, team t 
where t.team_id = l.team_id
and game_id = 6
union
select l.*
from lineup l, team t 
where t.team_id = l.team_id
and game_id = 11
union
select l.*
from lineup l, team t 
where t.team_id = l.team_id
and game_id = 17
union
select l.*
from lineup l, team t 
where t.team_id = l.team_id
and game_id = 18





create view final_four_players as 
select l.min,ffg.*
from final_four_games ffg, lineup l
where ffg.game_id = l.game_id
and ffg.team_id = l.team_id
and ffg.lineup_id = l.lineup_id


\copy (select * from player_play_types where team_name like '%Illinois Tech%' or team_name like '%Milwaukee School%' or team_name like '%Aurora%' or team_name like 'Concordia (WI) Falcons') to 'final_four_player_types.csv' csv header;


create view final_four_player_cumulatives as 

select t.team_name, p.player_name, pc.*
from team t, player p, player_cumulative pc
where t.team_id = p.team_id
and p.player_id = pc.player_id
and pc.uploaded_date='2019-02-21'
and t.team_name like '%Illinois Tech%'
union
select t.team_name, p.player_name, pc.*
from team t, player p, player_cumulative pc
where t.team_id = p.team_id
and p.player_id = pc.player_id
and pc.uploaded_date='2019-02-21'
and t.team_name like '%Milwaukee School%'
union
select t.team_name, p.player_name, pc.*
from team t, player p, player_cumulative pc
where t.team_id = p.team_id
and p.player_id = pc.player_id
and pc.uploaded_date='2019-02-21'
and t.team_name like '%Concordia (WI) Falcons%'
union
select t.team_name, p.player_name, pc.*
from team t, player p, player_cumulative pc
where t.team_id = p.team_id
and p.player_id = pc.player_id
and pc.uploaded_date='2019-02-21'
and t.team_name like '%Aurora%'



create view sum_final_four_players as
select team_id,player_name,game_name,sum(min) as min,sum(ast) as ast, sum(block) as block, sum(defreb) as defreb, 
sum(fga) as fga, sum(fg_made) as fg_made, sum(fg_miss) as fg_miss, sum(fta) as fta, sum(ft_made) as ft_made, sum(ft_miss) as ft_miss, 
sum(foul) as foul, sum(offreb) as offreb, sum(pts) as pts, sum(stl) as stl, sum(three_fga) as three_fga, sum(three_fg_made) as three_fg_made, 
sum(three_fg_miss) as three_fg_miss, sum(ttlreb) as ttlreb, sum(turnover) as turnover, sum(two_fga) as two_fga, 
sum(two_fg_made) as two_fga_made, sum(two_fg_miss) as two_fg_miss
from final_four_players 
group by team_id,player_name,game_name
having game_name like '%Hawks vs Milwaukee%'

create view final_four_player_stats as 
select team_name as team_name,ffpc.uploaded_date,ffpc.gp as gp,
ffpc.min as avg_min,ffpc.sst as avg_sst,ffpc.sstexpts as avg_sstexpts,ffpc.pts as avg_pts,ffpc.ast as avg_ast,
ffpc.turnover as avg_turnover,ffpc.ast_turnover_ratio as avg_ast_turnover_ratio,ffpc.stl as avg_stl,ffpc.stlpos as avg_stlpos,
ffpc.blk as avg_blk,ffpc.ttlreb as avg_ttlreb,ffpc.offreb as avg_offreb,ffpc.defreb as avg_defreb,ffpc.fga as avg_fga,
ffpc.fg_made as avg_fg_made,ffpc.fg_miss as avg_fg_miss,ffpc.fg as avg_fg,ffpc.adjusted_fg as avg_adjusted_fg,
ffpc.two_fga as avg_two_fga,ffpc.two_fg_made as avg_two_fg_made,ffpc.two_fg_miss as avg_two_fg_miss,
ffpc.two_fg as avg_two_fg,ffpc.three_fga as avg_three_fga,ffpc.three_fg_made as avg_three_fg_made,
ffpc.three_fg_miss as avg_three_fg_miss,ffpc.three_fg as avg_three_fg,ffpc.fta as avg_fta,
ffpc.ft_made as avg_ft_made,ffpc.ft_miss as avg_ft_miss,ffpc.ft as avg_ft,ffpc.andone as avg_andone,
ffpc.pftkn as avg_pftkn,ffpc.pfcom as avg_pfcom,sffp.*
from final_four_player_cumulatives ffpc, sum_final_four_players as sffp
where ffpc.team_id = sffp.team_id
and ffpc.player_name = sffp.player_name 


create view final_four_players_all_stats as 

\copy (select ppt.format_name,ppt.category_name,ppt.element_name,ppt.format_id,ppt.category_id,ppt.element_id,ppt.player_id,ppt.percentage_time,ppt.poss_per_game,ppt.points,ppt.ppp,ppt.rank,ppt.rating,ppt.fg_miss,ppt.fg_made,ppt.fga,ppt.fg,ppt.adjusted_fg,ppt.percent_turnover,ppt.percent_ft,ppt.percent_shooting_foul,ppt.percent_score,ffps.* from player_play_types ppt, final_four_player_stats ffps where ppt.team_name = ffps.team_name and ppt.player_name = ffps.player_name) to 'final_four_all_stats.csv' csv header;

