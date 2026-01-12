import psutil
import os


class UtilsMethod:

    def __init__(self):
        pass

    def get_metrices():

        process = psutil.Process(os.getpid())
        memory_info = process.memory_full_info().rss / (1024 * 1024)
        return memory_info
    

    def get_max(data: list) ->  int:
        count = 0

        pass

