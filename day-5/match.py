# 사용자로부터 숫자 입력 받기

num1 = int(input("3의 배수 입력: "))
num2 = int(input("5의 배수 입력: "))

match num1%3, num2%5:
    case 0, 0:
        print("num1은 3의 배수 num2는 5의 배수")
    case 0, _:
        print("num1은 3의 배수 num2는 아무숫자")
    case _, 0:
        print("num2는 5의 배수 num1은 아무숫자")
    case _, _:
        print("둘다 오류")