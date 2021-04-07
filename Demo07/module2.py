# 在module2.py使用module1中定义的涵义

import module1
from module1 import my_max

# import module1 as m1

print(module1.my_sum(10, 15))
print(my_max(10,16))
