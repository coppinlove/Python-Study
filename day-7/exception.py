
try: # 수행문장 안에 예외 발생하면
    num = int(input("숫자를 입력하세요: "))
    result = 10 / num
    print(f"10을 {num}으로 나눈 결과: {result}")

except ValueError: # except: 예외 발생 시 처리(값 오류)
    print("유효한 숫자를 입력하세요.")

except ZeroDivisionError: # except: 예외 발생 시 처리(0으로 나눌 때)
    print("0으로 나눌 수 없습니다.")

except Exception as e: # 그 외 나머지 예외인 경우: e 예외 저장
    print("에러메시지", e)

else: # 예외가 발생하지 않은 경우 실행
    print("결과:", result)

finally: # 공통적 수행(무조건 수행)
    print("프로그램이 종료되었습니다.")