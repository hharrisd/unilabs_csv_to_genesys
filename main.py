import logging.config

import yaml

with open("logging_config.yaml", "rb") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

if __name__ == '__main__':
    logger = logging.getLogger('development')


