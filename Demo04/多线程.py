# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 多线程.py
# @Author  : Administrator
# @Time    : 2021-08-28 15:37:32
# @Desc    : 多线程
from random import randint
from threading import Thread
from time import sleep, time


def download_task(filename):
    print(f"开始下载{filename}……")
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f'{filename}下载完成，耗费{time_to_download}秒！')


def main1():
    start = time()
    t1 = Thread(target=download_task, args=("Python从入门到住院.pdf",))
    t1.start()
    t2 = Thread(target=download_task, args=("Python从入门到住院.pdf",))
    t2.start()

    t1.join()
    t2.join()
    end = time()

    print("总共耗时：%.2f" % (end - start))


class DownLoadTask(Thread):
    """
    自定义线程类
    """
    def __init__(self, filename):
        super(DownLoadTask, self).__init__()
        self.filename = filename

    def run(self) -> None:
        print('开始下载%s...' % self.filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self.filename, time_to_download))


def main2():
    start = time()
    p1 = DownLoadTask("Python从入门到住院.pdf")
    p2 = DownLoadTask("Peking Hot.avi")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

if __name__ == '__main__':
    main2()