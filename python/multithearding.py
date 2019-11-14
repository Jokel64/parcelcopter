import logging
import threading
import time


def warten(name):
    logging.info("Thread %s: starting", name)
    empfangen = False

    while not empfangen:
        empfangen = True
        logging.info("Thread %s: warten", name)

    logging.info("Thread %s: GPS Signale Empfangen", name)


def aufsteigen(name):
   logging.info("Thread %s: starting", name)

    # motoren an
    # h_akt = 0 # in Metern
    # if(h_akt = h_soll)

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

logging.info("Main    : before creating thread")
x = threading.Thread(target=warten, args=('warten',))
logging.info("Main    : before running thread")
x.start()
logging.info("Main    : wait for the thread to finish")
x.join()
logging.info("Main    : all done")

