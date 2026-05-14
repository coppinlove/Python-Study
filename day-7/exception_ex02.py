
fruits = ["사과", "배", "오렌지"] # list 0 ~ 2

try:
    index = int(input("인덱스를 입력하세요 (0-2): "))
    if index < 0 or index >= len(fruits): # 인덱스 범위 체크
        raise IndexError # 예외 강제 발생

except IndexError: # 인덱스 범위 초과 예외 처리
    print("인덱스가 범위를 벗어났습니다.")

except ValueError: # 입력값이 정수가 아닌 경우 예외 처리
    print("유효한 숫자를 입력하세요.")

except Exception as e: # 그 외 나머지 예외인 경우: e 예외 저장
    print("에러메시지", e)

else: # 예외가 발생하지 않은 경우 실행
    print(f"선택한 과일: {fruits[index]}")  

finally: # 공통적 수행(무조건 수행)
    print("프로그램이 종료되었습니다.")