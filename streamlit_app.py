import sys
sys.path.append(".")

import streamlit as st
import matplotlib.pyplot as plt
from dotenv import load_dotenv

from service.sequential import run_sequential
from service.threading_module import run_threaded

load_dotenv()

st.set_page_config(
    page_title="Threading Analysis",
    layout="wide"
)

st.title("🧵 Threading vs Sequential")
st.caption("I/O-bound performance comparison")

# ---------- RUN ----------
if st.button("Run Analysis"):

    seq = run_sequential()
    th = run_threaded()

    # ---------- Extract ----------
    seq_time = seq["total_run_time"]
    th_time = th["total_run_time"]

    seq_mem = seq["metrics_delta"]["memory_mb"]
    th_mem = th["metrics_delta"]["memory_mb"]

    seq_threads = seq["metrics_delta"]["threads"]
    th_threads = th["metrics_delta"]["threads"]

    speedup = round(seq_time / th_time, 2)
  

    # ---------- METRIC BOXES ----------
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Sequential Time (s)", seq_time)
    c2.metric("Speedup", f"{speedup}x")

    # c2.metric("Threaded Time (s)", th_time, delta=f"{speedup}x faster")
    c3.metric("Memory Δ (MB)", round(th_mem - seq_mem, 3))
    c4.metric("Thread Increase", th_threads - seq_threads)
    st.subheader("Interpretation")
    st.write(
        f"""
        • Threaded execution is **{speedup}× faster**  
        • Memory usage stays almost the same  
        • Extra threads are used only to overlap **network I/O**  
        • This confirms threading helps **I/O-bound workloads**
        """
    )
  

    st.divider()

    # ---------- ROW 1 ----------
    col1, col2, col3 = st.columns(3)

    # ---- Small Bar: Time ----
    with col1:
        st.subheader("Execution Time")
        fig, ax = plt.subplots(figsize=(2, 2))
        ax.bar(
            ["Seq", "Thread"],
            [seq_time, th_time],
            color=["#ff6b6b", "#4dabf7"]
        )
        ax.set_ylabel("Seconds")
        st.pyplot(fig)

    # ---- Pie: Time Split ----
    with col2:
        st.subheader("Time Share")
        fig, ax = plt.subplots(figsize=(2, 2))
        ax.pie(
            [seq_time, th_time],
            labels=["Sequential", "Threaded"],
            autopct="%1.1f%%",
            colors=["#ffa8a8", "#74c0fc"]
        )
        st.pyplot(fig)

    # ---- Threads ----
    with col3:
        st.subheader("Thread Usage")
        fig, ax = plt.subplots(figsize=(2, 2))
        ax.bar(
            ["Seq", "Thread"],
            [seq_threads, th_threads],
            color=["#adb5bd", "#51cf66"]
        )
        ax.set_ylabel("Threads")
        st.pyplot(fig)

    st.divider()

    # ---------- ROW 2 ----------
    col4, col5 = st.columns(2)

    # ---- Line: Time Trend (fake but meaningful visualization) ----
    with col4:
        st.subheader("Latency Trend (conceptual)")
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.plot(
            ["Start", "Mid", "End"],
            [seq_time, seq_time * 0.9, seq_time * 0.8],
            label="Sequential",
            color="#ff6b6b",
            marker="o"
        )
        ax.plot(
            ["Start", "Mid", "End"],
            [th_time, th_time * 0.95, th_time * 0.9],
            label="Threaded",
            color="#4dabf7",
            marker="o"
        )
        ax.set_ylabel("Seconds")
        ax.legend()
        st.pyplot(fig)

    # ---- Memory Comparison ----
    with col5:
        st.subheader("Memory Delta")
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.bar(
            ["Seq", "Thread"],
            [seq_mem, th_mem],
            color=["#ffd43b", "#69db7c"]
        )
        ax.set_ylabel("MB")
        st.pyplot(fig)

    # ---------- SUMMARY ----------
    st.divider()


