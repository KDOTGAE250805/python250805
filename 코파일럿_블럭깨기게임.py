import tkinter as tk
import random

WIDTH = 500
HEIGHT = 400
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
BALL_SIZE = 15
BRICK_ROWS = 5
BRICK_COLS = 8
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 20

class BrickBreaker:
    def __init__(self, root):
        self.root = root
        self.root.title('블럭깨기 게임')
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        self.paddle = self.canvas.create_rectangle(WIDTH//2-PADDLE_WIDTH//2, HEIGHT-30,
                                                  WIDTH//2+PADDLE_WIDTH//2, HEIGHT-30+PADDLE_HEIGHT,
                                                  fill='white')
        self.ball = self.canvas.create_oval(WIDTH//2-BALL_SIZE//2, HEIGHT//2-BALL_SIZE//2,
                                            WIDTH//2+BALL_SIZE//2, HEIGHT//2+BALL_SIZE//2,
                                            fill='yellow')
        self.ball_dx = random.choice([-3, 3])
        self.ball_dy = -3
        self.bricks = []
        self.create_bricks()
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)
        self.game_over = False
        self.score = 0
        self.score_text = self.canvas.create_text(50, 10, text=f'Score: {self.score}', fill='white', font=('Arial', 14))
        self.update()

    def create_bricks(self):
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x1 = col * BRICK_WIDTH
                y1 = row * BRICK_HEIGHT + 30
                x2 = x1 + BRICK_WIDTH - 2
                y2 = y1 + BRICK_HEIGHT - 2
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill='skyblue', outline='gray')
                self.bricks.append(brick)

    def move_left(self, event):
        if not self.game_over:
            self.canvas.move(self.paddle, -20, 0)
            self.check_paddle_bounds()

    def move_right(self, event):
        if not self.game_over:
            self.canvas.move(self.paddle, 20, 0)
            self.check_paddle_bounds()

    def check_paddle_bounds(self):
        x1, _, x2, _ = self.canvas.coords(self.paddle)
        if x1 < 0:
            self.canvas.move(self.paddle, -x1, 0)
        elif x2 > WIDTH:
            self.canvas.move(self.paddle, WIDTH-x2, 0)

    def update(self):
        if self.game_over:
            return
        self.move_ball()
        self.root.after(16, self.update)

    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)
        # 벽 충돌
        if bx1 <= 0 or bx2 >= WIDTH:
            self.ball_dx = -self.ball_dx
        if by1 <= 0:
            self.ball_dy = -self.ball_dy
        # 패들 충돌
        px1, py1, px2, py2 = self.canvas.coords(self.paddle)
        if by2 >= py1 and bx2 >= px1 and bx1 <= px2 and by2 <= py2:
            self.ball_dy = -abs(self.ball_dy)
        # 바닥 충돌
        if by2 >= HEIGHT:
            self.end_game('Game Over!')
        # 벽돌 충돌
        hit_brick = None
        for brick in self.bricks:
            bx, by, bx2, by2 = self.canvas.coords(brick)
            if bx1 < bx2 and bx2 > bx and by1 < by2 and by2 > by:
                hit_brick = brick
                break
        if hit_brick:
            self.canvas.delete(hit_brick)
            self.bricks.remove(hit_brick)
            self.ball_dy = -self.ball_dy
            self.score += 10
            self.canvas.itemconfig(self.score_text, text=f'Score: {self.score}')
            if not self.bricks:
                self.end_game('You Win!')

    def end_game(self, msg):
        self.game_over = True
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text=msg, fill='red', font=('Arial', 24))

if __name__ == '__main__':
    root = tk.Tk()
    game = BrickBreaker(root)
    root.mainloop()
