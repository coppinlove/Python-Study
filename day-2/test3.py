Money = int(input("투입 금액을 입력하시오: "))
Price = int(input("물건 값을 입력하시오: "))

if Money < Price:
    print("투입 금액이 물건 값보다 적습니다.")
    exit()

change = Money - Price
change500 = change // 500
change100 = change500 // 100
print("거스름돈:", change)
print("500원 동전의 개수:", change500)
print("100원 동전의 개수:", change100)