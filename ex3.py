# 汇率计算

usd = 100
usd_cny_rate = 6.8327

cny = usd * usd_cny_rate

print(cny)
print('{dol}美元兑换的人民币数量为{yuan}'.format(dol=usd, yuan=usd * usd_cny_rate))