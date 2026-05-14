# a="봄"
# b="여름"
# print(a,b, sep="과",end=" 끝 ")
# sep: 변수사이에 들어가는 것을 나타냄
# end: 줄은 바꾸지 않고 옆으로 표시(공백도 가능)

# for i in range(1,100,2) 1~99 2씩증가
# 구구단에서 원하는 단을 입력받아서 출력
dan= int(input("원하는 단은"))
for i in range(1,10): #1~9
    print(dan,"*",i,"=", dan*i)

for  i in  range(2,10) :#2-9단
    print(  i, "단")
    for  j in  range(1,10): #1-9 수
        print( i,"*",j,"=", i*j,end="") 
    print()

import time
print()
for k in range(10,0,-1):#10~1
    print(k)
    time.sleep(1) # 1초동안 일시정지
print("발사!!")