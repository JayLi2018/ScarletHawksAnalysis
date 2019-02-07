CREATE TABLE Team
(
	Team_ID int,
	Team_Name varchar(50),

	Primary Key(Team_ID)
);

CREATE TABLE Player
(
	Player_Name varchar(50),
	Player_ID int,
	Team_ID INT,

	Primary Key(Player_ID),
	Foreign key(Team_ID) References TEAM(Team_ID)
);

CREATE TABLE Format
(
	Format_ID int,
	Format_Name CHAR(20),

	Primary Key(Format_ID)
);

CREATE TABLE Element
(
	Element_ID int,
	Element_Name CHAR(50),

	Primary Key(Element_ID)
);

CREATE TABLE Category
(
	Category_ID int,
	Category_Name CHAR(50),

	Primary Key(Category_ID)
);

CREATE TABLE Team_Average
(   
	Format_ID int,
	Category_ID int,
	Element_ID int,
	Team_ID int,
	Uploaded_Date Date,
	Percentage_Time FLOAT,
	Poss_Per_Game FLOAT,
	Points FLOAT,
	PPP FLOAT,
	Rank FLOAT,
	Rating CHAR(30),
	FG_miss FLOAT,
	FG_Made FLOAT,
	FGA FLOAT,
	FG FLOAT,
	Adjusted_FG FLOAT,
	Percent_Turnover FLOAT,
	Percent_FT FLOAT,
	Percent_Shooting_Foul FLOAT,
	Percent_Score FLOAT,
    
    Foreign Key(Format_ID) References Format(Format_ID),
    Foreign Key(Category_ID) References Category(Category_ID),
	Foreign Key(Element_ID) References Element(Element_ID),
	Foreign Key(Team_ID) References TEAM(Team_ID)
);


CREATE TABLE Player_Average
(	
	Format_ID int,
	Category_ID int,
	Element_ID int,
	Player_ID int,
	Uploaded_Date Date,
	Percentage_Time FLOAT,
	Poss_Per_Game FLOAT,
	Points FLOAT,
	PPP FLOAT,
	Rank FLOAT,
	Rating CHAR(30),
	FG_miss FLOAT,
	FG_Made FLOAT,
	FGA FLOAT,
	FG FLOAT,
	Adjusted_FG FLOAT,
	Percent_Turnover FLOAT,
	Percent_FT FLOAT,
	Percent_Shooting_Foul FLOAT,
	Percent_Score FLOAT,

    Foreign Key(Format_ID) References Format(Format_ID),
    Foreign Key(Category_ID) References Category(Category_ID),
	Foreign Key(Element_ID) References Element(Element_ID),
	Foreign Key(Player_ID) References Player(Player_ID)
);


CREATE TABLE GAME
(
	Game_ID int,
	Uploaded_Date Date,
	Home_Team_ID int,
	Away_Team_ID int,

	Primary Key (Game_ID),

	Foreign Key (Home_Team_ID) References Team(Team_ID),
	Foreign Key (Away_Team_ID) References Team(Team_ID)
);

CREATE TABLE Player_Game
(
	Ast FLOAT,
	Block FLOAT,
	DefReb FLOAT,
	FGA FLOAT,
	FG_Made FLOAT,
	FG_miss FLOAT,
	FTA FLOAT,
	FT_Made FLOAT,
	FT_miss FLOAT,
	Foul FLOAT,
	Game_ID int,
	Lineup_ID int,
	OffReb FLOAT, 
	Player_ID int,
	Pts FLOAT,
	Stl FLOAT,
	Three_FGA FLOAT,
	Three_FG_Made FLOAT,
	Three_FG_miss FLOAT,
	TtlReb FLOAT,
	Turnover FLOAT,
	Two_FGA FLOAT,
	Two_FG_Made FLOAT,
	Two_FG_miss FLOAT,

	Foreign Key (Player_ID) References Player(Player_ID),
	Foreign Key (Game_ID) References Game(Game_ID)
);	

CREATE TABLE Lineup
(
	Ast float,
	Block float,
	DefReb float,
	FGA float,
	FG_Made float,
	FG_miss float,
	FTA float,
	FT_Made float,
	FT_miss float,
	Foul float,
	Started float,
	Game_ID INT,
	Lineup_ID INT,
	Lineup_Players varchar(200),
	Lineup_Score float,
	Min float,
	OffReb float,
	Oppo_Ast float,
	Oppo_Block float,
	Oppo_DefReb float,
	Oppo_FGA float,
	Oppo_FG_Made float,
	Oppo_FG_miss float,
	Oppo_FTA float,
	Oppo_FT_Made float,
	Oppo_FT_miss float,
	Oppo_Foul float,
	Oppo_OffReb float,
	Oppo_Score float,
	Oppo_Stl float,
	Oppo_Three_FGA float,
	Oppo_Three_FG_Made float,
	Oppo_Three_FG_miss float,
	Oppo_TtlReb float,
	Oppo_Turnover float,
	Oppo_Two_FGA float,
	Oppo_Two_FG_Made float,
	Oppo_Two_FG_miss float,
	PlusMinus float,
	Stl float,
	Three_FGA float,
	Three_FG_Made float,
	Three_FG_miss float,
	Ended float,
	TtlReb float,
	Turnover float,
	Two_FGA float,
	Two_FG_Made float,
	Two_FG_miss float,
	session_number float,
	Team_ID INT,


	Foreign Key (Game_ID) References Game(Game_ID),
	Foreign Key (Team_ID) References Team(Team_ID)
);



CREATE TABLE GAME_TRACK
(
	Game_ID int,
	Score_Difference int,
	session_number int,
	Time float,

	Foreign Key (Game_ID) References Game(Game_ID)
);

CREATE TABLE PLAYER_CUMULATIVE
(
	Team_ID INT,
	Uploaded_Date DATE,
	Player_ID INT,
	GP INT,
	Min FLOAT,
	SST FLOAT,
	SSTexPts FLOAT,
	Pts FLOAT,
	Ast FLOAT,
	Turnover FLOAT, 
	Ast_Turnover_Ratio FLOAT,
	Stl FLOAT,
	StlPos FLOAT,
	Blk FLOAT,
	TtlReb FLOAT,
	OffReb FLOAT,
	DefReb FLOAT,
	FGA FLOAT,
	FG_Made FLOAT,
	FG_miss FLOAT,
	FG FLOAT,
	adjusted_FG FLOAT,
	Two_FGA FLOAT,
	Two_FG_Made FLOAT,
	Two_FG_miss FLOAT,
	Two_FG FLOAT,
	Three_FGA FLOAT,
	Three_FG_Made FLOAT,
	Three_FG_miss FLOAT,
	Three_FG FLOAT,
	FTA FLOAT,
	FT_Made FLOAT,
	FT_miss FLOAT,
	FT FLOAT,
	AndOne FLOAT,
	PFTkn FLOAT,
	PFCom FLOAT,

	Foreign KEY(Team_ID) References TEAM(Team_ID),
	Foreign Key(Player_ID) References Player(Player_ID)

);

CREATE TABLE Update_Comment
(
	Uploaded_Date date,
	Comment TEXT
)





COPY Team(Team_ID,Team_Name) from '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/Team.csv' DELIMITER ',' CSV HEADER NULL AS '-';
COPY Player(Player_Name,Player_ID,Team_ID) from '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/player.csv' DELIMITER ',' CSV HEADER NULL AS '-';
COPY Format(Format_ID,Format_Name) from '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/format.csv' DELIMITER ',' CSV HEADER NULL AS '-';
COPY Element(Element_Name,Element_ID) from '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/Element.csv' DELIMITER ',' CSV HEADER NULL AS '-';
COPY Category(Category_ID,Category_Name) from '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/Category.csv' DELIMITER ',' CSV HEADER NULL AS '-';
\COPY Team_Average(Uploaded_Date,Percentage_Time,Poss_Per_Game,Points,PPP,Rank,Rating,FG_miss,FG_Made,FGA,FG,Adjusted_FG,Percent_Turnover,Percent_FT,Percent_Shooting_Foul,Percent_Score,Format_ID,Category_ID,Element_ID,Team_ID) from '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/Merges/ta.csv' DELIMITER ',' CSV HEADER NULL AS '-';
\COPY Player_Average(Uploaded_Date,Percentage_Time,Poss_Per_Game,Points,PPP,Rank,Rating,FG_miss,FG_Made,FGA,FG,Adjusted_FG,Percent_Turnover,Percent_FT,Percent_Shooting_Foul,Percent_Score,Format_ID,Category_ID,Element_ID,Player_ID) from '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/Merges/pa.csv' DELIMITER ',' CSV HEADER NULL AS '-';
COPY GAME(Game_ID,Uploaded_Date,Home_Team_ID,Away_Team_ID) from '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/game.csv' DELIMITER ',' CSV HEADER NULL AS '-';
\COPY Player_Game(Ast,Block,DefReb,FGA,FG_Made,FG_miss,FTA,FT_Made,FT_miss,Foul,Game_ID,Lineup_ID,OffReb,Pts,Stl,Three_FGA,Three_FG_Made,Three_FG_miss,TtlReb,Turnover,Two_FGA,Two_FG_Made,Two_FG_miss,Player_ID) from '/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/1.26 Package/Player_Games.csv' DELIMITER ',' CSV HEADER NULL AS '-';
\COPY Lineup(Ast,Block,DefReb,FGA,FG_Made,FG_miss,FTA,FT_Made,FT_miss,Foul,Started,Game_ID,Lineup_ID,Lineup_Players,Lineup_Score,Min,OffReb,Oppo_Ast,Oppo_Block,Oppo_DefReb,Oppo_FGA,Oppo_FG_Made,Oppo_FG_miss,Oppo_FTA,Oppo_FT_Made,Oppo_FT_miss,Oppo_Foul,Oppo_OffReb,Oppo_Score,Oppo_Stl,Oppo_Three_FGA,Oppo_Three_FG_Made,Oppo_Three_FG_miss,Oppo_TtlReb,Oppo_Turnover,Oppo_Two_FGA,Oppo_Two_FG_Made,Oppo_Two_FG_miss,PlusMinus,Stl,Three_FGA,Three_FG_Made,Three_FG_miss,Ended,TtlReb,Turnover,Two_FGA,Two_FG_Made,Two_FG_miss,session_number,Team_ID) from '/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/1.26 Package/Lineups.csv' DELIMITER ',' CSV HEADER NULL AS '-';
\COPY GAME_TRACK(Game_ID,Score_Difference,Session_number,Time) from 'Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/GAME_CSVs/1.9/Lutheran_Wis_tracker.csv' DELIMITER ',' CSV HEADER NULL AS '-';
\COPY PLAYER_CUMULATIVE(GP,Min,SST,SSTexPts,Pts,Ast,Turnover,Ast_Turnover_Ratio,Stl,StlPos,Blk,TtlReb,OffReb,DefReb,FGA,FG_Made,FG_miss,FG,adjusted_FG,Two_FGA,Two_FG_Made,Two_FG_miss,Two_FG,Three_FGA,Three_FG_Made,Three_FG_miss,Three_FG,FTA,FT_Made,FT_miss,FT,AndOne,PFTkn,PFCom,Uploaded_Date,Player_ID,Team_ID) from '/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/1.26 Package/Player_Cumulative_Raw/Player_Cumulative.csv' DELIMITER ',' CSV HEADER NULL AS '-';











copy TEAM_GAME_STATUS(Team_Game_Status_ID,TEAM_Game_Status_Name) from 'D:\Final_Version_Tables\Team_Game_Status.csv' DELIMITER ',' CSV HEADER
