# Python Threading vs Sequential

FastAPI • Threading • Streamlit • Matplotlib

This project is a hands-on comparison between **sequential execution** and **Python threading** using **real API calls** and **real processing**. No fake `sleep()` delays, no theory-only talk — just practical results.

The idea is simple: run the **same workload twice** and see what actually changes.

## What’s happening here

The backend is built with FastAPI and executes the same set of API calls in two ways:

- One version runs everything **sequentially**
- The other version uses Python’s `threading` module to **overlap I/O calls**

The logic, data, and workload stay exactly the same. The **only difference** is how the code is executed.

Since the work is **I/O-bound**, threading helps reduce total response time by overlapping network calls, while **CPU and memory usage remain mostly unchanged**. This is exactly how Python threading behaves in real-world systems.

## Dashboard

A small Streamlit dashboard is included to make things visual and easy to understand.

It shows:
- Total execution time
- Memory usage
- Thread behavior

All charts are rendered using Matplotlib so you can clearly see the difference between sequential and threaded runs.

## Tech used

- FastAPI  
- Python threading  
- Streamlit  
- Matplotlib  
- psutil  

## Note

This project focuses **only on I/O-bound workloads**.  
It does **not** attempt to speed up CPU-heavy tasks (threading won’t help there anyway).

More advanced threading patterns and experiments will be added next 🚀
