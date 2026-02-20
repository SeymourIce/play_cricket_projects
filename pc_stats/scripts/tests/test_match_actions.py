import unittest
from unittest.mock import patch, Mock
from datetime import datetime

from pc_stats.scripts.tests.mock_test_data import *
from pc_stats.scripts.src.club_actions import *
from pc_stats.scripts.src.match_actions import *

# def test_import_new_matches():
#
#     import_new_matches()

def test_check_for_new_matches():
