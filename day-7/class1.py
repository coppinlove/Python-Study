# 클래스

class Board:
    def set_data(self, title, writer): # 책 제목, 저자 저장
        self.title = title # 오른쪽 title은 호출헐 때 받아온 매개변수 값
                           # 왼쪽 title은 객체(붕어빵)의 맴버변수
                           # 내 자신(객체)의미: self
        self.writer = writer
        self.cnt = 0
    
    def cnt_up(self): # 조회수 구하는 함수
        self.cnt += 1

# 게시판 객체 생성
# Board board1 = new Board() # 자바에서 객체 생성하는 방법
board1 = Board() # 파이썬에서 객체 생성하는 방법
board2 = Board()

board1.set_data("파이썬 정석", "홍길동")
board2.set_data("자바의 정석", "이순신")

board1.cnt_up()
board1.cnt_up()
board2.cnt_up()
print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)

board3 = Board()
# board3.cnt_up() # cnt_up() 함수를 호출하기 전에 set_data() 함수를 먼저 호출해서 cnt 변수를 초기화 해줘야 한다.
board3.set_data("C++의 정석", "김유신")
board3.cnt_up()
print(board3.title, board3.writer, board3.cnt)