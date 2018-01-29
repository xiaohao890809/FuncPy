# added by xiaohao
# time: 2018.01.29 22:49
# 如何计算函数的执行时间(耗时)

import time
def timer(fn, args):
    start = time.clock()
    return fn(*args),time.clock()-start

print(timer(max, range(1000)))