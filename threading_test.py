"""
Simple demonstration of the threading concept
"""

import logging
import threading
import time

def thread_function(name):
    """ A simple function that just logs and sleeps in between """
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    
    x = threading.Thread(target=thread_function, args=(1,))
    
    # With deamon=True, the Thread finishing statement will not be reached
    #x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
        
    # If the main thread should wait for the x thread, join() has to be called
    #x.join()

    logging.info("Main    : all done")
    