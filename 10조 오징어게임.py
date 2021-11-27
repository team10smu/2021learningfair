import random
from tkinter import *
from tkinter import messagebox
import turtle as t
import time
def game1():
    t.bgcolor("pink")
    t.ht()
    t.up()
    t.write("숫자 기억하기 게임을 시작합니다.", False, "center", ("맑은 고딕", 20))
    time.sleep(3)
    t.clear()

    num = ""
    for x in range(3):
        rand_num = random.randint(1, 50)
        t.write(rand_num, False, "center", ("맑은 고딕", 50))
        num += str(rand_num)
        num += " "
        time.sleep(1)
        t.clear()

    user_input = t.textinput("숫자 기억 게임", "기억한 숫자를 입력하세요")

    if user_input == num.strip():
        t.write("정답입니다.", False, "center", ("맑은 고딕", 30))
        abc()
    else:
        t.write("오답입니다.", False, "center", ("맑은 고딕", 30))
        t.goto(0, -50)
        t.write(f"정답은 {num}입니다.", False, "center", ("맑은 고딕", 30))
        t.goto(0, -100)
        t.write(f"입력하신 수는 {user_input}입니다.", False, "center", ("", 30))
        abc()

def game2():
    class Player():
        def __init__(self, canvas, x, y):
            self.canvas = canvas
            self.id = canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="red")
            self.x, self.y = x, y
            self.nx, self.ny = x, y

        def move(self, direction):
            # 키보드에서 누른 키에 따라서 움직임
            if direction == 'w':
                self.nx, self.ny = self.x, self.y - 1
            elif direction == 'a':
                self.nx, self.ny = self.x - 1, self.y
            elif direction == 's':
                self.nx, self.ny = self.x, self.y + 1
            elif direction == 'd':
                self.nx, self.ny = self.x + 1, self.y

            # 이동한 곳이 벽이 아닐 경우 이동시키며 x, y 갱신
            if not self.is_collide():
                self.canvas.move(self.id, (self.nx - self.x) * 30, (self.ny - self.y) * 30)
                self.x, self.y = self.nx, self.ny

            # 골인 지점에 도달할 경우
            if map[self.y][self.x] == 3:
                messagebox.showinfo(title="성공", message="미로 찾기에 성공하셨습니다")
                abc()

        # 이동한 곳이 벽인지 아닌지 판별
        def is_collide(self):
            if map[self.ny][self.nx] == 1:
                return True
            else:
                return False

    # 키리스너 이벤트
    def keyEvent(event):
        player.move(repr(event.char).strip("'"))

    root = Tk()
    root.title("미로 찾기 게임")
    root.resizable(False, False)

    # 창 너비, 높이, 위치 설정
    width, height = 540, 540
    x, y = (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    # canvas를 추가하고 키이벤트를 부착
    canvas = Canvas(root, width=width, height=height, bg="white")
    canvas.bind("<Key>", keyEvent)
    canvas.focus_set()
    canvas.pack()

    # 1 : 벽, 2 : 플레이어 시작 지점, 3 : 골인 지점
    map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 3, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # canvas에 맵을 그림
    for y in range(len(map[0])):
        for x in range(len(map[y])):
            if map[y][x] == 1:
                canvas.create_rectangle(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="black")
            elif map[y][x] == 2:
                player = Player(canvas, x, y)
            elif map[y][x] == 3:
                canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="blue")

    root.mainloop()

def game3():
    def turn_left():
        player.left(30)
    def turn_right():
        player.right(30)
    def rand_pos():
        x_cor = random.randint(-350, 350)
        y_cor = random.randint(-350, 350)
        return x_cor, y_cor
    # 환경 설정
    t.setup(800, 800)
    t.bgcolor("skyblue")
    t.up()
    t.ht()
    # 변수
    player_speed = 5
    score = 0
    game_over = False
    # 점수 표시
    t.goto(0, 350)
    t.write(f"score : {score}", False, "center", ("", 20))
    # 플레이어
    player = t.Turtle()
    player.shape("turtle")
    player.shapesize(2)
    player.up()
    player.color("lavender")
    player.speed(0)
    # 먹이
    food = t.Turtle()
    food.ht()
    food.shape("triangle")
    food.up()
    food.color("darkgreen")
    food.speed(0)
    food.setheading(90)
    food.goto(rand_pos())
    food.st()
    # 독초
    p_herbs = t.Turtle()
    p_herbs.ht()
    p_herbs.shape("triangle")
    p_herbs.up()
    p_herbs.color("red")
    p_herbs.speed(0)
    p_herbs.setheading(90)
    p_herbs.goto(rand_pos())
    p_herbs.st()
    # 키 이벤트
    t.onkeypress(turn_left, "Left")
    t.onkeypress(turn_right, "Right")
    t.listen()
    while not game_over:
        player.forward(player_speed)

        if player.xcor() > 360 or player.xcor() < -360 or player.ycor() > 360 or player.ycor() < -360:
            player.right(180)

        if player.distance(food) < 20:
            food.goto(rand_pos())  # 푸드 먹으면 새로 랜덤으로 생기기
            p_herbs.goto(rand_pos())
            player_speed += 1  # 음식 먹으면 점점 빨라지기
            score += 1
            t.clear()
            t.write(f"score : {score}", False, "center", ("", 20))
            if score == 3:
                game_over = True
                abc()

        if player.distance(p_herbs) < 20:
            game_over = True
            abc()
    t.goto(0, 0)
    t.write(" GAME OVER ", False, "center", ("", 50))

def game4():
    count = 5
    score = 3

    totalscore = 0

    print('구슬이 홀수개인지 짝수개인지 맞춰보세요. 기회는 5번~!~!')
    for i in range(0, count):
        marble = random.randint(1, 10)
        answer = input('짝수는 0 홀수는 1을 입력해주세요 : ')

        if marble % 2 == 0:
            if answer == '0':
                print('정답입니다')
                totalscore = totalscore + 1
            else:
                print('오답입니다')
        else:
            if answer == '1':
                print('정답입니다')
                totalscore = totalscore + 1
            else:
                print('오답입니다')

        count = count - 1
        print('남은 횟수 : {}    현재 점수 : {}'.format(count, totalscore))

    if totalscore >= score:
        print('승리!!! YOU WIN!!!')
    else:
        print('패배... YOU LOSE...')
    abc()

def abc():
    print("-----------게임 선택-----------")
    print("1. 숫자기억하기게임")
    print("2. 미로게임")
    print("3. 지렁이게임")
    print("4. 홀짝게임")
    print("5. 게임종료")
    while True:
        choose = int(input("하고싶은 게임을 선택해주세요\n"))
        if choose == 1:
            game1()
        elif choose == 2:
            game2()
        elif choose == 3:
            game3()
        elif choose == 4:
            game4()
        elif choose == 5:
            print("게임을 종료합니다")
            quit()
        else:
            print("다시 선택해주세요")
abc()