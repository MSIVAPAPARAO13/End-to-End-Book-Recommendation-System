import yaml
import sys
import os
from books_recommender.exception.exception_handler import AppException
from books_recommender.logger.log import logger


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    :param file_path: Path to YAML file
    :return: dict
    """
    try:
        logger.info(f"Reading YAML file from: {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"YAML file not found at path: {file_path}")

        with open(file_path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)

            if content is None:
                raise ValueError("YAML file is empty")

        logger.info("YAML file loaded successfully")

        return content

    except Exception as e:
        logger.error("Error while reading YAML file")
        raise AppException(e, sys) from e