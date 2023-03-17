def exhange(price) :
    price_500 = price // 500
    price_100 = (price % 500) // 100
    price_50 = price % 500 % 100 //50
    price_10 = price % 500 % 100 % 50 // 10
    print('500원:', price_500, '개')
    print('100원:', price_100, '개')
    print('50원:', price_50, '개')
    print('10원:', price_10, '개')
def get_integer(prompt) :
    rp = int(input(prompt))
    return rp
r_price = get_integer('동전으로 교환하고자 하는 금액은?')
exhange(r_price)