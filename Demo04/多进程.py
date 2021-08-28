# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 多进程.py
# @Author  : Administrator
# @Time    : 2021-08-28 15:30:05
# @Desc    : 多进程
from multiprocessing import Process
from random import randint
from time import time, sleep


def download_task(filename):
    print(f"开始下载{filename}……")
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f'{filename}下载完成，耗费{time_to_download}秒！')


if __name__ == '__main__':
    print(time())

    start = time()
    p1 = Process(target=download_task, args=("Python从入门到住院.pdf",))
    p1.start()
    p2 = Process(target=download_task, args=("Peking Hot.avi",))
    p2.start()

    # join 方法表示等待进程执行结束，才会往下执行
    p1.join()
    p2.join()
    end = time()
    print('总共耗时：%.2f' % (end - start))
