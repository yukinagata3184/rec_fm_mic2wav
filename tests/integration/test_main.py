##
# @file test_main.py
# @brief This file integration tests for main.py.
# @author yukinagata3184

import pytest
import os
from main import main

def test_main():
    """! Check whether the recorded wav file exists after executed main.py.
    """
    main()
    assert os.path.isfile("./record.wav") == True
    os.remove("./record.wav")
