# ©<2021> - Wow Labz, Bangalore, India. All rights Reserved.
import os
import json
import logging
SECRET_KEY = os.urandom(32)

log = logging.getLogger("dao_log")

def get_config_value(param):
    log.debug("Entering get_config_value")
    current_path = os.path.dirname(__file__)
    config_file_path = os.path.join(current_path, 'project_config.json')

    with open(config_file_path) as f:
        config_data = json.load(f)
    log.debug("Exiting get_config_value")
    return config_data[param]