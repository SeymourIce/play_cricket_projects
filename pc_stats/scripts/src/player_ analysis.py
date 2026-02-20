from pc_stats.scripts.src.utility_functions import *

name = "Chris Morris"

filtered_player_details = lhcc.player_details[lhcc.player_details['player_name']==name]

filtered_player_details.to_csv(f"{name.lower().replace(' ','_')}_data.csv", index=False)


# TODO - get_player_analysis()
# - Enter club id and player name
# - Optional to select teams
# - Check last updated date
# - Pull new matches