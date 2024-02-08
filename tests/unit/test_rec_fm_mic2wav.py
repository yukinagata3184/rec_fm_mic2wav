##
# @file test_rec_fm_mic2wav.py
# @brief This file unit tests for rec_fm_mic2wav.py.
# @author yukinagata3184

import pytest
import os
import time
from src import rec_fm_mic2wav

def test_rec_fm_mic2wav():
    """! Check whether the recorded wav file exists and the wav file exceeds the 
         RECORD_SECONDS time.
    """
    input_dict = {"CHUNK": 1024, "CHANNELS": 1, "SAMP_RATE": 16000, "RECORD_SECONDS": 3}
    start = time.time()
    rec_fm_mic2wav.rec_fm_mic2wav(param_dict=input_dict)
    end = time.time()
    assert (end - start) > input_dict["RECORD_SECONDS"]
    assert os.path.isfile("./record.wav") == True
    os.remove("./record.wav")