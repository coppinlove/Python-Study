# 스코프(scope)
# 파이썬은 변수를 찾을 때 가까운 곳부터 찾는다.
# LEGB 규칙: Local, Enclosing, Global, Built-in
# Local -> 함수 내부 변수
# Enclosing -> 바깥 함수 변수
# Gloobal -> 함수 밖의 변수
# Built-in -> 파이썬이 기본적으로 제공하는 함수나 변수
a = '홍길동'  # 전역변수
b = 99 # 전역변수

def function1():
    a = '이순신'
    c = [1 ,2 ,3]
    
    def function2():
        d = (1, 2, 3)
        print('Local a =',a) # '이순신'
        print('Local b =',b) # 99
        print('Local c =',c) # [1, 2, 3]
        print('Local d =',d) # (1, 2, 3)
        
    
    function2()
    print('Enclosing a =',a) # '이순신'
    print('Enclosing b =',b) # 99
    print('Enclosing c =',c) # [1, 2, 3]
    #print('Enclosing d =',d) # error
function1()
print('Global a =',a) # '홍길동'
print('Global b =',b) # 99
#print('Global c =',c) # error
#print('Global d =',d) # error