from gugu_module import *

r = 1
while r:
    num = int(input("\n숫자를 선택하세요(1: 세로 구구단   |||   2: 가로 구구단   |||   0: 종료): \n"))
    if num == 1:
        v_gugudan()

    elif num == 2:
        h_gugudan()

    elif num == 0:
        print("\n프로그램이 종료되었습니다.")
        r = 0
        
    else:
        print("\n잘못된 입력입니다.")
