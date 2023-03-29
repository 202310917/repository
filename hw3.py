def get_fixed_price(f_price) :
    o_price = f_price * 1 / ( 1 - (discount / 100))
    return o_price
discount =  int(input('할인율은?'))
f1_price = int(input('A 상품의 할인된 가격은?'))
f2_price = int(input('B 상품의 할인된 가격은?'))
o1_price = int(get_fixed_price(f1_price))
o2_price = int(get_fixed_price(f2_price))
print('A 상품의 정가는', o1_price, '원')
print('A 상품의 정가는', o2_price, '원')
