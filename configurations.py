
import json
import os
from typing import TypedDict


class Config(TypedDict):
    # Path to directory containing emoji files.
    emojis_dir: str


DEFAULT_CONFIG: Config = {
    'emojis_dir': ''
}


def load_config(config_path: str) -> Config:
    """Load config file or create a new one if it doesn't
    exists.

    Args:
        config_path (str): Path to config file

    Returns:
        Config: Config object
    """
    if not os.path.isfile(config_path):
        with open(config_path, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)

    config: Config = {}
    with open(config_path, 'r') as f:
        config = json.load(f)

    return config
