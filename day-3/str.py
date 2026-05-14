# 문자열
s= "Hello python"
print(s[6]) #인덱싱
print(s[6:12]) #슬라이싱

jumin="080415-3252656"
print("성별:"+jumin[7])
print("월:"+jumin[2:4]) #2~3
print("일:"+jumin[4:6]) #4~5
print("뒷자리"+jumin[7:])

s1="나는 학생입니다"
s2="파이썬을 배웁니다"
s3="재미있습니다"
s4="""
나는 학생입니다

파이썬을 배웁니다
재미있습니다
"""

print(s4)


year="1981"
month="08"
day="28"
date=year+month+day
print(date)

date2= date.split("-")
print(date2)
print(type(date2))
print(date2[1])

