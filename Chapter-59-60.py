"""
Chapter 59: Queue Module
The Queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded
programming when information must be exchanged safely between multiple threads. There are three types of
queues provides by queue module,Which are as following : 1. Queue 2. LifoQueue 3. PriorityQueue Exception which
could be come: 1. Full (queue overflow) 2. Empty (queue underflow)

Section 59.1: Simple example


Chapter 60: Deque Module
Parameter                           Details
iterable                Creates the deque with initial elements copied from another iterable.
maxlen                  Limits how large the deque can be, pushing out old elements as new are added.


Section 60.1: Basic deque using
The main methods that are useful with this class are popleft and appendleft

Section 60.2: Available methods in deque


Section 60.3: limit deque size

Section 60.4: Breadth First Search
The Deque is the only Python data structure with fast Queue operations. (Note queue.Queue isn't normally suitable,
since it's meant for communication between threads.) A basic use case of a Queue is the breadth first search.


"""
from multiprocessing import Queue
from collections import deque


question_queue = Queue()

for x in range(1,10):
    temp_dict = ('key', x)
    question_queue.put(temp_dict)

while(not question_queue.empty()):
    item = question_queue.get()
    print(str(item))

#Section 60.1: Basic deque using
print("-------Section 60.1: Basic deque using-----------")

d = deque([1, 2, 3])
p = d.popleft() # p = 1, d = deque([2, 3])
d.appendleft(5) # d = deque([5, 2, 3])

#Section 60.2: Available methods in deque
print("------Section 60.2: Available methods in deque--------------")

dl = deque() # deque([]) creating empty deque
dl = deque([1, 2, 3, 4]) # deque([1, 2, 3, 4])
dl.append(5) # deque([1, 2, 3, 4, 5])
dl.appendleft(0) # deque([0, 1, 2, 3, 4, 5])
dl.extend([6, 7]) # deque([0, 1, 2, 3, 4, 5, 6, 7])
dl.extendleft([-2, -1]) # deque([-1, -2, 0, 1, 2, 3, 4, 5, 6, 7])
dl.pop() # 7 => deque([-1, -2, 0, 1, 2, 3, 4, 5, 6])
dl.popleft() # -1 deque([-2, 0, 1, 2, 3, 4, 5, 6])
dl.remove(1) # deque([-2, 0, 2, 3, 4, 5, 6])
dl.reverse() # deque([6, 5, 4, 3, 2, 0, -2])

#Section 60.3: limit deque size
print("----------Section 60.3: limit deque size-----------")

d = deque(maxlen=3) # only holds 3 items
d.append(1) # deque([1])
d.append(2) # deque([1, 2])
d.append(3) # deque([1, 2, 3])
d.append(4) # deque([2, 3, 4]) (1 is removed because its maxlen is 3)

#Section 60.4: Breadth First Search
print("--------Section 60.4: Breadth First Search----------")
def bfs(graph, root):
    distances = {}
    distances[root] = 0
    q = deque([root])
    print(distances)
    while q:
        # The oldest seen (but not yet visited) node will be the left most one.
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                # When we see a new node, we add it to the right side of the queue.
                q.append(neighbor)
    return distances

graph = {1:[2,3], 2:[4], 3:[4,5], 4:[3,5], 5:[]}

print(bfs(graph, 1))
print(bfs(graph, 3))