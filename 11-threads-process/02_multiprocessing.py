from multiprocessing import Process
import time


# This function will be executed by each separate process.
def brew_chai(name):
    print(f"Start of {name} chai brewing")

    # Simulates a time-consuming task.
    # Other processes can run while this process is sleeping.
    time.sleep(3)

    print(f"End of {name} chai brewing")


# Ensures the code below runs only when this file is executed directly.
# IMPORTANT for multiprocessing, especially on Windows/macOS.
if __name__ == "__main__":

    # Create 3 separate processes.
    # Each process will run brew_chai().
    chai_makers = [
        Process(
            target=brew_chai,              # Function the process should execute
            args=(f"Chai Maker #{i+1}", )  # Arguments passed to brew_chai()
        )
        for i in range(3)
    ]

    # Start all 3 processes.
    # Each process can execute independently and potentially in parallel.
    for p in chai_makers:
        p.start()

    # Wait for every process to finish before continuing.
    # join() makes the main process wait for the child process.
    for p in chai_makers:
        p.join()

    # This runs only after ALL chai-making processes have completed.
    print("All chai served")