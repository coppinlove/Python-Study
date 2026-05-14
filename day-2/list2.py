move_list = ["아바타", "왕사남", "살목지", "극한직업"]
print(move_list)

#메서드(insert, append, remove)
move_list.insert(1, "범죄도시") #삽입
print(move_list)

move_list.append("슈퍼맨") #추가
print(move_list)

move_list.remove("살목지") #값을 지정하여 삭제
print(move_list)

#del: 명령어
del move_list[2]
print(move_list)

x = 10
print(x)
del x
# print(x)

print(len(move_list)) #len: 길이

a = [1, 2, 3]
print(sum(a))

A = [90, 50, 80, 70, 55]

print(sum(A) / len(A))