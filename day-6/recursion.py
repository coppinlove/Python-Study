# 재귀 호출 (함수 내부에서 자기 자신을 호출)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

a = int(input("정수를 입력하세요: "))

res = factorial(a)
print(str(a) + "! =", res)




# 1부터 입력 받은 숫자까지 합을 구하는 프로그램 작성
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

num = int(input("정수를 입력하세요: "))

result = sum(num)

print("1부터", num, "까지의 합은", result, "입니다.")
