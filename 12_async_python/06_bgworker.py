import asyncio
import threading
import time


# Normal synchronous function running in a SEPARATE THREAD.
def background_worker():

    # Infinite loop → keeps the background worker running.
    while True:

        # Blocking operation.
        # This pauses ONLY the background thread for 1 second.
        time.sleep(1)

        print(f"Logging the system health 🕰️")


# Async coroutine managed by the asyncio EVENT LOOP.
async def fetch_orders():

    # Non-blocking wait.
    # This pauses this coroutine for 3 seconds,
    # but the asyncio event loop can run other coroutines meanwhile.
    await asyncio.sleep(3)

    print("🎁 order fetched")


# Start background_worker() in a separate thread.
#
# daemon=True means:
# → this thread runs in the background
# → when the main program exits, this thread is automatically stopped
threading.Thread(
    target=background_worker,
    daemon=True
).start()


# Start the asyncio EVENT LOOP
# and run the fetch_orders() coroutine.
asyncio.run(fetch_orders())