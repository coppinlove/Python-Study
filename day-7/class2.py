
class Board:
    def __init__(self, title, writer): # 생성자 함수
        self.title = title
        self.writer = writer
        self.cnt = 0

    def cnt_up(self):
        self.cnt += 1

board1 = Board("파이썬 정석", "홍길동") # 객체 생성 + 생성자 호출
board2 = Board("자바의 정석", "이순신")

board1.cnt_up()
board1.cnt_up()
board2.cnt_up()
print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)