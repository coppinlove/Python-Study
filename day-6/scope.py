def calc(r1):
    result = 3.14 * r1 ** 2 # r1: 반지름
    return result

r = float(input("반지름을 입력하세요: "))
area = calc(r)
print(f"반지름이 {r}인 원의 넓이는 {area}입니다.")
# print(result)  :result는 지역변수 (함수 종료되면 소멸) -> 에러 발생


##############################################################################


def calc2(r2):
    global a # a는 전역변수
    a = 3.14 * r2 ** 2 # r2: 반지름
    return a

a = 0 # a는 전역변수 (프로그램이 종료될 때까지 존재)
rr = float(input("반지름을 입력하세요: "))
area2 = calc2(rr)
calc2(rr)
print(a)
