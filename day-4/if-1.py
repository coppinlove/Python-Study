# Str = input('영어 1글자 입력하세요 : ')

# if Str.isupper():   # 대문자면
#     print(Str.lower())
# else:               # 소문자면
#     print(Str.upper())


    #점수 구간에 해당하는 학점이 아래와 같이 정의 되어 있다.
    #사용자로부터 score를 입력받아 합력을 출력해라.
score = int(input("학점을 입력하세요 : "))
if 81 <= score <= 100:
    print("A")
elif 61 <= score <= 80:
    print("B")
elif 41 <= score <= 60:
    print("C")
elif 21 <= score <=40:
    print("D")
else:
    print("E")



    # 사용자로부터 세 개의 숫자를 입력 받은 후
# 가장 큰 숫자를 출력하라
num1 = int(input("첫 번째 숫자를 입력하세요. : "))
num2 = int(input("두 번째 숫자를 입력하세요. : "))
num3 = int(input("세 번째 숫자를 입력하세요. : "))
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2) 
else:    
    print(num3)  