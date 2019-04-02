"""
Simple demonstration of multi-threading
"""

import logging
import threading
import time

#for the ThreadPoolExecuter Demo
import concurrent.futures

def thread_function(name):
    """ A simple function that just logs and sleeps in between """
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for i in range(3):
        logging.info("Starting " + str(i))
        x = threading.Thread(target=thread_function, args=(i,))
        x.start()
        threads.append(x)

    for index, thread in enumerate(threads):
        thread.join()
        logging.info("Thread %s done", thread)

    logging.info("-"*30)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as exec:
        exec.map(thread_function, range(3))