import threading
import time
from threading import current_thread


def myThred(arg1, arg2):
    print(current_thread().getName(), 'start')
    print('%s %s' % (arg1, arg2))
    time.sleep(1)
    print(current_thread().getName(), 'stop')


for i in range(1, 6, 1):
    # t1 = myThred(i, i + 1)
    t1 = threading.Thread(target=myThred, args=(i, i + 1))
    t1.start()

print(current_thread().getName(), 'end')
