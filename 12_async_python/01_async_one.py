import asyncio
# asyncio = Python's built-in library for asynchronous programming.
# Useful mainly for I/O-bound tasks like API calls, database queries,
# file operations, etc., where the program spends time waiting.


#Threading = multiple workers
# Asyncio = one worker managing multiple tasks by switching whenever a task waits

async def brew_chai():
    # 'async def' defines a COROUTINE.
    # A coroutine is like a special function that can be PAUSED
    # and later RESUMED.

    print("Brewing chai...")

    # 'await' pauses this coroutine until the operation is complete.
    # IMPORTANT: it does NOT block the whole event loop.
    # While waiting for 2 seconds, asyncio can run other coroutines/tasks.
    await asyncio.sleep(2) #does not block the main thread

    print("Chai is ready")


# asyncio.run() starts the asyncio EVENT LOOP,
# runs the coroutine, and waits until it finishes.
asyncio.run(brew_chai())

# Event loop = "I'll manage all these paused/ready tasks and run whichever can make progress."
