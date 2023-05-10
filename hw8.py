def buy(shopping_bag):
    item = input("상품명? ")
    if item == "":
        return False
    quantity = int(input("수량은? "))
    shopping_bag[item] = quantity
    print(f'장바구니에 {item} {quantity}개가 담겼습니다.')
    print('')
    return True

def show(shopping_bag):
    print("장바구니 보기:", shopping_bag)
    print()

def find(shopping_bag):
    search_item = input("장바구니에서 확인하고자하는 상품은? ")
    if search_item in shopping_bag:
        print(f"{search_item}은(는) {shopping_bag[search_item]}개 담겨 있습니다.")
    else:
        print(f"{search_item}은(는) 장바구니에 없습니다.")

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
