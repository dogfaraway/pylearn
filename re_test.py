import re

p = re.compile('ca*t')
print(p.match('caaaaat'))

##
import re

p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2018-05-10').group(2))
print(p.match('2018-05-10').groups())

year, month, date = p.match('2018-05-10').groups()

print(p.search('aa2018-05-10a'))
