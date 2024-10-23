import json
import os


def load_config(config_path='config.json'):
    """
    Load configuration from a JSON file.
    :param config_path: Path to the configuration file
    :return: Dictionary containing the configuration
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件 '{config_path}' 不存在")

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    return config


def get_db_config():
    """
    Get database configuration from the loaded config.
    :return: Dictionary containing database configuration
    """
    config = load_config()
    return config.get('database', {})
