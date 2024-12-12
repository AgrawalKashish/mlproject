import logging #logger is a module in the standard library that is used to track events that happen when some software runs
import os #os is a module in the standard library that provides a way of using operating system dependent functionality
from datetime import datetime #datetime is a module in the standard library that provides classes for manipulating dates and times

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE) #os.getcwd() returns the current working directory of a process
os.makedirs(logs_path, exist_ok=True) #os.makedirs() method in Python is used to create a directory recursively. The method os.makedirs() internally calls the mkdir() method multiple times to create a directory structure.

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logger is working fine")