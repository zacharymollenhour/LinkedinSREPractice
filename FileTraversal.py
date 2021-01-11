#Directory Traversal Practice

#Used for walking through files on the computer
import os

#if directory exists, read in the file
if os.path.exists("./test"):
    with open("./test_log.log",'r') as file:
        for line in file:
            print(line)

#If directory does not exist create it
if not os.path.exists('./test'):
    os.makedirs('./test')
