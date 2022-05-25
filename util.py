import time
import os


def clear(secs=0):
    time.sleep(secs)
    os.system('cls' if os.name == 'nt' else 'clear')
