import yaml

def load_config():
    with open(r"C:\Projects\Alireza\Infostud-API\config\config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config