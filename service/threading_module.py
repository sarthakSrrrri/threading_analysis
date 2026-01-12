import requests
import time
import os
import threading
from dotenv import load_dotenv
from utils.metrice import get_metrices

load_dotenv()

E1 = os.getenv("E1")
E2 = os.getenv("E2")
E3 = os.getenv("E3")


def fetch(url, result_dict, key):
    result_dict[key] = requests.get(url).json()


def run_threaded():
    start_time = time.time()
    _, start_memory = get_metrices()

    results = {}

    t1 = threading.Thread(target=fetch, args=(E1, results, "r1"))
    t2 = threading.Thread(target=fetch, args=(E2, results, "r2"))
    t3 = threading.Thread(target=fetch, args=(E3, results, "r3"))

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
