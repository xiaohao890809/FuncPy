# added by xiaohao
# time: 2018.03.07 21:27
# 装饰器的用法

def log_cost_time(func):
    def wrapped(*args, **kwargs):
        import time
        begin = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            print('func %s cost %s' %(func.__name__,time.time()-begin))
    return wrapped

@log_cost_time
def complex_func(num):
    ret = 0
    for i in range(num):
        ret += i*i
    return ret

if __name__ == '__main__':
    print(complex_func(1000))




