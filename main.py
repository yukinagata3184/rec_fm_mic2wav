##
# @file main.py
# @brief Record from a mic and save to a WAV file. Using param by a param.ini.
# @author yukinagata3184
from src import get_ini
from src import rec_fm_mic2wav

def main():
    """! Record from a mic and save to a WAV file. Using param by a param.ini.
    """
    param_dict = get_ini.get_params_fm_ini(inifile_path="param.ini", section_name="OVERWRITE")
    rec_fm_mic2wav.rec_fm_mic2wav(param_dict=param_dict)

if __name__ == "__main__":
    main()