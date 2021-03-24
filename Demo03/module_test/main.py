import sys

from Demo03 import module_zh
from Demo03 import module_a

#from module_zh import *
print(sys.path)
module_zh.say_hello()
module_a.a.say_a()