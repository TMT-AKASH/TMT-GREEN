import os, sys
os.system("git pull")
try:
    __import__("foxs").approval()
except Exception as e:
    exit(str(e))
