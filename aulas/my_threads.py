from time import sleep
from threading import Thread
from threading import Lock

# # print('Starting main thread...')
# # for i in range(10):
# #     print(i)
# #     sleep(0.5)
# # print('Main thread finished!')

# class MyThread(Thread):
#     def __init__(self, text, delay):
#         self.text = text
#         self.delay = delay

#         Thread.__init__(self) #super().__init__()
#         # Thread.__init__(self, target=self.run) # Another way to do it

#     def run(self):
#         sleep(self.delay)
#         print(self.text)

# t1 = MyThread('Hello from the thread!', 7)
# t1.start() # Start the thread

# t2 = MyThread('Hello from the thread number 2!', 4)
# t2.start() # Start the thread

# t2 = MyThread('Hello from the thread number 3!', 11)
# t2.start() # Start the thread

# for i in range(25):
#     print(i)
#     sleep(0.5)

'''
def willTakeaWhile(text, time):
    sleep(time)
    print(text)
    return True

t1 = Thread(target=willTakeaWhile, args=('Will take a while...', 15))
t1.start() # Start the thread

t2 = Thread(target=willTakeaWhile, args=('Will take a while...',9))
t2.start() # Start the thread

t3 = Thread(target=willTakeaWhile, args=('Will take a while...', 7))
t3.start() # Start the thread

for i in range(20):
    print(i)
    sleep(1)
'''

'''
def willTakeaWhile(text, time):
    sleep(time)
    print(text)
    return True

t1 = Thread(target=willTakeaWhile, args=('Will take a while...', 10))
t1.start() # Start the thread

t1.join() # Wait for the thread to finish

# while t1.is_alive():
#     print('Thread is still alive...')
#     sleep(2)

print('Thread finished!')
'''


class Tickets:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.lock = Lock()

    def buy_ticket(self, tickets):
        self.lock.acquire()
        if self.total_tickets < tickets:
            print(f'Not enough tickets available!')
            self.lock.release()
            return
        self.total_tickets -= tickets
        print(f'{tickets} tickets bought!, Still available: {self.total_tickets}')
        sleep(1.7)
        self.lock.release()
        return

if __name__ == '__main__':
    tickets = Tickets(19)

    for i in range(1, 10):
        t = Thread(target=tickets.buy_ticket, args=(i,))
        t.start()

