import threading
import time


# CPU-bound function:
# The CPU spends most of its time doing calculations.
def cpu_heavy():
    print("Crunching some numbers...")

    total = 0

    # Perform a large number of calculations.
    for i in range(10**7):
        total += i

    print("DONE ✅")


# Start measuring execution time.
start = time.time()


# Create 2 threads inside the SAME Python process.
# Threads share the process's memory.
threads = [
    threading.Thread(target=cpu_heavy)
    for _ in range(2)
]


# Start both threads.
# They can make concurrent progress, but in standard CPython
# the GIL prevents multiple threads from executing Python
# bytecode simultaneously.
[t.start() for t in threads]


# Wait for both threads to finish.
[t.join() for t in threads]


# Calculate total execution time.
print(f"Time taken: {time.time() - start:.2f} seconds")