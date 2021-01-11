#Python Log File Parsing
import re

#Start by opening the log file
log_file_path = r"./test_log.log"
with open(log_file_path) as file:
    for line in file:
        print(line)