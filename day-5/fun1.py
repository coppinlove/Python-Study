#함수
def add(a,b):
    return a+b 


n1 = int(input("첫번째 숫자 : "))
n2 = int(input("두번째 숫자 : "))
sum = add(n1, n2)
print(sum)
#sum(): 합계
#len(): 길이
# 숫자 리스트의 평균을 반환
# 1. 숫자 리스트의 합계를 구한다.
# 2. 리스트의 개수를 구한다.
# 3. 합계를 개수로 나눈다.
def avg(numbers):
    total = sum(numbers) #합계
    count = len(numbers) #개수
    return total / count #평균
numbers = [80, 90, 100, 50, 70]
aver_res = avg(numbers)
print(aver_res)



