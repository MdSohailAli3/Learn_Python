import threading


# Two separate locks
lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():

    # Task 1 acquires lock_a first
    with lock_a:
        print("Task 1 acquired lock a")

        # Then Task 1 tries to acquire lock_b
        with lock_b:
            print("Task 1 acquired lock b")


def task2():

    # Task 2 acquires lock_b first
    with lock_b:
        print("Task 2 acquired lock b")

        # Then Task 2 tries to acquire lock_a
        with lock_a:
            print("Task 2 acquired lock a")


# Create two threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start both threads
t1.start()
t2.start()

# ⚠️ Potential DEADLOCK:
#
# Thread 1: holds lock_a → waiting for lock_b
# Thread 2: holds lock_b → waiting for lock_a
#
# Neither thread can continue, because each is waiting
# for a lock held by the other thread.