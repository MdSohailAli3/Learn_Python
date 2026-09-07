import threading

# Shared variable: all threads access the same counter
counter = 0

# Lock is used to protect the critical section
# Only one thread can hold this lock at a time
lock = threading.Lock()


def increament():
    # Tell Python that we want to modify the global counter
    global counter

    # Each thread performs 100,000 increments
    for _ in range(100000):

        # Acquire the lock before modifying shared data
        # Only ONE thread can execute this block at a time
        with lock:
            counter += 1

        # Lock is automatically released after the 'with' block


# Create 10 threads.
# All threads execute the same function and share the global counter.
threads = [
    threading.Thread(target=increament)
    for _ in range(10)
]


# Start all 10 threads
[t.start() for t in threads]


# Wait for all threads to finish
[t.join() for t in threads]


# Expected result:
# 10 threads × 100,000 increments = 1,000,000
print(f"Final counter: {counter}")

# Without the lock, multiple threads can modify 
# the same counter at the same time, which can cause a race condition and lost updates.