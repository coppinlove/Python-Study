def greet(name,msg="별일없지"):
    print("안녕 " + name + ", " + msg)

greet("홍길동")


#################

def print_star(n=1):
    print("n=", n)
    for i in range(n):
        print("**************")

print_star()
print()
print_star(3)
