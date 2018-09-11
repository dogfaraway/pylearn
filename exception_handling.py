# try:
#     year = int(input('input year'))
# except ValueError:
#     print('年份要输入数字')

# try:
#     print(1/'a')
# except ZeroDivisionError as e:
#     print('%s' %e)

# try:
#     raise NameError('HelloError')
# except NameError:
#     print('my custom error')
# finally:

try:
    a=open('name1.txt')
except Exception as e:
    print(e)
finally:
    a.close()