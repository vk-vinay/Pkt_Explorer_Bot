import sys
from os import environ as env
from dotenv import load_dotenv

load_dotenv()


def get_env(key: str):
    """getting environment variables  from environment file"""
    try:
        return env[key]
    except KeyError as e:
        print(f'[error]: `{e}` environment variable required')
        sys.exit(1)
