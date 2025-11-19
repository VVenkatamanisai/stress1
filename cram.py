import multiprocessing as mp
import threading
import time
import hashlib
import random

# -------- CONFIGURABLE SETTINGS -------- #
NUM_CPU_WORKERS = 4       # Increase for more CPU load
NUM_RAM_THREADS = 3       # Increase for more memory pressure
MEM_CHUNK_MB = 100        # RAM per thread (approx)
# --------------------------------------- #


def cpu_stress():
    """Burn CPU with endless matrix-like multiplications."""
    while True:
        x = [random.random() for _ in range(5000)]
        y = [random.random() for _ in range(5000)]
        _ = sum(a * b for a, b in zip(x, y))


def ram_stress():
    """Continuously allocate memory."""
    big_list = []
    chunk_size = MEM_CHUNK_MB * 1024 * 1024 // 8
    while True:
        block = [random.random() for _ in range(chunk_size)]
        big_list.append(block)
        time.sleep(0.5)


if __name__ == "__main__":
    print("Starting CPU + RAM stress...")

    # Start CPU-heavy processes
    for _ in range(NUM_CPU_WORKERS):
        p = mp.Process(target=cpu_stress)
        p.start()

    # Start memory-heavy threads
    for _ in range(NUM_RAM_THREADS):
        t = threading.Thread(target=ram_stress, daemon=True)
        t.start()

    # Keep main alive
    while True:
        time.sleep(1)
