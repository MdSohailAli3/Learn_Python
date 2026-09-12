import asyncio
import time

async def brew(name):

    print(f"Brewing {name}...")

    await asyncio.sleep(3)  # Pause THIS coroutine for 3 seconds
                           # Event loop can run other coroutines meanwhile

    # time.sleep(3)        # ❌ Blocking! This would block the event loop

    print(f"{name} is ready...")


async def main():

    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Ginger chai"),
    )


asyncio.run(main())