"""Module with a functions for working with a local storage"""
import json
from base_logger import logger


def read_storage(file_name: str):
    """
    Read all information from local storage (file with name = file_name)
    Args:
     file_name (string): file name for local storage
    Returns:
      news_all (dictionary): dictionary with all news, loaded from file or empty dictionary
    """
    logger.info('read_storage start') #Logs a message
    news_all = {}
    try:
        with open(file_name) as f:
            news_all = json.load(f)
    except:
        news_all = {}
    return news_all


def write_storage(file_name: str, news_all: dict):
    """
     Write all information from news_all to local storage (file with name = file_name)
     Args:
       file_name (string): file name for local storage
       news_all (dictionary): dictionary with all news
     Returns:
       False if error write to file or True if write ok
    """
    logger.info('read_storage start') #Logs a message
    try:
        with open(file_name, 'w') as f:
            json.dump(news_all, f, indent=4)
    except:
        return False
    return True
