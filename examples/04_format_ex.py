'''
num = input('number: ')
add = input('address')
name = input('name : ')
phone = input('phone')
'''

item1, item2 = 'airpod', 'usb 120GB'
unit1, unit2 = int(input(item1 + ' unit :')), int(input(item2 + ' unit : '))
qty1, qty2 = 1, 2
price1, price2 = unit1*qty1, unit2*qty2
recv = 200000


print('{:-^70}'.format('python shop'))
print(
    '{:<70}\n{:<70}\n{:<70}\n{:<70}'\
    .format('No.  : 11212','Addr : seoul', 'Name : kim', 'ph : 01012341234')\
)

print('{:-<70}'.format('-'))                #print('-'*70) is also okay

print(
    '{:<25} {:<14} {:>14} {:>14}'\
.format('Items', 'Unit', 'qty', 'price')\
)

print('{:-<70}'.format('-'))

print(
    '{:<25} {:<14,} {:>14} {:>14,}'\
.format(item1,unit1,qty1,price1)\
)

print(
    '{:<25} {:<14,} {:>14} {:>14,}'\
.format(item2,unit2,qty2,price2)\
)


print('{:-<70}'.format('-'))

print(
    '{:<10} {:>59,}'\
.format('total', price1 +price2)\
)

print('{:-<70}'.format('-'))

print(
    '{:<10} {:>59,}'\
.format('pay money', price1 + price2)\
)

print(
    '{:<10} {:>56,}'\
.format('receive money', recv)\
)

print(
    '{:<10} {:>59,}'\
.format('change', recv - (price1 + price2))\
)


print('{:-<70}'.format('-'))


