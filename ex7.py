# 1. 创建一个文件，并写入当前日期

import  datetime
now = datetime.datetime.now()
with open('c.txt','w') as f:
    f.write(str(now))



# 2. 再次打开这个文件，读取文件的前4个字符后退出

with open('c.txt') as f:
    text_4 = f.read(4)
    print(text_4)