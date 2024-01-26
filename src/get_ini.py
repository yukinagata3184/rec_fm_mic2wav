##
# @file get_params_fm_ini.py
# @brief This file implements loading an inifile to manage configuration values.
# @author yukinagata3184

import configparser

def get_params_fm_ini(inifile_path, section_name="DEFAULT"):
    """! Get params(dict) from an inifile.
    @param inifile_path [str] The path to an inifile as a str.
    @param section_name [str] The name of an inifile section to get.
    @retval param_dict Parameters get from an inifile are stored in a dictionary.
    """
    key_list = []
    param_dict = {}

    inifile_object = configparser.ConfigParser()
    inifile_object.read(inifile_path, encoding="utf-8")
    for key in inifile_object[section_name]:
        key_list.append(key.upper())
    for key in key_list:
        param = inifile_object[section_name][key]
        if param.isdecimal():
            param_dict[key] = int(param)
        else:
            param_dict[key] = param
    return param_dict