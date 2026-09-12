import asyncio
import aiohttp


# async def → defines a COROUTINE.
# This coroutine performs an asynchronous HTTP request.
async def fetch_url(session, url):

    # session.get() makes an async HTTP request.
    # 'async with' waits for the response without blocking
    # the event loop and automatically handles/cleans up the response.
    async with session.get(url) as response:

        # response.status → HTTP status code (e.g. 200 = OK)
        print(f"Fetched {url} with status {response.status}")


# Main coroutine that coordinates all our tasks.
async def main():

    # Create a list containing the same URL 3 times.
    # We will make 3 HTTP requests concurrently.
    urls = ["https://httpbin.org/delay/2"] * 3

    # ClientSession → reusable HTTP client.
    # Reusing one session is better than creating a new session
    # for every request.
    async with aiohttp.ClientSession() as session:

        # Create coroutine objects for each URL.
        #
        # IMPORTANT:
        # At this point these are coroutine objects.
        # They haven't all started executing yet.
        tasks = [fetch_url(session, url) for url in urls]

        # Equivalent idea:
        # tasks = [task1, task2, task3]

        # gather() runs all the coroutines concurrently.
        #
        # *tasks → unpack the list:
        # gather(task1, task2, task3)
        #
        # await → wait until ALL requests are finished.
        await asyncio.gather(*tasks)


# asyncio.run() creates and starts the EVENT LOOP,
# runs the main() coroutine, and stops the loop when it finishes.
asyncio.run(main())