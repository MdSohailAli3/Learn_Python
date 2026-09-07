# Concurrency: multiple tasks make progress by switching between them; 
# Parallelism: multiple tasks execute simultaneously on multiple CPU cores.


# concurrency = 
                # threading.Thread
                # asyncio 

# multiprocessing = 
                # multiprocessing.Process
                # concurrent.futures.ProcessPoolExecutor
import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)
        
# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai) # target should be the function

order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")