intvar = 1
floatvar = 1.9
print("-----------------2-------------------------")
# 2
res = intvar + floatvar
print(f'{res}, type-> {type(res)}')
# 3
print("-----------------3-------------------------")
floatvar = int(floatvar)
print(f'{floatvar}, type-> {type(floatvar)}')

# Decimal Part is removed when we typecast float to int
# 1.9 is converted to 1