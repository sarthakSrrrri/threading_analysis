import requests
import time
import os
import threading
from dotenv import load_dotenv
from utils.metrice import UtilsMethod

load_dotenv()

E1 = os.getenv("E1")  # DummyJSON products
E2 = os.getenv("E2")  # GitHub user
E3 = os.getenv("E3")  # JSONPlaceholder posts


def heavy_processing(products):
    prices = []
    ratings = []
    score = 0.0

    for p in products:
        prices.append(p["price"])
        ratings.append(p["rating"])

    max_price = max(prices)
    for i in range(len(prices)):
        score += (prices[i] / max_price) * ratings[i]

    freq = {}
    for price in prices:
        freq[price] = freq.get(price, 0) + 1

    duplicate_prices = {k: v for k, v in freq.items() if v > 1}

    for _ in range(500_000):
        score += 0.000001

    return {
        "max_price": max_price,
        "highest_rating": max(ratings),
        "score": round(score, 3),
        "duplicate_prices": duplicate_prices
    }


def fetch(url, store, key):
    store[key] = requests.get(url).json()


def run_threaded():
    start_time = time.time()
    start_metrics = UtilsMethod.get_metrices()

    results = {}

    t1 = threading.Thread(target=fetch, args=(E1, results, "products"))
    t2 = threading.Thread(target=fetch, args=(E2, results, "github"))
    t3 = threading.Thread(target=fetch, args=(E3, results, "posts"))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    analysis = heavy_processing(results["products"]["products"])

    end_metrics = UtilsMethod.get_metrices()
    end_time = time.time()

    return {
        "mode": "threaded",
        "total_run_time": round(end_time - start_time, 3),

        "metrics_delta": {
            "memory_mb": round(
                end_metrics["memory_mb"] - start_metrics["memory_mb"], 3
            ),
            "threads": end_metrics["threads"],
            "cpu_user_time": round(
                end_metrics["cpu_user_time"] - start_metrics["cpu_user_time"], 3
            ),
            "cpu_system_time": round(
                end_metrics["cpu_system_time"] - start_metrics["cpu_system_time"], 3
            ),
            "net_recv_mb": round(
                end_metrics["net_recv_mb"] - start_metrics["net_recv_mb"], 3
            ),
        },

        "analysis": {
            **analysis,
            "github_public_repos": results["github"].get("public_repos"),
            "total_posts": len(results["posts"])
        }
    }
