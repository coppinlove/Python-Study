Americano, CaffeLatte, Cappuccino = map(int, input("아메리카노, 카페라떼, 카푸치노의 판매수량을 입력하세요: ").split())
amer = 2000
caffe = 3000
capu = 3500

sale = Americano * amer + CaffeLatte * caffe + Cappuccino * capu
print("총 매출:", sale)