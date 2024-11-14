import yaml

def load_config():
    with open(r"E:\project-root\config\config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config