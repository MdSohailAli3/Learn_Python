# Multiprocessing Queue → safely passes data between separate processes 
# that do not normally share memory.
# from multiprocessing import Process, Queue

# def prepare_chai(queue):
#     queue.put("Masala chai is ready")



# if __name__ == '__main__':
#     queue = Queue()

#     p = Process(target=prepare_chai, args=(queue,))
#     p.start()
#     p.join()
#     print(queue.get())




from multiprocessing import Process, Queue


def producer(queue):
    for i in range(5):
        queue.put(i)
        print(f"Produced: {i}")


def consumer(queue):
    for i in range(5):
        value = queue.get()
        print(f"Consumed: {value}")


if __name__ == "__main__":

    # Create a multiprocessing Queue
    queue = Queue()

    # Producer puts data into the Queue
    p1 = Process(target=producer, args=(queue,))

    # Consumer takes data from the Queue
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()