# 주민번호를 입력
# 1, 3 -> 남자 아니면 2, 4 -> 여자
jumin = input("주민번호를 입력하세요 : ")
num = jumin.split("-")[1]
if num[0] == "1" or num[0] == "3":
    print("남자입니다.")
elif num[0] == "2" or num[0] == "4":
    print("여자입니다.")

