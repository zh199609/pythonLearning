import os

import pytest

if __name__ == '__main__':
    # print("__file__:", __file__)
    # print("返回当前文件所在的目录：", os.path.dirname(__file__))
    # print("返回d所在目录规范的绝对路径:", os.path.abspath('./'))
    # print("返回d所在目录规范的绝对路径:", os.path.abspath(__file__))
    pytest.main(['-s','-v', '../conftestDemo/'])
