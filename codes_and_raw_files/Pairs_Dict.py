Metrics_Dict = {
	"plusminus" : ['high','sum(plusminus)','plusminus','Net performance Evaluation Metric'],
	"ast_rate": ['high','sum(ast)/NULLIF(sum(min),0)','ast_rate','Assist(s) per minute'],
	"block_rate": ['high','sum(block)/NULLIF(sum(min),0)','block_rate','Block(s) per minute'],
	"def_reb_rate" : ['high','sum(defreb)/NULLIF((sum(defreb)+sum(oppo_offreb)),0)','deffensive_rebound_rate','def_rebound/(def_rebound+opponent_off_rebound'],
	"off_reb_rate" : ['high','sum(offreb)/NULLIF((sum(offreb)+sum(oppo_defreb)),0)','offensive_rebound_rate','off_rebound/(off_rebound+opponent_def_rebound'],
	"free_throw_rate": ['high','sum(fta)/NULLIF(sum(min),0)','free_throw_rate','number of free throws earned per minute'],
	"free_throw_percentage" :['high','sum(ft_made)/NULLIF(sum(fta),0)','free_throw_percentage','average free throw percentage'],
	"three_point_rate": ['high','sum(three_fga)/NULLIF(sum(min),0)','three_point_rate','number of 3 point attempts per minute'],
	"three_point_percentage":['high','sum(three_fg_made)/NULLIF(sum(three_fga),0)','three_point_percentage','average 3 point percentage'],
	"foul_rate": ['low','sum(foul)/NULLIF(sum(min),0)','foul_rate','number of fouls committed per minute'],
	"tournover_rate":['low','sum(turnover)/NULLIF(sum(min),0)','four_rate','number of turnovers committed per min']
}

