#리스트
subway=["아이유","변우석","박지훈","유재석"]
print(subway)
subway.append("장원영")   #append는 리스트에 요소를 추가하는 함수
print(subway)
subway.insert(1,"카리나")    #insert는 리스트에서 원하는 위치에 요소를 추가하는 함수
print(subway) 
print(subway.index("박지훈"))    #index는 리스트에서 해당 요소가 몇 번째에 있는지 알려주는 함수
print(subway.pop(1))    #맨 뒤에 있는 요소를 꺼내는 함수
print(subway)

name=subway.pop(1)    #pop은 리스트에서 요소를 꺼내는 함수
print(name)

subway.remove("유재석")    #remove는 리스트에서 해당 요소를 제거하는 함수
print(subway)

subway.append("아이유")
print(subway) 

num_list=[3,4,2,5,1]
print(num_list)

num_list.sort()    #sort는 리스트의 요소를 정렬하는 함수
print(num_list)

num_list.reverse()    #reverse는 리스트의 요소를 역순으로 정렬하는 함수
print(num_list)

num_list.clear()    #clear는 리스트의 모든 요소를 제거하는 함수
print(num_list)

# 튜플
menu=("김밥","어묵")    #튜플은 리스트와 달리 요소를 변경할 수 없는 자료형
print(menu)    #튜플은 리스트와 달리 요소를 변경할 수 없기 때문에 인덱싱으로 요소를 가져올 수 있다.
#menu[1]="피자"
#print(menu)    #튜플은 리스트와 달리 요소를 변경할 수 없기 때문에 인덱싱으로 요소를 가져올 수 있다.

(name,age,addr)=("이순신",30,"안산")    #튜플은 리스트와 달리 요소를 변경할 수 없기 때문에 인덱싱으로 요소를 가져올 수 있다.
print(name,age,addr)

#딕셔너리
classroom={407:"개발자과정",402:"영상과정"}
print(classroom)
print(classroom[407])    #딕셔너리는 키와 값으로 이루어진 자료형이기 때문에 키를 이용해서 값을 가져올 수 있다.
#print(classroom[404])    #딕셔너리는 키와 값으로 이루어진 자료형이기 때문에 키를 이용해서 값을 가져올 수 있다.

print(classroom.get(407))    #get은 딕셔너리에서 키를 이용해서 값을 가져오는 함수
print(classroom.get(404))    #get은 딕셔너리에서 키를 이용해서 값을 가져오는 함수

print(classroom.keys())
print(classroom.values())
print(classroom.items())    

del classroom[402]
print(classroom)    #del은 딕셔너리에서 키와 값을 제거하는 함수
