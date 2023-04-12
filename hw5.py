def read_single_gigit(x) :
    if x == 9 :
        return '구'
    elif x == 8 :
        return '팔'
    elif x == 7 :
        return '칠'
    elif x == 6 :
        return '육'
    elif x == 5 :
        return '오'
    elif x == 4 :
        return '사'
    elif x == 3 :
        return '삼'
    elif x == 2 :
        return '이'
    elif x == 1 :
        return '일'
    else :
        return '영'

def read_number(num) :
    if num<0 or num>999 :
        return '잘못된 입력'
    else :
        h = num // 100
        t = (num % 100) // 10
        o = (num % 100 % 10)
        k_h = read_single_gigit(h)
        k_t = read_single_gigit(t)
        k_o = read_single_gigit(o)
        s = k_h + k_t + k_o
        return s
num = int(input('세 자리 정수 입력:'))
print(read_number(num))
