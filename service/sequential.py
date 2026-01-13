import requests
import time
import os
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

    # pass 1: extract
    for p in products:
        prices.append(p["price"])
        ratings.append(p["rating"])

    # pass 2: normalization + scoring
    max_price = max(prices)
    for i in range(len(prices)):
        normalized_price = prices[i] / max_price
        score += normalized_price * ratings[i]

    # pass 3: duplicate detection
    freq = {}
    for price in prices:
        freq[price] = freq.get(price, 0) + 1

    duplicate_prices = {k: v for k, v in freq.items() if v > 1}

    # pass 4: realistic CPU work (feature-style loop)
    for _ in range(500_000):
        score += 0.000001

    return {
        "max_price": max_price,
        "highest_rating": max(ratings),
        "score": round(score, 3),
        "duplicate_prices": duplicate_prices
    }


def run_sequential():
    start_time = time.time()
    start_metrics = UtilsMethod.get_metrices()

    # ---- Sequential API calls (blocking) ----
    products_resp = requests.get(E1).json()
    github_resp = requests.get(E2).json()
    posts_resp = requests.get(E3).json()

    # ---- Processing ----
    analysis = heavy_processing(products_resp["products"])

    end_metrics = UtilsMethod.get_metrices()
    end_time = time.time()

    return {
        "mode": "sequential",
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
            "github_public_repos": github_resp.get("public_repos"),
            "total_posts": len(posts_resp)
        }
    }
