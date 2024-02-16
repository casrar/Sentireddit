import json
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger(__name__)

def logger_config() -> None:
    try:
        config = pathlib.Path('config.json')
        with open(config) as f:
            config = json.load(f)
        logging.config.dictConfig(config=config)
    except FileNotFoundError:
        logger.critical('config.json not found')
    except json.JSONDecodeError:
        logger.critical('Error parsing config.json')
    except Exception as e:
        logger.critical(f'Error with logger configuration: {e}')


def get_logger() -> logging.Logger:
    try:
        logger_config()
        return logger
    except Exception as e:
        logger.critical(f'Error getting logger: {e}')


