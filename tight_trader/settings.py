import pathlib
import yaml


BASE_DIR = pathlib.Path(__file__).parent.parent  # get project base dir
config_path = BASE_DIR / 'config' / 'bot.yaml'  # git config file dir


def get_config(path):
    with open(path) as file:
        config = yaml.safe_load(file)
    return config


config = get_config(config_path)
