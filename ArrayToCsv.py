# 数组转为 csv 存储
import numpy as np
import pandas as pd

arr1 = np.arange(100).reshape(10,10)
data1 = pd.DataFrame(arr1)
data1.to_csv('data1.csv',index=False,header=False)