
import threading
import time
from myThread import *
from GUI import *

# Create new threads
thread1 = GUI(1, "Thread-1")
thread2 = myThread(2, "Thread-2", 4)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")
