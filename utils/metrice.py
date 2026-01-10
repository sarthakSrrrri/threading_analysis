import psutil
import os

def get_metrices():

    process = psutil.Process(os.getpid())
    memory_info = process.memory_full_info().rss / (1024 * 1024)
    return memory_info
   

