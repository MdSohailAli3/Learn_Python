import threading
import time


def monitor_tea_temp():

    # Runs continuously in the background
    while True:
        print("Monitoring tea temperature...")

        # Blocks this thread for 2 seconds
        time.sleep(2)


# daemon=False by default
# This is a NON-DAEMON thread, so it keeps the program alive
t = threading.Thread(target=monitor_tea_temp)

# Start the thread
t.start()

# Main thread reaches this line and finishes
print("Main program done")

# ⚠️ Program does NOT exit here because the non-daemon
# thread is still running its infinite while loop.


# profilers - to check the stats of function call and time
#DEFAULT->  python -m cProfile -s time 08_non_daemon.py

# opensource ->  py spy, vprof