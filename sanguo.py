# 读取人物名称
# f = open('name.txt',encoding='UTF-8')
# data = f.read()
# print(data.split('|'))
#
# # 读取兵器名称
# f2 = open('weapon.txt',encoding="utf-8")
# # data2 = f2.read()
# i =1
# for line in f2.readlines():
#     if i %2 ==1:
#         print(line.strip('\n'))
#     i += 1
#
# f3 = open('sanguo.txt',encoding='gb18030')
# print(f3.read().replace('\n',''))

def func(filename):
    print(open(filename,encoding='utf-8').read())
    print('test func')

func('name.txt')