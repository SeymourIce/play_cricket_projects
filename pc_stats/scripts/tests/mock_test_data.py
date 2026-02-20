import pandas as pd

matches_summary = {
    "matches": [
        {
            "id": 6538073,
            "status": "New",
            "published": "Yes",
            "last_updated": "01/04/2024",
            "league_name": "",
            "league_id": "",
            "competition_name": "",
            "competition_id": "",
            "competition_type": "Friendly",
            "match_type": "Limited Overs",
            "game_type": "Standard",
            "season": "2024",
            "match_date": "20/04/2024",
            "match_time": "13:30",
            "ground_name": "Ley_Hill_CC",
            "ground_id": "11691",
            "ground_latitude": "51.7067612",
            "ground_longitude": "-0.5685045",
            "home_club_name": "Ley_Hill_CC",
            "home_team_name": "1st XI",
            "home_team_id": "54824",
            "home_club_id": "3931",
            "away_club_name": "Rickmansworth CC",
            "away_team_name": "1st XI",
            "away_team_id": "159861",
            "away_club_id": "5321",
            "umpire_1_name": "",
            "umpire_1_id": "",
            "umpire_2_name": "",
            "umpire_2_id": "",
            "umpire_3_name": "",
            "umpire_3_id": "",
            "referee_name": "",
            "referee_id": "",
            "scorer_1_name": "",
            "scorer_1_id": "",
            "scorer_2_name": "",
            "scorer_2_id": ""
        },
        {
            "id": 6538106,
            "status": "New",
            "published": "Yes",
            "last_updated": "21/04/2024",
            "league_name": "",
            "league_id": "",
            "competition_name": "",
            "competition_id": "",
            "competition_type": "Friendly",
            "match_type": "Limited Overs",
            "game_type": "Standard",
            "season": "2024",
            "match_date": "21/04/2024",
            "match_time": "13:30",
            "ground_name": "Ley_Hill_CC",
            "ground_id": "11691",
            "ground_latitude": "51.7067612",
            "ground_longitude": "-0.5685045",
            "home_club_name": "Ley_Hill_CC",
            "home_team_name": "Sunday 1st XI",
            "home_team_id": "216373",
            "home_club_id": "3931",
            "away_club_name": "Soho Cricket Collective",
            "away_team_name": "Friendly XI",
            "away_team_id": "207493",
            "away_club_id": "12834",
            "umpire_1_name": "",
            "umpire_1_id": "",
            "umpire_2_name": "",
            "umpire_2_id": "",
            "umpire_3_name": "",
            "umpire_3_id": "",
            "referee_name": "",
            "referee_id": "",
            "scorer_1_name": "",
            "scorer_1_id": "",
            "scorer_2_name": "",
            "scorer_2_id": ""
        },
        {
            "id": 6244897,
            "status": "New",
            "published": "Yes",
            "last_updated": "27/04/2024",
            "league_name": "",
            "league_id": "",
            "competition_name": "",
            "competition_id": "",
            "competition_type": "Friendly",
            "match_type": "Limited Overs",
            "game_type": "Standard",
            "season": "2024",
            "match_date": "27/04/2024",
            "match_time": "13:30",
            "ground_name": "Holmer Green Cricket Club",
            "ground_id": "7614",
            "ground_latitude": "51.6667141",
            "ground_longitude": "-0.7037339",
            "home_club_name": "Holmer Green CC",
            "home_team_name": "Friendly XI",
            "home_team_id": "316960",
            "home_club_id": "7792",
            "away_club_name": "Ley_Hill_CC",
            "away_team_name": "1st XI",
            "away_team_id": "54824",
            "away_club_id": "3931",
            "umpire_1_name": "",
            "umpire_1_id": "",
            "umpire_2_name": "",
            "umpire_2_id": "",
            "umpire_3_name": "",
            "umpire_3_id": "",
            "referee_name": "",
            "referee_id": "",
            "scorer_1_name": "",
            "scorer_1_id": "",
            "scorer_2_name": "",
            "scorer_2_id": ""
        }
    ]
}
clubs_list = {
    "clubs":[
        {"id":29666,"name":"11 Aces CC","county":"Middlesex","county_id":23,"status":"active","last_updated":"12/04/2025"},
        {"id":3931,"name":"Ley Hill CC","county":"Buckinghamshire","county_id":2,"status":"active","last_updated":"01/04/2025"},
        {"id":4065,"name":"London Colney CC","county":"Hertfordshire","county_id":16,"status":"active","last_updated":"01/04/2025"}
    ]
}

ley_hill_teams = {"teams":[
{"id":54824,"status":"active","last_updated":"11/12/2023","site_id":3931,"team_name":"1st XI","other_team_name":"","nickname":"The Hill","team_captain":"1000955"},
{"id":119465,"status":"active","last_updated":"20/05/2025","site_id":3931,"team_name":"2nd XI","other_team_name":"","nickname":"","team_captain":"5974971"},
{"id":216373,"status":"active","last_updated":"31/01/2020","site_id":3931,"team_name":"Sunday 1st XI","other_team_name":"","nickname":"","team_captain":"1101452"},
{"id":232724,"status":"active","last_updated":"20/05/2025","site_id":3931,"team_name":"Midweek XI","other_team_name":"","nickname":"","team_captain":"1809919"},
{"id":119469,"status":"active","last_updated":"26/02/2024","site_id":3931,"team_name":"Under 17","other_team_name":"","nickname":"","team_captain":""},
{"id":119470,"status":"active","last_updated":"26/02/2024","site_id":3931,"team_name":"Under 15","other_team_name":"","nickname":"","team_captain":""},
{"id":327066,"status":"active","last_updated":"06/02/2023","site_id":3931,"team_name":"Under 14","other_team_name":"","nickname":"","team_captain":""},
{"id":241663,"status":"active","last_updated":"26/02/2024","site_id":3931,"team_name":"Under 13","other_team_name":"","nickname":"","team_captain":""},
{"id":119472,"status":"active","last_updated":"20/05/2025","site_id":3931,"team_name":"Under 12","other_team_name":"","nickname":"","team_captain":""},
{"id":119473,"status":"active","last_updated":"29/02/2024","site_id":3931,"team_name":"Under 11","other_team_name":"","nickname":"","team_captain":""}
]
}

lhcc_all_2025_matches = pd.read_csv('lhcc_get_all_matches.csv')

lhcc_some_2025_matches = pd.read_csv('lhcc_get_3_2025_matches.csv')

empty_matches_summary = {"matches": []}

match_id_list = ['6538073', '6538106', '6244897']

complete_match_details = \
    {"match_details": [
        {
      "id": 5544903,
      "status": "New",
      "published": "Yes",
      "last_updated": "03/07/2023",
      "league_name": "Berkshire, Chilterns and Mid Bucks League",
      "league_id": "391",
      "competition_name": "Championship",
      "competition_id": "109522",
      "competition_type": "League",
      "match_type": "Limited Overs",
      "game_type": "Standard",
      "countdown_cricket": "no",
      "match_id": "5544903",
      "match_date": "01/07/2023",
      "match_time": "13:00",
      "ground_name": "Ley Hill Cricket Club",
      "ground_id": "",
      "home_team_name": "1st XI",
      "home_team_id": "54824",
      "home_club_name": "Ley_Hill_CC",
      "home_club_id": "3931",
      "away_team_name": "1st XI",
      "away_team_id": "66365",
      "away_club_name": "Braywood CC",
      "away_club_id": "1360",
      "umpire_1_name": "Zia Ul Hasan",
      "umpire_1_id": "5874306",
      "umpire_2_name": "Paul Green",
      "umpire_2_id": "1101452",
      "umpire_3_name": "",
      "umpire_3_id": "",
      "referee_name": "",
      "referee_id": "",
      "scorer_1_name": "Nigel Barton",
      "scorer_1_id": "5557784",
      "scorer_2_name": "Freddie Ventham",
      "scorer_2_id": "5552337",
      "toss_won_by_team_id": "54824",
      "toss": "Ley_Hill_CC - 1st XI won the toss and elected to bat",
      "batted_first": "54824",
      "no_of_overs": "45",
      "balls_per_innings": "",
      "no_of_innings": "1",
      "no_of_days": "1",
      "no_of_players": "11",
      "no_of_reserves": "1",
      "result": "W",
      "result_description": "Braywood CC - 1st XI - Won",
      "result_applied_to": "66365",
      "match_notes": "\u003Cp\u003ELey&nbsp;HIll&nbsp;innings:&nbsp;Mudassar&nbsp;Yasin&nbsp;3-32\u003C/p\u003E\r\n\r\n\u003Cp\u003EBraywood&nbsp;innings:&nbsp;Yaser&nbsp;Ahmed&nbsp;83*,&nbsp;Syed&nbsp;Kazmi&nbsp;55\u003C/p\u003E\r\n\r\n\u003Cp\u003E\u003Cstrong\u003ELey&nbsp;Hill&nbsp;CC&nbsp;1st&nbsp;XI&nbsp;Innings\u003C/strong\u003E\u003Cbr /\u003E\r\n6.7&nbsp;Ley&nbsp;Hill&nbsp;CC&nbsp;1st&nbsp;XI:&nbsp;50&nbsp;runs&nbsp;in&nbsp;7.0&nbsp;overs,&nbsp;31&nbsp;minutes,&nbsp;14&nbsp;extras\u003Cbr /\u003E\r\n20.1&nbsp;Ley&nbsp;Hill&nbsp;CC&nbsp;1st&nbsp;XI:&nbsp;100&nbsp;runs&nbsp;in&nbsp;20.1&nbsp;overs,&nbsp;87&nbsp;minutes,&nbsp;21&nbsp;extras\u003Cbr /\u003E\r\n36.4&nbsp;Ley&nbsp;Hill&nbsp;CC&nbsp;1st&nbsp;XI:&nbsp;150&nbsp;runs&nbsp;in&nbsp;36.4&nbsp;overs,&nbsp;146&nbsp;minutes,&nbsp;24&nbsp;extras\u003Cbr /\u003E\r\n\u003Cbr /\u003E\r\n\u003Cstrong\u003EBraywood&nbsp;CC&nbsp;1st&nbsp;XI&nbsp;Innings\u003C/strong\u003E\u003Cbr /\u003E\r\n9.3&nbsp;1st&nbsp;Wicket:&nbsp;50&nbsp;runs&nbsp;in&nbsp;58&nbsp;balls,&nbsp;36&nbsp;minutes,&nbsp;Syed&nbsp;Kazmi&nbsp;24&nbsp;(32),&nbsp;Yaser&nbsp;Ahmed&nbsp;24&nbsp;(26),&nbsp;3&nbsp;extras\u003Cbr /\u003E\r\n9.3&nbsp;Braywood&nbsp;CC&nbsp;1st&nbsp;XI:&nbsp;50&nbsp;runs&nbsp;in&nbsp;9.3&nbsp;overs,&nbsp;36&nbsp;minutes,&nbsp;3&nbsp;extras\u003Cbr /\u003E\r\n17.1&nbsp;1st&nbsp;Wicket:&nbsp;100&nbsp;runs&nbsp;in&nbsp;105&nbsp;balls,&nbsp;64&nbsp;minutes,&nbsp;Syed&nbsp;Kazmi&nbsp;46&nbsp;(55),&nbsp;Yaser&nbsp;Ahmed&nbsp;49&nbsp;(50),&nbsp;8&nbsp;extras\u003Cbr /\u003E\r\n17.1&nbsp;Braywood&nbsp;CC&nbsp;1st&nbsp;XI:&nbsp;100&nbsp;runs&nbsp;in&nbsp;17.1&nbsp;overs,&nbsp;64&nbsp;minutes,&nbsp;8&nbsp;extras\u003Cbr /\u003E\r\n17.2&nbsp;Yaser&nbsp;Ahmed:&nbsp;50&nbsp;runs&nbsp;in&nbsp;51&nbsp;balls,&nbsp;64&nbsp;minutes&nbsp;(9x4,&nbsp;1x6)\u003Cbr /\u003E\r\n19.2&nbsp;Syed&nbsp;Kazmi:&nbsp;50&nbsp;runs&nbsp;in&nbsp;60&nbsp;balls,&nbsp;69&nbsp;minutes&nbsp;(6x4,&nbsp;3x6)\u003Cbr /\u003E\r\n22.4&nbsp;Braywood&nbsp;CC&nbsp;1st&nbsp;XI:&nbsp;150&nbsp;runs&nbsp;in&nbsp;22.4&nbsp;overs,&nbsp;83&nbsp;minutes,&nbsp;10&nbsp;extras\u003C/p\u003E\r\n",
      "points": [
        {
          "team_id": 54824,
          "game_points": "0",
          "penalty_points": "-5.0",
          "bonus_points_together": "3.0",
          "bonus_points_batting": "3.0",
          "bonus_points_bowling": "0.0",
          "bonus_points_2nd_innings_together": ""
        },
        {
          "team_id": 66365,
          "game_points": "35",
          "penalty_points": "-5.0",
          "bonus_points_together": "0.0",
          "bonus_points_batting": "0.0",
          "bonus_points_bowling": "0.0",
          "bonus_points_2nd_innings_together": ""
        }
      ],
      "match_result_types": [
        [
          "Ley_Hill_CC - 1st XI - Won",
          "876736#54824"
        ],
        [
          "Braywood CC - 1st XI - Won",
          "876736#66365"
        ],
        [
          "Tied",
          876742],
        [
          "Cancelled",
          876738],
        [
          "Abandoned",
          876739],
        [
          "Ley_Hill_CC - 1st XI - Conceded",
          "876740#66365"
        ],
        [
          "Braywood CC - 1st XI - Conceded",
          "876741#54824"
        ],
        [
          "Match In Progress",
          14]
      ],
      "players": [
        {
          "home_team": [
            {
              "position": 1,
              "player_name": "Craig Peterson",
              "player_id": 3858366,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 2,
              "player_name": "Raheel Khan",
              "player_id": 5402781,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 3,
              "player_name": "Brad Norton",
              "player_id": 4252538,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 4,
              "player_name": "Callum Wilson",
              "player_id": 5497375,
              "captain": 'true',
              "wicket_keeper": 'false'
            },
            {
              "position": 5,
              "player_name": "Yusuf Khan",
              "player_id": 4940735,
              "captain": 'false',
              "wicket_keeper": 'true'
            },
            {
              "position": 6,
              "player_name": "Ted Sussum",
              "player_id": 4951412,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 7,
              "player_name": "Jamie Valentine",
              "player_id": 4524064,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 8,
              "player_name": "Rob Jaycocks",
              "player_id": 5973076,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 9,
              "player_name": "Scott Peterson",
              "player_id": 5483704,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 10,
              "player_name": "Douglas Petrie",
              "player_id": 1917305,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 11,
              "player_name": "Joe Yerrell",
              "player_id": 6044911,
              "captain": 'false',
              "wicket_keeper": 'false'
            }
          ]
        },
        {
          "away_team": [
            {
              "position": 1,
              "player_name": "Syed Kazmi",
              "player_id": 4999167,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 2,
              "player_name": "Mudassar Yasin",
              "player_id": 4979675,
              "captain": 'true',
              "wicket_keeper": 'false'
            },
            {
              "position": 3,
              "player_name": "Yaser Ahmed",
              "player_id": 3786374,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 4,
              "player_name": "Arslan Yaseen",
              "player_id": 5078586,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 5,
              "player_name": "Asad Munawer",
              "player_id": 5594210,
              "captain": 'false',
              "wicket_keeper": 'true'
            },
            {
              "position": 6,
              "player_name": "Shiny Johnston",
              "player_id": 4080244,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 7,
              "player_name": "Riasat Swapnil",
              "player_id": 5352655,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 8,
              "player_name": "Usman Rasheed",
              "player_id": 4698153,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 9,
              "player_name": "Haseeb Muhammad",
              "player_id": 5818403,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 10,
              "player_name": "Ahsan Malik",
              "player_id": 3873460,
              "captain": 'false',
              "wicket_keeper": 'false'
            },
            {
              "position": 11,
              "player_name": "Raja Ahsan",
              "player_id": 4495642,
              "captain": 'false',
              "wicket_keeper": 'false'
            }
          ]
        }
      ],
      "innings": [
        {
          "team_batting_name": "Ley_Hill_CC - 1st XI",
          "team_batting_id": "54824",
          "innings_number": 1,
          "extra_byes": "1",
          "extra_leg_byes": "13",
          "extra_wides": "7",
          "extra_no_balls": "3",
          "extra_penalty_runs": "0",
          "penalties_runs_awarded_in_other_innings": "0",
          "total_extras": "24",
          "runs": "159",
          "wickets": "10",
          "overs": "39",
          "balls": "",
          "declared": 'false',
          "forfeited_innings": 'false',
          "revised_target_runs": "",
          "revised_target_overs": "45.0",
          "revised_target_balls": "",
          "bat": [
            {
              "position": "1",
              "batsman_name": "Craig Peterson",
              "batsman_id": "3858366",
              "how_out": "lbw",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Mudassar Yasin",
              "bowler_id": "4979675",
              "runs": "15",
              "fours": "3",
              "sixes": "0",
              "balls": "13"
            },
            {
              "position": "2",
              "batsman_name": "Raheel Khan",
              "batsman_id": "5402781",
              "how_out": "ct",
              "fielder_name": "Yaser Ahmed",
              "fielder_id": "3786374",
              "bowler_name": "Arslan Yaseen",
              "bowler_id": "5078586",
              "runs": "14",
              "fours": "3",
              "sixes": "0",
              "balls": "16"
            },
            {
              "position": "3",
              "batsman_name": "Callum Wilson",
              "batsman_id": "5497375",
              "how_out": "ct",
              "fielder_name": "Asad Munawer",
              "fielder_id": "5594210",
              "bowler_name": "Ahsan Malik",
              "bowler_id": "3873460",
              "runs": "36",
              "fours": "6",
              "sixes": "0",
              "balls": "39"
            },
            {
              "position": "4",
              "batsman_name": "Yusuf Khan",
              "batsman_id": "4940735",
              "how_out": "ct",
              "fielder_name": "Asad Munawer",
              "fielder_id": "5594210",
              "bowler_name": "Mudassar Yasin",
              "bowler_id": "4979675",
              "runs": "3",
              "fours": "0",
              "sixes": "0",
              "balls": "20"
            },
            {
              "position": "5",
              "batsman_name": "Ted Sussum",
              "batsman_id": "4951412",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Mudassar Yasin",
              "bowler_id": "4979675",
              "runs": "33",
              "fours": "5",
              "sixes": "0",
              "balls": "79"
            },
            {
              "position": "6",
              "batsman_name": "Brad Norton",
              "batsman_id": "4252538",
              "how_out": "ct",
              "fielder_name": "Mudassar Yasin",
              "fielder_id": "4979675",
              "bowler_name": "Ahsan Malik",
              "bowler_id": "3873460",
              "runs": "4",
              "fours": "1",
              "sixes": "0",
              "balls": "2"
            },
            {
              "position": "7",
              "batsman_name": "Rob Jaycocks",
              "batsman_id": "5973076",
              "how_out": "ct",
              "fielder_name": "Asad Munawer",
              "fielder_id": "5594210",
              "bowler_name": "Haseeb Muhammad",
              "bowler_id": "5818403",
              "runs": "10",
              "fours": "1",
              "sixes": "0",
              "balls": "31"
            },
            {
              "position": "8",
              "batsman_name": "Jamie Valentine",
              "batsman_id": "4524064",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Shiny Johnston",
              "bowler_id": "4080244",
              "runs": "2",
              "fours": "0",
              "sixes": "0",
              "balls": "12"
            },
            {
              "position": "9",
              "batsman_name": "Scott Peterson",
              "batsman_id": "5483704",
              "how_out": "st",
              "fielder_name": "Asad Munawer",
              "fielder_id": "5594210",
              "bowler_name": "Shiny Johnston",
              "bowler_id": "4080244",
              "runs": "0",
              "fours": "0",
              "sixes": "0",
              "balls": "2"
            },
            {
              "position": "10",
              "batsman_name": "Douglas Petrie",
              "batsman_id": "1917305",
              "how_out": "not out",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "18",
              "fours": "3",
              "sixes": "0",
              "balls": "19"
            },
            {
              "position": "11",
              "batsman_name": "Joe Yerrell",
              "batsman_id": "6044911",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Shiny Johnston",
              "bowler_id": "4080244",
              "runs": "0",
              "fours": "0",
              "sixes": "0",
              "balls": "4"
            }
          ],
          "fow": [
            {
              "runs": "28",
              "wickets": 1,
              "batsman_out_name": "Craig Peterson",
              "batsman_out_id": "3858366",
              "batsman_in_name": "Raheel Khan",
              "batsman_in_id": "5402781",
              "batsman_in_runs": "6"
            },
            {
              "runs": "37",
              "wickets": 2,
              "batsman_out_name": "Raheel Khan",
              "batsman_out_id": "5402781",
              "batsman_in_name": "Callum Wilson",
              "batsman_in_id": "5497375",
              "batsman_in_runs": "0"
            },
            {
              "runs": "68",
              "wickets": 3,
              "batsman_out_name": "Yusuf Khan",
              "batsman_out_id": "4940735",
              "batsman_in_name": "Callum Wilson",
              "batsman_in_id": "5497375",
              "batsman_in_runs": "19"
            },
            {
              "runs": "90",
              "wickets": 4,
              "batsman_out_name": "Callum Wilson",
              "batsman_out_id": "5497375",
              "batsman_in_name": "Ted Sussum",
              "batsman_in_id": "4951412",
              "batsman_in_runs": "2"
            },
            {
              "runs": "94",
              "wickets": 5,
              "batsman_out_name": "Brad Norton",
              "batsman_out_id": "4252538",
              "batsman_in_name": "Ted Sussum",
              "batsman_in_id": "4951412",
              "batsman_in_runs": "2"
            },
            {
              "runs": "113",
              "wickets": 6,
              "batsman_out_name": "Rob Jaycocks",
              "batsman_out_id": "5973076",
              "batsman_in_name": "Ted Sussum",
              "batsman_in_id": "4951412",
              "batsman_in_runs": "10"
            },
            {
              "runs": "117",
              "wickets": 7,
              "batsman_out_name": "Jamie Valentine",
              "batsman_out_id": "4524064",
              "batsman_in_name": "Ted Sussum",
              "batsman_in_id": "4951412",
              "batsman_in_runs": "12"
            },
            {
              "runs": "117",
              "wickets": 8,
              "batsman_out_name": "Scott Peterson",
              "batsman_out_id": "5483704",
              "batsman_in_name": "Ted Sussum",
              "batsman_in_id": "4951412",
              "batsman_in_runs": "12"
            },
            {
              "runs": "154",
              "wickets": 9,
              "batsman_out_name": "Ted Sussum",
              "batsman_out_id": "4951412",
              "batsman_in_name": "Douglas Petrie",
              "batsman_in_id": "1917305",
              "batsman_in_runs": "13"
            },
            {
              "runs": "159",
              "wickets": 10,
              "batsman_out_name": "Joe Yerrell",
              "batsman_out_id": "6044911",
              "batsman_in_name": "Douglas Petrie",
              "batsman_in_id": "1917305",
              "batsman_in_runs": "18"
            }
          ],
          "bowl": [
            {
              "bowler_name": "Arslan Yaseen",
              "bowler_id": "5078586",
              "overs": "9",
              "maidens": "0",
              "runs": "43",
              "wides": "2",
              "wickets": "1",
              "no_balls": "0"
            },
            {
              "bowler_name": "Mudassar Yasin",
              "bowler_id": "4979675",
              "overs": "9",
              "maidens": "2",
              "runs": "32",
              "wides": "4",
              "wickets": "3",
              "no_balls": "1"
            },
            {
              "bowler_name": "Ahsan Malik",
              "bowler_id": "3873460",
              "overs": "6",
              "maidens": "1",
              "runs": "30",
              "wides": "1",
              "wickets": "2",
              "no_balls": "1"
            },
            {
              "bowler_name": "Haseeb Muhammad",
              "bowler_id": "5818403",
              "overs": "6",
              "maidens": "0",
              "runs": "14",
              "wides": "0",
              "wickets": "1",
              "no_balls": "1"
            },
            {
              "bowler_name": "Shiny Johnston",
              "bowler_id": "4080244",
              "overs": "6",
              "maidens": "3",
              "runs": "11",
              "wides": "0",
              "wickets": "3",
              "no_balls": "0"
            },
            {
              "bowler_name": "Raja Ahsan",
              "bowler_id": "4495642",
              "overs": "3",
              "maidens": "0",
              "runs": "15",
              "wides": "0",
              "wickets": "0",
              "no_balls": "0"
            }
          ]
        },
        {
          "team_batting_name": "Braywood CC - 1st XI",
          "team_batting_id": "66365",
          "innings_number": 1,
          "extra_byes": "1",
          "extra_leg_byes": "3",
          "extra_wides": "3",
          "extra_no_balls": "3",
          "extra_penalty_runs": "0",
          "penalties_runs_awarded_in_other_innings": "0",
          "total_extras": "10",
          "runs": "162",
          "wickets": "1",
          "overs": "23.1",
          "balls": "",
          "declared": 'false',
          "forfeited_innings": 'false',
          "revised_target_runs": "",
          "revised_target_overs": "45.0",
          "revised_target_balls": "",
          "bat": [
            {
              "position": "1",
              "batsman_name": "Syed Kazmi",
              "batsman_id": "4999167",
              "how_out": "ct",
              "fielder_name": "Jamie Valentine",
              "fielder_id": "4524064",
              "bowler_name": "Raheel Khan",
              "bowler_id": "5402781",
              "runs": "55",
              "fours": "7",
              "sixes": "3",
              "balls": "65"
            },
            {
              "position": "2",
              "batsman_name": "Yaser Ahmed",
              "batsman_id": "3786374",
              "how_out": "not out",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "83",
              "fours": "12",
              "sixes": "3",
              "balls": "71"
            },
            {
              "position": "3",
              "batsman_name": "Arslan Yaseen",
              "batsman_id": "5078586",
              "how_out": "not out",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "14",
              "fours": "0",
              "sixes": "2",
              "balls": "6"
            },
            {
              "position": "4",
              "batsman_name": "Mudassar Yasin",
              "batsman_id": "4979675",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "5",
              "batsman_name": "Asad Munawer",
              "batsman_id": "5594210",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "6",
              "batsman_name": "Shiny Johnston",
              "batsman_id": "4080244",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "7",
              "batsman_name": "Riasat Swapnil",
              "batsman_id": "5352655",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "8",
              "batsman_name": "Usman Rasheed",
              "batsman_id": "4698153",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "9",
              "batsman_name": "Haseeb Muhammad",
              "batsman_id": "5818403",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "10",
              "batsman_name": "Ahsan Malik",
              "batsman_id": "3873460",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "11",
              "batsman_name": "Raja Ahsan",
              "batsman_id": "4495642",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            }
          ],
          "fow": [
            {
              "runs": "129",
              "wickets": 1,
              "batsman_out_name": "Syed Kazmi",
              "batsman_out_id": "4999167",
              "batsman_in_name": "Yaser Ahmed",
              "batsman_in_id": "3786374",
              "batsman_in_runs": "65"
            }
          ],
          "bowl": [
            {
              "bowler_name": "Douglas Petrie",
              "bowler_id": "1917305",
              "overs": "4",
              "maidens": "0",
              "runs": "18",
              "wides": "0",
              "wickets": "0",
              "no_balls": "0"
            },
            {
              "bowler_name": "Scott Peterson",
              "bowler_id": "5483704",
              "overs": "6",
              "maidens": "0",
              "runs": "43",
              "wides": "2",
              "wickets": "0",
              "no_balls": "0"
            },
            {
              "bowler_name": "Raheel Khan",
              "bowler_id": "5402781",
              "overs": "8",
              "maidens": "2",
              "runs": "27",
              "wides": "1",
              "wickets": "1",
              "no_balls": "1"
            },
            {
              "bowler_name": "Joe Yerrell",
              "bowler_id": "6044911",
              "overs": "2",
              "maidens": "0",
              "runs": "20",
              "wides": "0",
              "wickets": "0",
              "no_balls": "1"
            },
            {
              "bowler_name": "Craig Peterson",
              "bowler_id": "3858366",
              "overs": "2",
              "maidens": "0",
              "runs": "24",
              "wides": "0",
              "wickets": "0",
              "no_balls": "0"
            },
            {
              "bowler_name": "Jamie Valentine",
              "bowler_id": "4524064",
              "overs": "1.1",
              "maidens": "0",
              "runs": "26",
              "wides": "0",
              "wickets": "0",
              "no_balls": "1"
            }
          ]
        }
      ]
    }
    ]}

lite_match_details = {"match_details": [{
          "id": 6244897,
          "status": "New",
          "published": "Yes",
          "last_updated": "21/04/2024",
          "league_id": "",
          "competition_name": "",
          "competition_id": "",
          "competition_type": "Friendly",
          "match_type": "Limited Overs",
          "game_type": "Standard",
          "countdown_cricket": "no",
          "match_id": "6538106",
          "match_date": "21/04/2024",
          "match_time": "13:30",
          "ground_name": "Ley_Hill_CC",
          "ground_id": "11691",
          "home_team_name": "Sunday 1st XI",
          "home_team_id": "216373",
          "home_club_name": "Ley_Hill_CC",
          "home_club_id": "3931",
          "away_team_name": "Friendly XI",
          "away_team_id": "207493",
          "away_club_name": "Soho Cricket Collective",
          "away_club_id": "12834",
          "umpire_1_name": "",
          "umpire_1_id": "",
          "umpire_2_name": "",
          "umpire_2_id": "",
          "umpire_3_name": "",
          "umpire_3_id": "",
          "referee_name": "",
          "referee_id": "",
          "scorer_1_name": "",
          "scorer_1_id": "",
          "scorer_2_name": "",
          "scorer_2_id": "",
          "toss_won_by_team_id": "216373",
          "toss": "Ley_Hill_CC - Sunday 1st XI won the toss and elected to field",
          "batted_first": "207493",
          "no_of_overs": "",
          "balls_per_innings": "",
          "no_of_innings": "1",
          "no_of_days": "1",
          "no_of_players": "",
          "no_of_reserves": "",
          "result": "W",
          "result_description": "Ley_Hill_CC - Sunday 1st XI - Won",
          "result_applied_to": "216373",
          "match_notes": "\u003Cb\u003ESoho Cricket Collective Friendly XI Innings\u003C/b\u003E\u003Cbr/\u003E\n12.1 Soho Cricket Collective Friendly XI: 50 runs in 12.1 overs, 44 minutes, 3 extras\u003Cbr/\u003E31.3 Soho Cricket Collective Friendly XI: 100 runs in 31.3 overs, 116 minutes, 13 extras\n\u003Cbr/\u003E\n\u003Cbr/\u003E\n\u003Cb\u003ELey Hill CC Sunday 1st XI Innings\u003C/b\u003E\u003Cbr/\u003E\n12.2 Ley_Hill_CC Sunday 1st XI: 50 runs in 12.1 overs, 43 minutes, 6 extras\u003Cbr/\u003E20.6 Ley_Hill_CC Sunday 1st XI: 100 runs in 21.0 overs, 80 minutes, 8 extras\n\u003Cbr/\u003E\n",
          "points": [],
          "match_result_types": [
              [
                  "Ley_Hill_CC - Sunday 1st XI - Won",
                  "1#216373"
              ],
              [
                  "Soho Cricket Collective - Friendly XI - Won",
                  "1#207493"
              ],
              [
                  "Drawn",
                  2],
              [
                  "Tied",
                  3],
              [
                  "Cancelled",
                  4],
              [
                  "Abandoned",
                  5],
              [
                  "Trophy Shared",
                  661119],
              [
                  "Match In Progress",
                  14]
          ],
          "players": [
              {
                  "home_team": [
                      {
                          "position": 1,
                          "player_name": "Ted Sussum",
                          "player_id": 4951412,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 2,
                          "player_name": "James Meek",
                          "player_id": 3480050,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 3,
                          "player_name": "Paul Green",
                          "player_id": 1101452,
                          "captain": "true",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 4,
                          "player_name": "Geoffrey Sussum",
                          "player_id": 4951380,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 5,
                          "player_name": "Joe Yerrell",
                          "player_id": 6044911,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 6,
                          "player_name": "Joe Foster",
                          "player_id": 6010486,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 7,
                          "player_name": "Alastair Rowe",
                          "player_id": 4952492,
                          "captain": "false",
                          "wicket_keeper": "true"
                      },
                      {
                          "position": 8,
                          "player_name": "Charlie Sussum",
                          "player_id": 6227859,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 9,
                          "player_name": "Ross Davies",
                          "player_id": 6439833,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 10,
                          "player_name": "Jon Lown",
                          "player_id": 5902299,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 11,
                          "player_name": "Dave Gwynn-Costello",
                          "player_id": 6227856,
                          "captain": "false",
                          "wicket_keeper": "false"
                      }
                  ]
              },
              {
                  "away_team": [
                      {
                          "position": 1,
                          "player_name": "Philip Richardson",
                          "player_id": 5340228,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 2,
                          "player_name": "Dan March",
                          "player_id": 4733831,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 3,
                          "player_name": "John Hirst",
                          "player_id": 5347249,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 4,
                          "player_name": "Kamran Hafeez",
                          "player_id": "null",
                          "captain": "false",
                          "wicket_keeper": "true"
                      },
                      {
                          "position": 5,
                          "player_name": "R Muller",
                          "player_id": 4406353,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 6,
                          "player_name": "Martin Collier",
                          "player_id": 5444636,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 7,
                          "player_name": "Daniel Woodhouse",
                          "player_id": 5341331,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 8,
                          "player_name": "David Hooper",
                          "player_id": 3987426,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 9,
                          "player_name": "Pete Brandon - Brandonovski",
                          "player_id": 3987428,
                          "captain": "false",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 10,
                          "player_name": "J Savitt",
                          "player_id": "null",
                          "captain": "true",
                          "wicket_keeper": "false"
                      },
                      {
                          "position": 11,
                          "player_name": "J Todd",
                          "player_id": "null",
                          "captain": "false",
                          "wicket_keeper": "false"
                      }
                  ]
              }
          ],
          "innings": [
              {
                  "team_batting_name": "Soho Cricket Collective - Friendly XI",
                  "team_batting_id": "207493",
                  "innings_number": 1,
                  "extra_byes": "1",
                  "extra_leg_byes": "1",
                  "extra_wides": "6",
                  "extra_no_balls": "5",
                  "extra_penalty_runs": "0",
                  "penalties_runs_awarded_in_other_innings": "0",
                  "total_extras": "13",
                  "runs": "106",
                  "wickets": "10",
                  "overs": "32",
                  "balls": "",
                  "declared": "false",
                  "forfeited_innings": "false",
                  "revised_target_runs": "",
                  "revised_target_overs": "",
                  "revised_target_balls": "",
                  "bat": [],
                  "fow": [],
                  "bowl": []
              },
              {
                  "team_batting_name": "Ley_Hill_CC - Sunday 1st XI",
                  "team_batting_id": "216373",
                  "innings_number": 1,
                  "extra_byes": "1",
                  "extra_leg_byes": "2",
                  "extra_wides": "3",
                  "extra_no_balls": "3",
                  "extra_penalty_runs": "0",
                  "penalties_runs_awarded_in_other_innings": "0",
                  "total_extras": "9",
                  "runs": "110",
                  "wickets": "3",
                  "overs": "23.5",
                  "balls": "",
                  "declared": "false",
                  "forfeited_innings": "false",
                  "revised_target_runs": "",
                  "revised_target_overs": "",
                  "revised_target_balls": "",
                  "bat": [],
                  "fow": [],
                  "bowl": []
              }
          ]
      }]}

problem_match_details = {
  "match_details": [
    {
      "id": 6230251,
      "status": "New",
      "published": "Yes",
      "last_updated": "17/05/2024",
      "league_name": "Hertfordshire Premier Cricket League",
      "league_id": "572",
      "competition_name": "Division 7 West",
      "competition_id": "116683",
      "competition_type": "League",
      "match_type": "Limited Overs",
      "game_type": "Standard",
      "countdown_cricket": "no",
      "match_id": "6230251",
      "match_date": "11/05/2024",
      "match_time": "13:00",
      "ground_name": "Ley Hill",
      "ground_id": "",
      "home_team_name": "1st XI",
      "home_team_id": "54824",
      "home_club_name": "Ley_Hill_CC",
      "home_club_id": "3931",
      "away_team_name": "2nd XI",
      "away_team_id": "119321",
      "away_club_name": "Kings Langley CC",
      "away_club_id": "3743",
      "umpire_1_name": "",
      "umpire_1_id": "",
      "umpire_2_name": "",
      "umpire_2_id": "",
      "umpire_3_name": "",
      "umpire_3_id": "",
      "referee_name": "",
      "referee_id": "",
      "scorer_1_name": "Nick Lee",
      "scorer_1_id": "4430142",
      "scorer_2_name": "",
      "scorer_2_id": "",
      "toss_won_by_team_id": "119321",
      "toss": "Kings Langley CC - 2nd XI won the toss and elected to bat",
      "batted_first": "119321",
      "no_of_overs": "40",
      "balls_per_innings": "",
      "no_of_innings": "1",
      "no_of_days": "1",
      "no_of_players": "11",
      "no_of_reserves": "1",
      "result": "W",
      "result_description": "Ley_Hill_CC - 1st XI - Won",
      "result_applied_to": "54824",
      "match_notes": "\u003Cb\u003EKings Langley CC 2nd XI Innings\u003C/b\u003E\u003Cbr/\u003E\n17.2 Kings Langley CC 2nd XI: 50 runs in 17.2 overs, 75 minutes, 6 extras\n\u003Cbr/\u003E\n\u003Cbr/\u003E\n\u003Cb\u003ELey Hill CC 1st XI Innings\u003C/b\u003E\u003Cbr/\u003E\n6.5 Ley_Hill_CC 1st XI: 50 runs in 6.5 overs, 24 minutes, 9 extras\n\u003Cbr/\u003E\n",
      "points": [
        {
          "team_id": 54824,
          "game_points": "30",
          "penalty_points": "0.0",
          "bonus_points_together": "0.0",
          "bonus_points_batting": "0.0",
          "bonus_points_bowling": "0.0",
          "bonus_points_2nd_innings_together": ""
        },
        {
          "team_id": 119321,
          "game_points": "0",
          "penalty_points": "0.0",
          "bonus_points_together": "1.0",
          "bonus_points_batting": "0.0",
          "bonus_points_bowling": "1.0",
          "bonus_points_2nd_innings_together": ""
        }
      ],
      "match_result_types": [
        [
          "Ley_Hill_CC - 1st XI - Won",
          "930428#54824"
        ],
        [
          "Kings Langley CC - 2nd XI - Won",
          "930428#119321"
        ],
        [
          "Tied",
          930435],
        [
          "Cancelled",
          930431],
        [
          "Abandoned",
          930432],
        [
          "Ley_Hill_CC - 1st XI - Conceded",
          "930433#119321"
        ],
        [
          "Kings Langley CC - 2nd XI - Conceded",
          "930434#54824"
        ],
        [
          "Match In Progress",
          14]
      ],
      "players": [
        {
          "home_team": [
            {
              "position": 1,
              "player_name": "Craig Peterson",
              "player_id": 3858366,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 2,
              "player_name": "Raheel Khan",
              "player_id": 5402781,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 3,
              "player_name": "Lewis Thompson",
              "player_id": 1000955,
              "captain": "true",
              "wicket_keeper": "false"
            },
            {
              "position": 4,
              "player_name": "Max Lee",
              "player_id": 1809919,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 5,
              "player_name": "Rob Leybourne",
              "player_id": 5363547,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 6,
              "player_name": "Callum Wilson",
              "player_id": 5497375,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 7,
              "player_name": "Yusuf Khan",
              "player_id": 4940735,
              "captain": "false",
              "wicket_keeper": "true"
            },
            {
              "position": 8,
              "player_name": "Chris Morris",
              "player_id": 3846114,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 9,
              "player_name": "Craig Ottaway",
              "player_id": 5499462,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 10,
              "player_name": "Scott Peterson",
              "player_id": 5483704,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 11,
              "player_name": "Joe Yerrell",
              "player_id": 6044911,
              "captain": "false",
              "wicket_keeper": "false"
            }
          ]
        },
        {
          "away_team": [
            {
              "position": 1,
              "player_name": "Paul Ashford",
              "player_id": 5899509,
              "captain": "true",
              "wicket_keeper": "false"
            },
            {
              "position": 2,
              "player_name": "John Battams",
              "player_id": 5628610,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 3,
              "player_name": "Andy Felton",
              "player_id": 6105592,
              "captain": "false",
              "wicket_keeper": "true"
            },
            {
              "position": 4,
              "player_name": "Martin Henderson",
              "player_id": 3599301,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 5,
              "player_name": "Kalpa Mendis",
              "player_id": 5331744,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 6,
              "player_name": "Iain Milton",
              "player_id": 5327411,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 7,
              "player_name": "Sifan Naeem",
              "player_id": 5327785,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 8,
              "player_name": "Spencer Snowball",
              "player_id": 6242598,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 9,
              "player_name": "Matthew Owens",
              "player_id": 5367426,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 10,
              "player_name": "Sam Siraj",
              "player_id": 5867559,
              "captain": "false",
              "wicket_keeper": "false"
            },
            {
              "position": 11,
              "player_name": "Amila Sethuge",
              "player_id": 6271959,
              "captain": "false",
              "wicket_keeper": "false"
            }
          ]
        }
      ],
      "innings": [
        {
          "team_batting_name": "Kings Langley CC - 2nd XI",
          "team_batting_id": "119321",
          "innings_number": 1,
          "extra_byes": "5",
          "extra_leg_byes": "0",
          "extra_wides": "1",
          "extra_no_balls": "0",
          "extra_penalty_runs": "0",
          "penalties_runs_awarded_in_other_innings": "0",
          "total_extras": "6",
          "runs": "61",
          "wickets": "10",
          "overs": "19.4",
          "balls": "",
          "declared": "false",
          "forfeited_innings": "false",
          "revised_target_runs": "",
          "revised_target_overs": "40.0",
          "revised_target_balls": "",
          "bat": [
            {
              "position": "1",
              "batsman_name": "Paul Ashford",
              "batsman_id": "5899509",
              "how_out": "ct",
              "fielder_name": "Rob Leybourne",
              "fielder_id": "5363547",
              "bowler_name": "Craig Ottaway",
              "bowler_id": "5499462",
              "runs": "0",
              "fours": "0",
              "sixes": "0",
              "balls": "2"
            },
            {
              "position": "2",
              "batsman_name": "Spencer Snowball",
              "batsman_id": "6242598",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Chris Morris",
              "bowler_id": "3846114",
              "runs": "0",
              "fours": "0",
              "sixes": "0",
              "balls": "2"
            },
            {
              "position": "3",
              "batsman_name": "Sifan Naeem",
              "batsman_id": "5327785",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Craig Ottaway",
              "bowler_id": "5499462",
              "runs": "4",
              "fours": "1",
              "sixes": "0",
              "balls": "4"
            },
            {
              "position": "4",
              "batsman_name": "Andy Felton",
              "batsman_id": "6105592",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Chris Morris",
              "bowler_id": "3846114",
              "runs": "11",
              "fours": "1",
              "sixes": "0",
              "balls": "30"
            },
            {
              "position": "5",
              "batsman_name": "Kalpa Mendis",
              "batsman_id": "5331744",
              "how_out": "ct",
              "fielder_name": "Callum Wilson",
              "fielder_id": "5497375",
              "bowler_name": "Chris Morris",
              "bowler_id": "3846114",
              "runs": "5",
              "fours": "1",
              "sixes": "0",
              "balls": "19"
            },
            {
              "position": "6",
              "batsman_name": "Amila Sethuge",
              "batsman_id": "6271959",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Joe Yerrell",
              "bowler_id": "6044911",
              "runs": "4",
              "fours": "1",
              "sixes": "0",
              "balls": "15"
            },
            {
              "position": "7",
              "batsman_name": "Sam Siraj",
              "batsman_id": "5867559",
              "how_out": "not out",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "16",
              "fours": "3",
              "sixes": "0",
              "balls": "21"
            },
            {
              "position": "8",
              "batsman_name": "John Battams",
              "batsman_id": "5628610",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Joe Yerrell",
              "bowler_id": "6044911",
              "runs": "0",
              "fours": "0",
              "sixes": "0",
              "balls": "1"
            },
            {
              "position": "9",
              "batsman_name": "Martin Henderson",
              "batsman_id": "3599301",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Joe Yerrell",
              "bowler_id": "6044911",
              "runs": "0",
              "fours": "0",
              "sixes": "0",
              "balls": "2"
            },
            {
              "position": "10",
              "batsman_name": "Iain Milton",
              "batsman_id": "5327411",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Scott Peterson",
              "bowler_id": "5483704",
              "runs": "11",
              "fours": "1",
              "sixes": "0",
              "balls": "16"
            },
            {
              "position": "11",
              "batsman_name": "Matthew Owens",
              "batsman_id": "5367426",
              "how_out": "b",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "Scott Peterson",
              "bowler_id": "5483704",
              "runs": "4",
              "fours": "1",
              "sixes": "0",
              "balls": "6"
            }
          ],
          "fow": [
            {
              "runs": "0",
              "wickets": 1,
              "batsman_out_name": "Paul Ashford",
              "batsman_out_id": "5899509",
              "batsman_in_name": "Spencer Snowball",
              "batsman_in_id": "6242598",
              "batsman_in_runs": "0"
            },
            {
              "runs": "4",
              "wickets": 2,
              "batsman_out_name": "Sifan Naeem",
              "batsman_out_id": "5327785",
              "batsman_in_name": "Spencer Snowball",
              "batsman_in_id": "6242598",
              "batsman_in_runs": "0"
            },
            {
              "runs": "4",
              "wickets": 3,
              "batsman_out_name": "Spencer Snowball",
              "batsman_out_id": "6242598",
              "batsman_in_name": "Andy Felton",
              "batsman_in_id": "6105592",
              "batsman_in_runs": "0"
            },
            {
              "runs": "16",
              "wickets": 4,
              "batsman_out_name": "Kalpa Mendis",
              "batsman_out_id": "5331744",
              "batsman_in_name": "Andy Felton",
              "batsman_in_id": "6105592",
              "batsman_in_runs": "7"
            },
            {
              "runs": "25",
              "wickets": 5,
              "batsman_out_name": "Andy Felton",
              "batsman_out_id": "6105592",
              "batsman_in_name": "Amila Sethuge",
              "batsman_in_id": "6271959",
              "batsman_in_runs": "4"
            },
            {
              "runs": "25",
              "wickets": 6,
              "batsman_out_name": "Amila Sethuge",
              "batsman_out_id": "6271959",
              "batsman_in_name": "Sam Siraj",
              "batsman_in_id": "5867559",
              "batsman_in_runs": "0"
            },
            {
              "runs": "25",
              "wickets": 7,
              "batsman_out_name": "John Battams",
              "batsman_out_id": "5628610",
              "batsman_in_name": "Sam Siraj",
              "batsman_in_id": "5867559",
              "batsman_in_runs": "0"
            },
            {
              "runs": "26",
              "wickets": 8,
              "batsman_out_name": "Martin Henderson",
              "batsman_out_id": "3599301",
              "batsman_in_name": "Sam Siraj",
              "batsman_in_id": "5867559",
              "batsman_in_runs": "0"
            },
            {
              "runs": "53",
              "wickets": 9,
              "batsman_out_name": "Iain Milton",
              "batsman_out_id": "5327411",
              "batsman_in_name": "Sam Siraj",
              "batsman_in_id": "5867559",
              "batsman_in_runs": "12"
            },
            {
              "runs": "61",
              "wickets": 10,
              "batsman_out_name": "Matthew Owens",
              "batsman_out_id": "5367426",
              "batsman_in_name": "Sam Siraj",
              "batsman_in_id": "5867559",
              "batsman_in_runs": "16"
            }
          ],
          "bowl": [
            {
              "bowler_name": "Craig Ottaway",
              "bowler_id": "5499462",
              "overs": "6",
              "maidens": "2",
              "runs": "15",
              "wides": "0",
              "wickets": "2",
              "no_balls": "0"
            },
            {
              "bowler_name": "Chris Morris",
              "bowler_id": "3846114",
              "overs": "6",
              "maidens": "3",
              "runs": "9",
              "wides": "0",
              "wickets": "3",
              "no_balls": "0"
            },
            {
              "bowler_name": "Joe Yerrell",
              "bowler_id": "6044911",
              "overs": "4",
              "maidens": "0",
              "runs": "12",
              "wides": "1",
              "wickets": "3",
              "no_balls": "0"
            },
            {
              "bowler_name": "Scott Peterson",
              "bowler_id": "5483704",
              "overs": "3.4",
              "maidens": "0",
              "runs": "20",
              "wides": "0",
              "wickets": "2",
              "no_balls": "0"
            }
          ]
        },
        {
          "team_batting_name": "Ley_Hill_CC - 1st XI",
          "team_batting_id": "54824",
          "innings_number": 1,
          "extra_byes": "8",
          "extra_leg_byes": "2",
          "extra_wides": "2",
          "extra_no_balls": "1",
          "extra_penalty_runs": "0",
          "penalties_runs_awarded_in_other_innings": "0",
          "total_extras": "13",
          "runs": "64",
          "wickets": "1",
          "overs": "8.4",
          "balls": "",
          "declared": "false",
          "forfeited_innings": "false",
          "revised_target_runs": "",
          "revised_target_overs": "40.0",
          "revised_target_balls": "",
          "bat": [
            {
              "position": "1",
              "batsman_name": "Craig Peterson",
              "batsman_id": "3858366",
              "how_out": "ct",
              "fielder_name": "Matthew Owens",
              "fielder_id": "5367426",
              "bowler_name": "Matthew Owens",
              "bowler_id": "5367426",
              "runs": "14",
              "fours": "3",
              "sixes": "0",
              "balls": "19"
            },
            {
              "position": "2",
              "batsman_name": "Raheel Khan",
              "batsman_id": "5402781",
              "how_out": "not out",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "26",
              "fours": "5",
              "sixes": "0",
              "balls": "25"
            },
            {
              "position": "3",
              "batsman_name": "Lewis Thompson",
              "batsman_id": "1000955",
              "how_out": "not out",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "11",
              "fours": "1",
              "sixes": "1",
              "balls": "9"
            },
            {
              "position": "4",
              "batsman_name": "Max Lee",
              "batsman_id": "1809919",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "5",
              "batsman_name": "Rob Leybourne",
              "batsman_id": "5363547",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "6",
              "batsman_name": "Callum Wilson",
              "batsman_id": "5497375",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "7",
              "batsman_name": "Yusuf Khan",
              "batsman_id": "4940735",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "8",
              "batsman_name": "Chris Morris",
              "batsman_id": "3846114",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "9",
              "batsman_name": "Craig Ottaway",
              "batsman_id": "5499462",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "10",
              "batsman_name": "Scott Peterson",
              "batsman_id": "5483704",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            },
            {
              "position": "11",
              "batsman_name": "Joe Yerrell",
              "batsman_id": "6044911",
              "how_out": "did not bat",
              "fielder_name": "",
              "fielder_id": "",
              "bowler_name": "",
              "bowler_id": "",
              "runs": "",
              "fours": "",
              "sixes": "",
              "balls": ""
            }
          ],
          "fow": [
            {
              "runs": "38",
              "wickets": 1,
              "batsman_out_name": "Craig Peterson",
              "batsman_out_id": "3858366",
              "batsman_in_name": "Raheel Khan",
              "batsman_in_id": "5402781",
              "batsman_in_runs": "19"
            }
          ],
          "bowl": [
            {
              "bowler_name": "Iain Milton",
              "bowler_id": "5327411",
              "overs": "3",
              "maidens": "0",
              "runs": "24",
              "wides": "2",
              "wickets": "0",
              "no_balls": "0"
            },
            {
              "bowler_name": "Matthew Owens",
              "bowler_id": "5367426",
              "overs": "3",
              "maidens": "0",
              "runs": "14",
              "wides": "0",
              "wickets": "1",
              "no_balls": "1"
            },
            {
              "bowler_name": "Amila Sethuge",
              "bowler_id": "6271959",
              "overs": "1.4",
              "maidens": "0",
              "runs": "6",
              "wides": "0",
              "wickets": "0",
              "no_balls": "0"
            },
            {
              "bowler_name": "Martin Henderson",
              "bowler_id": "3599301",
              "overs": "1",
              "maidens": "0",
              "runs": "10",
              "wides": "0",
              "wickets": "0",
              "no_balls": "0"
            }
          ]
        }
      ]
    }
  ]
}