import os, sys
os.system("git pull")
try:
    __import__("FOLX").approval()
except Exception as e:
    exit(str(e))
