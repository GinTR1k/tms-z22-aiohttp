from threading import Thread, Event
from time import sleep, time


event = Event()


def do_something(i):
    event.wait()
    print(f'child {i}, {time()}')


threads = [Thread(target=do_something, args=(i,)).start() for i in range(10)]

# for i in range(5):
#     print(f'main thread: {i}, {time()}')
#     sleep(1)

print('main thread:', time())
sleep(3)
event.set()
print('main thread done')
