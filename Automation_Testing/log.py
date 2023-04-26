import logging
import os
import sys
from pathlib import Path

sys.path.append(os.path.join(str(Path(os.getcwd()).parent.parent)))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))


def find_directory():
    directory = str(Path(os.getcwd()).parent)+"\\Logs"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def log_files(name):
    directory = find_directory()
    logging.basicConfig(filename=f'{directory}\\{name}.log',
                            filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%H:%M:%S',level=logging.DEBUG)
    logging.info(directory)
    result_logger = logging.getLogger(name)
    return result_logger


#print(okok())
#print(log_files("vinayy")
#system()


