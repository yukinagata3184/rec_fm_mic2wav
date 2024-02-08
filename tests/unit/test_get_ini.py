##
# @file test_get_ini.py
# @brief This file unit tests for get_ini.py.
# @author yukinagata3184

import pytest
from src import get_ini

def test_get_params_fm_ini_is_true():
    """! When expected param and got inifile param are assert , true is pass a test.
    """
    assert get_ini.get_params_fm_ini(inifile_path="./param.ini", section_name="DEFAULT") == \
           {"CHUNK": 1024, "CHANNELS": 1, "SAMP_RATE": 16000, "RECORD_SECONDS": 10}

def test_get_params_fm_ini_is_false():
    """! When unexpected param and got inifile param are assert , false is pass a test.
    """
    assert get_ini.get_params_fm_ini(inifile_path="./param.ini", section_name="DEFAULT") != \
           {"CHUNK": 1024, "CHANNELS": 1, "SAMP_RATE": 16000, "RECORD_SECONDS": 11}