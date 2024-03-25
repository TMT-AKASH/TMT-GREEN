import os, sys
os.system("git pull")
try:
    __import__("fox").approval()
except Exception as e:
    exit(str(e))
