#input - 키보드로 입력받기("출력문자")
#input - 문자로 기본적으로 입력받음
#input - 앞에 int를 붙여서 정수형으로 입력받음


#간단한 실습
n = "apple"
print("I like", n)
print("I like" + n)
print(str(3)+str(5))
#print에서 , 는 구분 & 공백 + 는 연결

print("결과는" + 20) #오류
#+는 같은 자료형끼리 가능하다

#input 실습
a, b = map(int, input("a와 b를 입력하세요: ").split())
sum = a+b
print(sum)