import requests
import time
import os
# import json
from dotenv import load_dotenv
from utils.metrice import get_metrices

load_dotenv()

v1 = os.getenv("E1")
v2 = os.getenv("E2")
v3 = os.getenv("E3")


def run_sequential():
    start_time = time.time()
    get_usage = get_metrices()
    r1 = requests.get(v1).json()
    r2 = requests.get(v2).json()
    r3 = requests.get(v3).json()

    end_memory = get_metrices()
    end_time = time.time()
    total_run_time = end_time - start_time 


    return{

        "total_run_time" : round(total_run_time , 3),
        "memory_usage" : round(end_memory - get_usage , 3),
        "r1" : r1,
        "r2" : r2,
        "r3" : r3
    }



def do_the_data_analysis():
    pass