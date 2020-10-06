"""
Chapter 116: Multiprocessing
Section 116.1: Running Two Simple Processes

Section 116.2: Using Pool and Map
Pool is a class which manages multiple Workers (processes) behind the scenes and lets you, the programmer, use.
Pool(5) creates a new Pool with 5 processes, and pool.map works just like map but it uses multiple processes (the
amount defined when creating the pool).
Similar results can be achieved using map_async, apply and apply_async

Chapter 117: Multithreading
Threads allow Python programs to handle multiple functions at once as opposed to running a sequence of
commands individually. This topic explains the principles behind threading and demonstrates its usage

Section 117.1: Basics of multithreading
Using the threading module, a new thread of execution may be started by creating a new threading.Thread and
assigning it a function to execute:
The target parameter references the function (or callable object) to be run. The thread will not begin execution
until start is called on the Thread object.

Now that my_thread has run and terminated, calling start again will produce a RuntimeError. If you'd like to run
your thread as a daemon, passing the daemon=True kwarg, or setting my_thread.daemon to True before calling
start(), causes your Thread to run silently in the background as a daemon.

Create a Custom Thread Class
Using threading.Thread class we can subclass new custom Thread class. we must override run method in a
subclass.


Section 117.2: Communicating between threads

Section 117.3: Creating a worker pool
Using concurrent.futures.Threadpoolexecutor

Section 117.4: Advanced use of multithreads


Chapter 118: Processes and Threads
Threading with multiple processors permits programs to run multiple processes
simultaneously.

Section 118.1: Global Interpreter Lock
Python multithreading performance can often suffer due to the Global Interpreter Lock. In short, even though
you can have multiple threads in a Python program, only one bytecode instruction can execute in parallel at any
one time, regardless of the number of CPUs.

processes = multiprocessing.Process(target=process)
processes.start()
processes.join()

Section 118.2: Running in Multiple Threads

Section 118.3: Running in Multiple Processes

Section 118.4: Sharing State Between Threads
As all threads are running in the same process, all threads have access to the same data.
However, concurrent access to shared data should be protected with a lock to avoid synchronization issues.

Section 118.5: Sharing State Between Processes
Code running in different processes do not, by default, share the same data. However, the multiprocessing
module contains primitives to help share values across multiple processes.


Chapter 119: Python concurrency
Section 119.1: The multiprocessing module
The new processes are launched differently depending on the version of python and the platform on which the
code is running e.g.:
Windows uses spawn to create the new process.
With unix systems and version earlier than 3.3, the processes are created using a fork.
Note that this method does not respect the POSIX usage of fork and thus leads to unexpected behaviors,
especially when interacting with other multiprocessing libraries.
With unix system and version 3.4+, you can choose to start the new processes with either fork, forkserver
or spawn using multiprocessing.set_start_method at the beginning of your program. forkserver and
spawn methods are slower than forking but avoid some unexpected behaviors

POSIX fork usage:
After a fork in a multithreaded program, the child can safely call only async-signal-safe functions until
such time as it calls execve.

If you use a Lock in MainThread and pass it to another thread which is supposed to lock it at some point. If
the fork occurs simultaneously, the new process will start with a locked lock which will never be released as
the second thread does not exist in this new process.


Section 119.2: The threading module

Section 119.3: Passing data between multiprocessing processes
Because data is sensitive when dealt with between two threads (think concurrent read and concurrent write can
conflict with one another, causing race conditions), a set of unique objects were made in order to facilitate the
passing of data back and forth between threads. Any truly atomic operation can be used between threads, but it is
always safe to stick with Queue.

my_Queue=multiprocessing.Queue()
#Creates a queue with an undefined maximum size
#this can be dangerous as the queue becomes increasingly large
#it will take a long time to copy data to/from each read/write thread

Chapter 120: Parallel computation
Section 120.1: Using the multiprocessing module to parallelise tasks

import multiprocessing
def fib(n):
    ""computing the Fibonacci in an inefficient way
    was chosen to slow down the CPU.""
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

p = multiprocessing.Pool()
print(p.map(fib,[38,37,36,35,34,33]))
# Out: [39088169, 24157817, 14930352, 9227465, 5702887, 3524578]

As the execution of each call to fib happens in parallel, the time of execution of the full example is 1.8× faster than
if done in a sequential way on a dual processor.

Section 120.2: Using a C-extension to parallelize tasks
The idea here is to move the computationally intensive jobs to C (using special macros), independent of Python, and
have the C code release the GIL while it's working
#include "Python.h"
...
PyObject *pyfunc(PyObject *self, PyObject *args) {
    ...
    Py_BEGIN_ALLOW_THREADS
    // Threaded C code
    ...
    Py_END_ALLOW_THREADS
    ...
}

Section 120.3: Using Parent and Children scripts to execute code in parallel

Section 120.4: Using PyPar module to parallelize
PyPar is a library that uses the message passing interface (MPI) to provide parallelism in Python.


"""

#Section 116.1: Running Two Simple Processes
print("---Section 116.1: Running Two Simple Processes-----")
import multiprocessing
import time
from random import randint
from multiprocessing import Pool


def countUp():
    i = 0
    while i <= 3:
        print('Up:\t{}'.format(i))
        time.sleep(randint(1, 3)) # sleep 1, 2 or 3 seconds
        i += 1
def countDown():
    i = 3
    while i >= 0:
        print('Down:\t{}'.format(i))
        time.sleep(randint(1, 3)) # sleep 1, 2 or 3 seconds
        i -= 1

def cube(x):
    return x ** 3


#Section 117.1: Basics of multithreading
print("----Section 117.1: Basics of multithreading-------")
import threading
def foo():
    print("Hello threading!")
my_thread = threading.Thread(target=foo)
#Starting a Thread
my_thread.start()

#Joining a Thread
import requests
from threading import Thread
from queue import Queue

q = Queue(maxsize=20)
def put_page_to_q(page_num):
    q.put(requests.get('http://advantageonlineshopping.com//page_%s.html' % page_num))
def compile(q):
    # magic function that needs all pages before being able to be executed
    if not q.full():
        print("Value Error")
        #raise ValueError
    else:
        print("Done compiling!")
threads = []
for page_num in range(20):
    t = Thread(target=requests.get, args=(page_num,))
    t.start()
    threads.append(t)
# Next, join all threads to make sure all threads are done running before
# we continue. join() is a blocking call (unless specified otherwise using
# the kwarg blocking=False when calling join)
for t in threads:
    t.join()
# Call compile() now, since all threads have completed
compile(q)

#Create a Custom Thread Class
import time
class Sleepy(Thread):
    def run(self):
        time.sleep(5)
        print("Hello form Thread")


#Section 117.2: Communicating between threads
# create a data producer
def producer(output_queue):
    while True:
        data = data_computation()
        output_queue.put(data)
        # create a consumer
def consumer(input_queue):
    while True:
        # retrieve data (blocking)
        data = input_queue.get()
        # do something with the data
        # indicate data has been consumed
        input_queue.task_done()
q1 = Queue()
t1 = Thread(target=consumer, args=(q1,))
t2 = Thread(target=producer, args=(q1,))
t1.start()
t2.start()


#Section 117.3: Creating a worker pool
print("-----Section 117.3: Creating a worker pool-------")
from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor
def echo_server(addr):
    print('Echo server running at', addr)
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)
echo_server(('',15000))

#Section 117.4: Advanced use of multithreads
print("------Section 117.4: Advanced use of multithreads--------")

#Section 117.5: Stoppable Thread with a while Loop
print("---Section 117.5: Stoppable Thread with a while Loop---")
class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""
    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()
    def stop(self):
        self._stop_event.set()
    def join(self, *args, **kwargs):
        self.stop()
        super(StoppableThread,self).join(*args, **kwargs)
    def run()
        while not self._stop_event.is_set():
            print("Still running!")
            time.sleep(2)
        print("stopped!"

obj = {}
obj_lock = threading.Lock()

def objify(key, val):
    print("Obj has %d values" % len(obj))

with obj_lock:
    obj[key] = val
print("Obj now has %d values" % len(obj))
ts = [threading.Thread(target=objify, args=(str(n), n)) for n in range(4)]
for t in ts:
    t.start()
for t in ts:

#Section 118.5: Sharing State Between Processes
print("----Section 118.5: Sharing State Between Processes------")




if __name__ == '__main__':
    # Initiate the workers.
    # Initiate the workers.
    workerUp = multiprocessing.Process(target=countUp)
    workerDown = multiprocessing.Process(target=countDown)
    # Start the workers.
    workerUp.start()
    workerDown.start()
    # Join the workers. This will block in the main (parent) process
    # until the workers are complete.
    workerUp.join()
    workerDown.join()
    pool = Pool(5)
    result = pool.map(cube, [0, 1, 2, 3])
    t = Sleepy()
    t.start()  # start method automatic call Thread class run method.
    # print 'The main program continues to run in foreground.'
    t.join()
    print("The main program continues to run in the foreground.")
