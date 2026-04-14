import os

# Get root directory of project
ROOT_DIR = os.getcwd()

# Config folder and file name
CONFIG_FOLDER_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"

# Full path to config file
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_FOLDER_NAME, CONFIG_FILE_NAME)

# Print for verification
print("Root Directory:", ROOT_DIR)
print("Config File Path:", CONFIG_FILE_PATH)