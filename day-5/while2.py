# 숫자 입력 -> 출력 반복, 0 입력 시 종료
while True:  
    num = int(input("숫자를 입력하세요 : "))
    if num == 0:
        print("종료합니다.")
        break
    print("입력한 숫자 :", num)

    menu=["쫄면","김밥","냉면","오뎅"]
    b=input("메뉴를 입력하세요 : ")
    while b not in menu:
        print("없는 메뉴입니다. 다시 입력하세요.")
        b=input("메뉴를 입력하세요 : ")