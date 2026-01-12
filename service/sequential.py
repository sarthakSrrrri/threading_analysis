import requests
import time
import os
from dotenv import load_dotenv
from utils.metrice import get_metrices

load_dotenv()

v1 = os.getenv("E1")
v2 = os.getenv("E2")
v3 = os.getenv("E3")

price_list = []



def run_sequential():
    start_time = time.time()
    get_usage = get_metrices()
    r1 = requests.get(v1).json()
    r2 = requests.get(v2).json()
    r3 = requests.get(v3).json()


    for i in r1.get("products"):
        price_list.append(i["price"])
    
    max_price = price_list[0]

    for i in range(0, len(price_list)-1):    
        if max_price < price_list[i]:
            max_price = price_list[i]
    print(f"This is Max price :  {max_price}")

    end_memory = get_metrices()
    end_time = time.time()
    total_run_time = end_time - start_time 
    r1_dict = []
    for i in r1.get("products"):
        r1_dict.append(i["rating"])
    print(f"This is ratimg list :  {r1_dict}")

    find_highest_rating = r1_dict[0]
    for i in range(0,len(r1_dict)):
        if find_highest_rating < r1_dict[i]:
            find_highest_rating = r1_dict
        

    processed_Data = {
        "status" : True,
        "highest_price" : max_price,
        "highest_rating" : find_highest_rating
    }

    return{

        "total_run_time" : round(total_run_time , 3),
        "memory_usage" : round(end_memory - get_usage , 3),
        "r1" : r1,
        "r2" : r2,
        "r3" : r3
    }









def do_the_data_analysis():
    pass