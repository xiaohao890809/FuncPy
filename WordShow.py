from collections import Counter
import numpy as np
import wordcloud

# 进行分词
from PIL import Image
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt


my_list = ['a','b','a','c','d','e','e','f','g','h','j','f','d','a','a','a']
with open('word.txt','w') as fw:
    for k,v in Counter([i for i in my_list]).most_common(350):
        fw.write('%s,%d\n' %(k,v))

# 关于python3,numpy-loadtxt的编码问题
# http://blog.csdn.net/akon_wang_hkbu/article/details/73866523
list_word = np.loadtxt('word.txt',delimiter=',',dtype=bytes).astype(str)
frequencies = dict(list_word.tolist()[:50]) # 取前50个
frequencies = [(k,int(v)) for k,v in frequencies.items()]

# 加载图片
my_pic = np.array(Image.open('girl.jpg'))
wc = WordCloud(background_color="white",max_words=2000,mask=my_pic)
# 生成颜色绘图
imgae_colors = ImageColorGenerator(my_pic)
wc.fit_words(dict(frequencies))
plt.figure()
# plt.imshow(wc)
plt.imshow(wc.recolor(color_func=imgae_colors),interpolation="bilinear")
plt.axis('off')
# 保存图片
# plt.savefig('1.png',dpi=200)
plt.show()


