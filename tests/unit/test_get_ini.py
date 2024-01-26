import pytest
from src import get_ini

def test_get_params_fm_ini_is_true():
    assert get_ini.get_params_fm_ini(inifile_path="./param.ini", section_name="DEFAULT") == \
           {"CHUNK": 1024, "CHANNELS": 1, "SAMP_RATE": 16000, "RECORD_SECONDS": 10}

def test_get_params_fm_ini_is_false():
    assert get_ini.get_params_fm_ini(inifile_path="./param.ini", section_name="DEFAULT") != \
           {"CHUNK": 1024, "CHANNELS": 1, "SAMP_RATE": 16000, "RECORD_SECONDS": 11}