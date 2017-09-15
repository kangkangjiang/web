class AA():
    @staticmethod
    def a():
        return 123


aaaaa=AA()
v=aaaaa.a
b=AA.a

print(type(v),type(b),isinstance(  v ,staticmethod))



# 正则表达式
# import re
# text = input("Please input your Email address：\n")
# if re.match(r'^[0-9a-zA-Z_]{1,19}@[0-9a-zA-Z]{1,13}.[com,cn,net]{1,3}$',text):
# #if re.match(r'[0-9a-zA-Z_]{0,19}@163.com',text):
#     print('Email address is Right!')
# else:
#     print('Please reset your right Email address!')


# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C','d','e']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(0.5)
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         time.sleep(1)
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
#     print()

