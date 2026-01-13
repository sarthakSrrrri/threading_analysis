import requests
import time
import os
from dotenv import load_dotenv
from utils.metrice import UtilsMethod

load_dotenv()

E1 = os.getenv("E1")
E2 = os.getenv("E2")
E3 = os.getenv("E3")


def run_sequential():
    start_time = time.time()
    _, start_memory = UtilsMethod.get_metrices()

    # Sequential API calls (blocking)
    products_resp = requests.get(E1).json()
    github_resp = requests.get(E2).json()
    posts_resp = requests.get(E3).json()

    products = products_resp["products"]

    prices = [p["price"] for p in products]
    ratings = [p["rating"] for p in products]

    max_price = max(prices)
    highest_rating = max(ratings)

    price_frequency = {}
    for price in prices:
        price_frequency[price] = price_frequency.get(price, 0) + 1

    duplicate_prices = {k: v for k, v in price_frequency.items() if v > 1}

    _, end_memory = UtilsMethod.get_metrices()
    end_time = time.time()

    return {
        "mode": "sequential",
        "total_run_time": round(end_time - start_time, 3),
        "memory_usage": round(end_memory - start_memory, 3),
        "analysis": {
            "max_price": max_price,
            "highest_rating": highest_rating,
            "duplicate_price_count": duplicate_prices,
            "github_public_repos": github_resp.get("public_repos"),
            "total_posts": len(posts_resp)
        }
    }
