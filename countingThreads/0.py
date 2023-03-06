import _thread as thread, time


def counter(id, count):
    for i in range(count):
        time.sleep(1)
        print(f'{id} => {i}')


for i in range(5):
    thread.start_new_thread(counter, (i, 5))

time.sleep(5)
print('main thread exiting')