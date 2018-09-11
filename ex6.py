# 定义一个字典，分别使用a、b、c、d作为字典的关键字，值为任意内容

dict_a = {'a':'啊', 'b':2,'c':'3','d':5}
print(dict_a)

# 为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕

dict_a['c'] = 'cake'
print(dict_a)

# 取出字典中关键字为d的值

print(dict_a['d'])

# 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕

str_1 = input('请输入一个字符串，例如“hello” ')
dict_set ={}
for i in range(1,len(str_1)):
    dict_set[i] = str_1[i]
    i += 1

print(dict_set)

# 1. 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕
str1 = 'hello'
# 集合里的元素不能重复
print(set(str1))