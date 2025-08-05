import pygame
import random

# 게임 설정
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLUMNS = WIDTH // BLOCK_SIZE
ROWS = HEIGHT // BLOCK_SIZE

# 색상 정의
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0),    # Z
]

# 테트로미노 도형
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0],
     [1, 1, 1]],     # J
    [[0, 0, 1],
     [1, 1, 1]],     # L
    [[1, 1],
     [1, 1]],        # O
    [[0, 1, 1],
     [1, 1, 0]],     # S
    [[0, 1, 0],
     [1, 1, 1]],     # T
    [[1, 1, 0],
     [0, 1, 1]],     # Z
]

class Tetromino:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_board():
    return [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

def check_collision(board, tetromino, dx=0, dy=0, rotated_shape=None):
    shape = rotated_shape if rotated_shape else tetromino.shape
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                nx = tetromino.x + x + dx
                ny = tetromino.y + y + dy
                if nx < 0 or nx >= COLUMNS or ny >= ROWS:
                    return True
                if ny >= 0 and board[ny][nx]:
                    return True
    return False

def merge_board(board, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                ny = tetromino.y + y
                nx = tetromino.x + x
                if 0 <= ny < ROWS and 0 <= nx < COLUMNS:
                    board[ny][nx] = tetromino.color

def clear_lines(board):
    cleared = 0
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    cleared = ROWS - len(new_board)
    for _ in range(cleared):
        new_board.insert(0, [0 for _ in range(COLUMNS)])
    return new_board, cleared

def draw_board(screen, board):
    for y in range(ROWS):
        for x in range(COLUMNS):
            color = board[y][x] if board[y][x] else GRAY
            pygame.draw.rect(screen, color, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
            pygame.draw.rect(screen, BLACK, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_tetromino(screen, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen,
                    tetromino.color,
                    ((tetromino.x + x)*BLOCK_SIZE, (tetromino.y + y)*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    0
                )
                pygame.draw.rect(
                    screen,
                    BLACK,
                    ((tetromino.x + x)*BLOCK_SIZE, (tetromino.y + y)*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    1
                )

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("테트리스 게임")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24)

    board = create_board()
    score = 0
    running = True

    def new_tetromino():
        idx = random.randint(0, len(SHAPES)-1)
        shape = [row[:] for row in SHAPES[idx]]
        color = COLORS[idx]
        return Tetromino(COLUMNS//2 - len(shape[0])//2, 0, shape, color)

    tetromino = new_tetromino()
    fall_time = 0
    fall_speed = 500  # ms

    while running:
        dt = clock.tick(60)
        fall_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(board, tetromino, dx=-1):
                        tetromino.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(board, tetromino, dx=1):
                        tetromino.x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(board, tetromino, dy=1):
                        tetromino.y += 1
                elif event.key == pygame.K_UP:
                    rotated = [list(row) for row in zip(*tetromino.shape[::-1])]
                    if not check_collision(board, tetromino, rotated_shape=rotated):
                        tetromino.shape = rotated

        if fall_time > fall_speed:
            if not check_collision(board, tetromino, dy=1):
                tetromino.y += 1
            else:
                merge_board(board, tetromino)
                board, cleared = clear_lines(board)
                score += cleared * 100
                tetromino = new_tetromino()
                if check_collision(board, tetromino):
                    running = False  # 게임 오버
            fall_time = 0

        screen.fill(BLACK)
        draw_board(screen, board)
        draw_tetromino(screen, tetromino)
        score_text = font.render(f"점수: {score}", True, (255,255,255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

    pygame.quit()
    print("게임 오버! 최종 점수:", score)

if __name__ == "__main__":
    main()