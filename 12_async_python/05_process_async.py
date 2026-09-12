import asyncio
from concurrent.futures import ProcessPoolExecutor


# Normal synchronous function.
# This is the CPU-bound work we want to run in a separate PROCESS.
def encrypt(data):

    # [::-1] reverses the string.
    # Here it is just a simple example of "encryption".
    return f"🔒 {data[::-1]}"


# Main asyncio coroutine.
async def main():

    # Get the currently running EVENT LOOP.
    # The event loop manages our async tasks.
    loop = asyncio.get_running_loop()

    # Create a ProcessPoolExecutor.
    # Unlike ThreadPoolExecutor, this creates separate PROCESSES.
    #
    # Useful for CPU-bound tasks because processes can run
    # independently of Python's GIL.
    with ProcessPoolExecutor() as pool:

        # run_in_executor() sends the blocking/CPU-bound function
        # to the process pool instead of running it directly
        # on the asyncio event-loop thread.
        #
        # Arguments:
        #   pool    → ProcessPoolExecutor
        #   encrypt → function to execute
        #   data    → argument passed to encrypt()
        #
        # await → asynchronously wait for the process to return
        # its result while keeping the event loop available.
        result = await loop.run_in_executor(
            pool,
            encrypt,
            "credit_card_1234"
        )

        print(f"{result}")


# IMPORTANT when using multiprocessing:
#
# if __name__ == "__main__"
# prevents the multiprocessing code from being executed
# again when Python creates/spawns child processes.
if __name__ == "__main__":

    # Start the asyncio event loop
    # and run the main() coroutine.
    asyncio.run(main())