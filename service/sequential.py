import threading
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


def fetch(url, result_dict, key):
    result_dict[key] = requests.get(url).json()


def run_threaded():
    start_time = time.time()
    _, start_memory = get_metrices()

    results = {}

    t1 = threading.Thread(target=fetch, args=(v1, results, "r1"))
    t2 = threading.Thread(target=fetch, args=(v2, results, "r2"))
    t3 = threading.Thread(target=fetch, args=(v3, results, "r3"))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    _, end_memory = get_metrices()
    end_time = time.time()

    return {
        "mode": "threaded",
        "time_taken_sec": round(end_time - start_time, 3),
        "memory_used_mb": round(end_memory - start_memory, 3),
        "result": {
            "products_count": len(results["r1"].get("products", [])),
            "github_public_repos": results["r2"].get("public_repos"),
            "posts_count": len(results["r3"])
        }
    }




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
            find_highest_rating = r1_dict[i]
        
    print(F"This is Highest rating { find_highest_rating}")
    
    processed_Data = {
        "status" : True,
        "highest_price" : max_price,
        "highest_rating" : find_highest_rating
    }

    return{

        "total_run_time" : round(total_run_time , 3),
        "memory_usage" : round(end_memory - get_usage , 3),
        "r1" : processed_Data,
        "r2" : r2,
        "r3" : r3
    }



def process_github(data: dict) -> dict:
    login_id = data["login"]
    uri = data["url"]
    name = data["name"]
    bio = data["bio"]
    pass



def do_the_data_analysis():
    pass