#使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出

# text_input = input("请输入一段文字")
#
# if text_input.__len__() == 10:
#     print('输入的文字长度为10个字符')
# else:
#     print('输入的文字长度不是10个字符')


# 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，
# 如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出

# text_input_2 = input('输入一个1-40之间的数字')
#
# num_to_int = int(text_input_2)
#
# if 1 <= num_to_int <= 10:
#     print('数字在1～10之间')
# elif 11 <= num_to_int <= 20:
#     print('数字在11～20之间')
# elif 21 <= num_to_int <= 30:
#     print('数字在21～30之间')
# elif 31 <= num_to_int <= 40:
#     print('数字在21～30之间')
# else:
#     print('数字在31～40之间')

# 使用for语句输出1-100之间的所有偶数

# for i in range(1,100):
#     if i%2 ==0:
#         print('%s是偶数' %(i))


# 使用while语句输出1-100之间能够被3整除的数字
i=0
while i <= 100:
    if i % 3 == 0:
        print('%s能被3整除' %(i) )
    i+=1