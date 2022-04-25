import threading
from time import sleep,ctime

def music(func):
    for i in range(3):
        print(func,ctime())
        sleep(3)

def movie(func):
    for i in range(3):
        print(func,ctime())
        sleep(1)


threads = []
t1 = threading.Thread(target=music,args=('爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=('阿凡达',))
threads.append(t2)

for t in threads:
    t.setDaemon(True)
    t.start()

for t in threads:
    t.join()

print('over',ctime())
