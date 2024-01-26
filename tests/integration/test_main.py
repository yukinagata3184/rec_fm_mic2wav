import pytest
import os
from main import main

def test_main():
    main()
    assert os.path.isfile("./record.wav") == True
    os.remove("./record.wav")
