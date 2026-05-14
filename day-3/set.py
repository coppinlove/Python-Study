# set(집합)
# 순서가 없음, 중복 안됨
# {} , set([])

my_set = {"홍길동","김길동","장길동"}
print(my_set)

football = {"홍길동","김길동","장길동"}
#baseball = {"홍길동","김길동","장길동"}
baseball=set(["홍길동","오길동","김광현"])
#교집합
print(football & baseball)
print(football.intersection(baseball))

#합집합
print(football | baseball)
print(football.union(baseball))

#차집합
print(football - baseball)
print(football.difference(baseball))

#추가
football.add("박길동")
print(football)

#제거
baseball.remove("오길동")
print(baseball)
