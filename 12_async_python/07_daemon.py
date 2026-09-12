import threading
import time


def monitor_tea_temp():
    # Runs continuously in the background
    while True:
        print("Monitoring tea temperature...")

        # Blocks only this background thread for 2 seconds
        time.sleep(2)


# daemon=True → thread automatically stops when the main program exits
t = threading.Thread(target=monitor_tea_temp, daemon=True)

# Start the background thread
t.start()

# Main thread finishes here
# Since t is a daemon thread, Python can exit without waiting for it
# time.sleep(4)
print("Main program done")