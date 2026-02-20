import unittest
from unittest.mock import patch, Mock
from datetime import datetime
import os
from pc_stats.scripts.tests.mock_test_data import *
from pc_stats.scripts.src.club_actions import Club

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

lhcc = Club(site_id=3931, club_name='Ley Hill CC')
ley_hill_cc = Club(3931)
lhcc_1s = Club(site_id=3931, club_name='Ley Hill CC', selected_team_names = ['1st XI'])
lhcc_sat = Club(site_id=3931, club_name='Ley Hill CC', selected_team_names = ['1st XI', '2nd XI'])

class TestPlayCricketAPI(unittest.TestCase):

    # @patch('requests.get')
    # def test_fetch_data(self, mock_get):
    #
    #     mock_response = Mock()
    #
    #     mock_response.json.return_value = matches_summary
    #     mock_response.status_code = 200
    #
    #     mock_get.return_value = mock_response
    #
    #     results_2024 = api_test.fetch_data('matches', params={"site_id": '3931', "season": 2024})
    #
    #     mock_get.assert_called_with(
    #         "http://play-cricket.com/api/v2/matches",
    #         params={'site_id': '3931', 'season': 2024, 'api_token': '7068b85d44186c4d96eef29a6c3da106'}
    #     )
    #     self.assertEqual(results_2024, matches_summary)

    @patch('requests.get')
    def test_get_club_name(self, mock_get):

        mock_get.json.return_value = clubs_list
        mock_get.status_code = 200

        mock_get.return_value = mock_get

        lhcc_no_name = Club(3931)

        self.assertEqual('Ley Hill CC', lhcc_no_name.club_name)

        lhcc_club_name = Club(3931, club_name='LHCC')

        self.assertEqual('LHCC', lhcc_club_name.club_name)

    @patch('pandas.read_csv')
    def test_get_last_updated_date(self, mock_read_csv):

        self.assertIsNone(lhcc.last_updated_date)

        mock_read_csv.return_value = pd.DataFrame({'date': ['2025-02-01','2025-05-01']
                                                      ,'club': ['Ley Hill CC', 'Ley Hill CC']
                                                   })

        self.assertEqual(datetime(2025,5,1), lhcc.get_last_updated_date())

    @patch('requests.get')
    def test_get_team_ids(self, mock_get):

        mock_get.json.return_value = ley_hill_teams
        mock_get.status_code = 200

        mock_get.return_value = mock_get

        lhcc_expected_team_ids = [54824,119465,216373,232724]
        lhcc_all_teams = [54824,119465,216373,232724,119469,119470,327066,241663,119472,119473]

        self.assertEqual(lhcc_expected_team_ids, lhcc.get_team_ids())
        self.assertEqual(lhcc_all_teams, ley_hill_cc.get_team_ids())

    def test_get_new_matches(self):

        # mock_get.return_value.json.side_effect = [ley_hill_teams, lhcc_some_2025_matches]

        matches_df = lhcc_1s.get_new_matches()

        return matches_df

    def test_export_new_matches(self):

        lhcc_sat = Club(site_id=3931, club_name='Ley Hill CC', selected_team_names=['1st XI', '2nd XI'])

        lhcc_sat.root_folder = f"../../testing/club_directory/{lhcc_sat.club_name}/"
        lhcc_sat.matches_output_folder = f"../../testing/data/results/"

        activity_log_file = f'{lhcc_sat.root_folder}/activity_log.csv'

        if (os.path.exists(activity_log_file) and os.path.isfile(activity_log_file)):
            os.remove(activity_log_file)

        # Update 1st XI and 2nd XI matches
        lhcc_sat.update_new_matches()

        # Read the activity log
        df = pd.read_csv(activity_log_file, sep=',')

        only_1st_XI_activity_df = df[df['team_name'] == '1st XI']
        round_1_1st_XI_matches = only_1st_XI_activity_df['new_matches'].iloc[-1]

        only_2nd_XI_activity_df = df[df['team_name'] == '2nd XI']

        # Write filtered df back to file
        only_2nd_XI_activity_df.to_csv(activity_log_file, sep=',',index=False)

        # Run update again
        lhcc_sat.update_new_matches()

        # Update the activity log to remove activity for 1st XI
        df = pd.read_csv(activity_log_file, sep=',')

        only_1st_XI_activity_df = df[df['team_name'] == '1st XI']
        round_2_1st_XI_matches = only_1st_XI_activity_df['new_matches'].iloc[-1]
        only_2nd_XI_activity_df = df[df['team_name'] == '2nd XI']
        round_2_2nd_XI_matches = only_2nd_XI_activity_df['new_matches'].iloc[-1]

        # All matches should have been pulled again for the 1st XI
        self.assertEqual(round_1_1st_XI_matches,round_2_1st_XI_matches)
        self.assertEqual(0,round_2_2nd_XI_matches)


    # def test_create_and_update_club(self):




    # @patch('requests.get')
    # def test_get_results_summary(self, mock_get):
    #
    #     mock_response = Mock()
    #     mock_response.json.return_value = matches_summary
    #     mock_response.status_code = 200
    #
    #     mock_get.return_value = mock_response
    #
    #     results_list = api_test.get_match_ids(lhcc.site_id, season='2024')
    #
    #     equal_check = (match_id_list == results_list)
    #
    #     self.assertTrue(equal_check)
    #
    #     mock_response.status_code = 100
    #     mock_response.json.return_value = empty_matches_summary
    #
    #     mock_get.return_value = mock_response
    #
    #     empty_results_list, grounds_list = api_test.get_match_ids(lhcc.site_id, season=1991)
    #
    #     self.assertEqual(empty_results_list,[])
    #
    # @patch('requests.get')
    # def test_process_match_details(self, mock_get):
    #     mock_response = Mock()
    #
    #     mock_response.status_code = 200
    #     mock_response.json.return_value = problem_match_details
    #     mock_get.return_value = mock_response
    #
    #     match_info, player_info_df = lhcc.process_match_details('5544903')
    #
    #     print(match_info)
    #     print(player_info_df)
    #
    # def test_extract_match_info(self):
    #
    #     match_info = lhcc.extract_match_info(problem_match_details)
    #
    #     self.assertEqual(match_info.loc[0, 'season'], '2024')
    #     self.assertEqual(match_info.loc[0, 'location'], 'Home')
    #     self.assertEqual(match_info.loc[0, 'won_toss'], 0)
    #     self.assertEqual(match_info.loc[0, 'batted_first'], 0)
    #
if __name__ == '__main__':
    unittest.main()