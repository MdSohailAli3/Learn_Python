import threading


# Shared variable — both threads access and modify this
chai_stock = 0


def restock():

    global chai_stock

    # Each thread increments chai_stock 100,000 times
    for _ in range(100000):
        chai_stock += 1

        # ⚠️ Shared-state operation:
        # Multiple threads modifying the same variable can cause
        # a race condition because += involves multiple steps.


# Create 2 threads running the same function
threads = [threading.Thread(target=restock) for _ in range(2)]


# Start both threads
for t in threads:
    t.start()


# Wait for both threads to finish
# join() blocks the main thread until each thread completes
for t in threads:
    t.join()


# Expected: 200,000
# Without proper synchronization, shared-state updates can be unsafe.
print("Chai stock: ", chai_stock)