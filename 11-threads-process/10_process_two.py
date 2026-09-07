from multiprocessing import Process
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


# Required for multiprocessing to safely create child processes.
if __name__ == "__main__":

    # Start measuring execution time.
    start = time.time()

    # Create 2 SEPARATE processes.
    # Each process gets its own Python interpreter and memory space.
    processes = [
        Process(target=cpu_heavy)
        for _ in range(2)
    ]

    # Start both processes.
    # CPU-bound tasks can execute in parallel on multiple CPU cores.
    [p.start() for p in processes]

    # Wait for both processes to finish.
    [p.join() for p in processes]

    # Calculate total execution time.
    print(f"Time taken: {time.time() - start:.2f} seconds")


# IMPORTANT:
# Processes do NOT normally share memory directly.
# Each process has its own 'total' variable.
#
# Multiprocessing is useful for CPU-bound tasks because
# separate processes are not limited by the same GIL.