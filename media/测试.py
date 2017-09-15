#  线程
import time, threading

# 新线程执行的代码:
def loop():
    print('1thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
if __name__=='__main__':
    print('2thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


# 进程
# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')



#''''装饰器

# import  time
#
# def pp():
#     def ss(func):
#         def aa(*args,**kwargs):
#             now=time.clock()
#             time.sleep(2)
#             end=time.clock()
#             print("开始")
#             func(*args,**kwargs)
#             print("介绍")
#             times=end-now
#             return print(times)
#         return aa
#     return ss
#
# @pp()
# def A():
#     print("<<<>>>>>")
# A()
