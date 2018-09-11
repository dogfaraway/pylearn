# 定义一个字符串Hello Python 并使用print( )输出

str_1 = "Hello Python"
print(str_1)

# 定义第二个字符串Let‘s go并使用print( )输出

str_2 = "Let's go"
print(str_2)

# 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出

str_3 = ' "The Zen of Python" -- by Tim Peters'
print(str_3)

# 定义两个字符串分别为 xyz 、abc

str_a = 'xyz'
str_b = 'abc'

# 对两个字符串进行连接
str_c = str_a + str_b

print(str_c)

# 取出xyz字符串的第二个和第三个元素

print(str_c[1:3])

# 对abc输出10次

print(str_c * 10)

# 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出

print('a' in str_a)
print('a' in str_b)

# 定义一个含有5个数字的列表

list_1 = [1, 2, 3, 4, 5]

# 为列表增加一个元素 100
list_1.append(100)
print(list_1)
# 使用remove()删除一个元素后观察列表的变化
list_1.remove(3)
print(list_1)

# 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
print(list_1[0:3])
print(list_1[4])

# 定义一个任意元组，对元组使用append() 查看错误信息
group_any = ('a','b')
#group_any.append(2)
print(group_any)

# 访问元组中的倒数第二个元素
print(group_any[1])

# 定义一个新的元组，和 1. 的元组连接成一个新的元组
group_new = ('c',3)
group_new1 = group_any + group_new
print(group_new1)

# 计算元组元素个数
print(len(group_new1))
print(group_new1.__len__())