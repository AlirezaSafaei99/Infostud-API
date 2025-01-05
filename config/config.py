# config.py
# This file provides configuration management for the application.
# It defines a function to load configuration settings (such as database connection details) from a YAML file.
# The configuration data is accessed and used throughout the application.

import yaml

def load_config():
    with open(r"E:\project-root\config\config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config