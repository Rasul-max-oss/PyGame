import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600  # Размеры экрана
# Шарик
BALL_RADIUS = 15
# Ракетка
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100  # Размеры ракетки
PADDLE_SPEED = 10  # Скорость ракетки

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")

# Описание мяча
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.speed_x = 5
        self.speed_y = 5

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)  # Отрисовываем мяч

    def move(self):
        self.rect.x += self.speed_x  # Двигаем мяч по оси X
        self.rect.y += self.speed_y  # Двигаем мяч по оси Y

        # Столкновение с верхней и нижней границей экрана
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1  # Меняем направление по вертикали

# Описание ракетки
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)  # Отрисовываем ракетку

    def move(self, up, down):
        keys = pygame.key.get_pressed()  # Получаем состояние клавиш

        if keys[up] and self.rect.top > 0:  # Двигаем ракетку вверх
            self.rect.y -= self.speed
        if keys[down] and self.rect.bottom < HEIGHT:  # Двигаем ракетку вниз
            self.rect.y += self.speed

# Создаем объекты мяча и ракеток
ball = Ball()
paddle_left = Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2)
paddle_right = Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)

# Инициализация времени и счёта
clock = pygame.time.Clock()
score_left = 0
score_right = 0

# Шрифты для отображения счёта
font = pygame.font.SysFont("Arial", 36)

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие окна
            pygame.quit()
            sys.exit()

    # Движение мяча
    ball.move()

    # Управление ракетками
    paddle_left.move(pygame.K_w, pygame.K_s)  # Управление для левой ракетки (W и S)
    paddle_right.move(pygame.K_UP, pygame.K_DOWN)  # Управление для правой ракетки (стрелки вверх и вниз)

    # Столкновение мяча с ракетками
    if ball.rect.colliderect(paddle_left.rect) or ball.rect.colliderect(paddle_right.rect):
        ball.speed_x *= -1  # Меняем направление мяча по горизонтали

    # Проверка, не вышел ли мяч за пределы экрана
    if ball.rect.left <= 0:  # Мяч ушел за левую границу
        score_right += 1  # Очко правому игроку
        ball.rect.center = (WIDTH // 2, HEIGHT // 2)  # Центрируем мяч
    elif ball.rect.right >= WIDTH:  # Мяч ушел за правую границу
        score_left += 1  # Очко левому игроку
        ball.rect.center = (WIDTH // 2, HEIGHT // 2)  # Центрируем мяч

    # Отображаем все на экране
    screen.fill(BLACK)  # Очищаем экран
    ball.draw(screen)  # Рисуем мяч
    paddle_left.draw(screen)  # Рисуем левую ракетку
    paddle_right.draw(screen)  # Рисуем правую ракетку

    # Отображаем счёт
    score_text = font.render(f"{score_left}  -  {score_right}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))  # Отображаем счёт вверху

    pygame.display.flip()  # Обновляем экран

    clock.tick(60)  # Ограничиваем FPS (60 кадров в секунду)








