#Python Log File Parsing
import re

#Start by opening the log file
log_file_path = r"./test_log.log"

#Regex to match for css files
regex = re.compile(r'.*path="/.......css')

#Open Log file and search for above regex
with open(log_file_path,"r") as file:
    for line in file:
        if (regex.search(line)):
            print(line)
            
        