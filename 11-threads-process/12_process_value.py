from multiprocessing import Process, Value


# This function is executed by every process.
def increment(counter):

    # Each process performs 100,000 increments.
    for _ in range(100000):

        # Acquire the lock before modifying shared data.
        # This ensures only ONE process modifies counter at a time.
        with counter.get_lock():

            # counter.value accesses the actual shared value.
            counter.value += 1


if __name__ == "__main__":

    # Create a shared integer in memory.
    #
    # 'i' → integer type
    # 0   → initial value
    #
    # Unlike a normal variable, this Value can be accessed
    # by multiple processes.
    counter = Value('i', 0)


    # Create 4 separate processes.
    # All 4 processes receive the SAME shared counter.
    processes = [
        Process(
            target=increment,
            args=(counter,)
        )
        for _ in range(4)
    ]


    # Start all 4 processes.
    [p.start() for p in processes]


    # Wait until all 4 processes finish.
    [p.join() for p in processes]


    # 4 processes × 100,000 increments
    # = 400,000 expected final value.
    print("Final counter value:", counter.value)