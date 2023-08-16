"""Project wide path settings to be used by other modules while operating with files."""


# External Imports
from os.path import dirname, abspath, join


# Top level folders
ROOT_FOLDER = dirname(dirname(dirname(abspath(__file__))))
LOGS_FOLDER = join(ROOT_FOLDER, "logs")
