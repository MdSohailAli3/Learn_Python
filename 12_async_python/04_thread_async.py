import asyncio
import time

from concurrent.futures import ThreadPoolExecutor
  

# Normal synchronous function.
# This function contains a BLOCKING operation (time.sleep).
def check_stock(item):

    print(f"Checking {item} in store...")

    # Blocking operation:
    # This blocks the thread for 3 seconds.
    # If we called this directly inside an async function,
    # it would BLOCK the asyncio event loop.
    time.sleep(3)

    return f"{item} stock: 42"


# Main asyncio coroutine.
async def main():

    # Get the currently running EVENT LOOP.
    # The event loop manages and schedules our async tasks.
    loop = asyncio.get_running_loop()

    # Create a ThreadPoolExecutor.
    # It allows us to run blocking/synchronous functions
    # in a separate thread instead of blocking the event loop.
    with ThreadPoolExecutor() as pool:

        # run_in_executor() sends the blocking function
        # to the thread pool.
        #
        # Arguments:
        #   pool        → where the function should run
        #   check_stock → blocking function
        #   "Masala chai" → argument passed to check_stock()
        #
        # await → wait asynchronously for the thread's result.
        result = await loop.run_in_executor(
            pool,
            check_stock,
            "Masala chai"
        )
        # Run this blocking function in a thread so that
        #  it doesn't block my asyncio event loop, and let me 
        # asynchronously wait for its result.

        print(result)


# Starts the asyncio event loop
# and runs the main() coroutine.
asyncio.run(main())