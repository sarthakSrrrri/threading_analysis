import matplotlib.pyplot as plt

def plot_comparison(sequential, threaded):
    modes = ["Sequential", "Threaded"]

    time_values = [
        sequential["total_run_time"],
        threaded["total_run_time"]
    ]

    memory_values = [
        sequential["memory_usage"],
        threaded["memory_usage"]
    ]

    # Time comparison
    plt.figure()
    plt.bar(modes, time_values)
    plt.title("Execution Time Comparison")
    plt.ylabel("Time (seconds)")
    plt.show()

    # Memory comparison
    plt.figure()
    plt.bar(modes, memory_values)
    plt.title("Memory Usage Comparison")
    plt.ylabel("Memory (MB)")
    plt.show()
