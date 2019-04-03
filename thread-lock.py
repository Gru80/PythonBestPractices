"""
Demonstration of the tread lock feature to avoid race conditions
"""

import threading
import logging
import concurrent.futures
import time

class LockDown:
    """ Thread lock demo class.

    A Value is stored, the value can be modified (+1) with it's update method
    """

    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update_me(self, name):
        """ Update the value

        Update the value of the Class by one
        """

        logging.info("Thread %s", name)
        with self._lock:
            logging.info("Thread %s has lock", name)
            copy = self.value
            copy += 1
            time.sleep(0.2)
            self.value = copy
            
            logging.info("Thread %s releasing with value %d", name, self.value)
        logging.info("Thread %s release done", name)

if __name__ == "__main__":
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt="%M:%S")
    
    datab = LockDown()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2)as executerr:
        for index in range(4):
            executerr.submit(datab.update_me, index)
    logging.info("Main done - end val: %d", datab.value)