name, price, amount = input("상품의 이름과 가격과 수량을 입력하세요: ").split()
price, amount = int(price), int(amount)
print("상품 이름:", name)
print("가격:", price)
print("수량:", amount)
print(name + "의 총 금액은", str(price * amount) + "원 입니다")
print(f"{name}의 총 금액은 {price * amount}원 입니다")
#print 안에서 f는 f-string이라고하며 포맷 문자열
# --> f" {변수 값} "
#숫자 -> 문자로 변환: str
#실수는 float만 있음 (8바이트)