
# 부모 클래스 
class Passbook:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
        print(f"{money}원이 입금되었습니다. 현재 잔액: {self.balance}원")

    def withdraw(self, money):
        if money > self.balance:
            print("잔액 부족")
        else:
            self.balance -= money
            print(f"{money}원이 출금되었습니다. 현재 잔액: {self.balance}원")
    
    def showInfo(self):
        print(f"예금주: {self.owner}, 잔액: {self.balance}원")

# 자식 클래스
class MinusPassbook(Passbook): # 상속
    # withdraw() 자식이 재정의 (오버라이딩)
    def withdraw(self, money):
        if (self.balance - money) >= -1000000:
            self.balance -= money
            print(f"{money}원이 출금되었습니다. 현재 잔액: {self.balance}원")
        else:
            print("마이너스 한도 초과")

# 실행
account1 = Passbook("홍길동", 100000)
account1.showInfo()
account1.deposit(50000)
account1.withdraw(120000)
account1.withdraw(70000)

account2 = MinusPassbook("감철수", 100000)
account2.withdraw(120000)
account2.withdraw(900000)
account2.withdraw(100000)