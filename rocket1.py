import pygame
import random

pygame.init()

# Определение параметров экрана
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flying Rocket")

# Загрузка изображений
background = pygame.image.load("img/space_background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Используйте PNG или другой совместимый формат для ракеты
rocket_img = pygame.image.load("img/rocket.svg")  # измените на подходящее изображение
rocket_img = pygame.transform.scale(rocket_img, (50, 50))  # размер

# Астероиды или метеориты
meteor_img = pygame.image.load("img/asteroid.png")
meteor_img = pygame.transform.scale(meteor_img, (50, 50))

# Функция отрисовки ракеты на экране
def draw_rocket(x, y):
    screen.blit(rocket_img, (x, y))

# Функция отрисовки метеоритов
def draw_meteorite(x, y):
    screen.blit(meteor_img, (x, y))



# Функция для отображения текста
def draw_text(text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Функция столкновения
def collision_check(rocket_x, rocket_y, meteor_x, meteor_y):
    if rocket_x < meteor_x + 50 and rocket_x + 50 > meteor_x and rocket_y < meteor_y + 50 and rocket_y + 50 > meteor_y:
        return True
    return False

# Создание списка метеоритов
meteorites = []
meteor_speed = 0.5
last_meteor_time = 0
meteor_interval = 500  # Интервал в миллисекундах (2 секунды)

# Управление ракетой
rocket_x = screen_width // 2  # ширину делим на два тем самым ставим ракету по середине
rocket_y = screen_height - 70  # аналогично
rocket_speed = 2  # скорость ракеты пока будет равна 2

# Очки
score = 0
# Шрифты
font = pygame.font.SysFont("arial", 30)
game_over_font = pygame.font.SysFont("arial", 50)
orange = (255, 215, 0) # Цвет


# Основной цикл
running = True
while running:
    # Обновление фона
    screen.blit(background, (0, 0))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление ракетой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rocket_x > 0:
        rocket_x -= rocket_speed
    if keys[pygame.K_RIGHT] and rocket_x < screen_width - 50:
        rocket_x += rocket_speed

    # Отрисовка ракеты
    draw_rocket(rocket_x, rocket_y)

    # Генерация нового метеорита
    current_time = pygame.time.get_ticks()
    if current_time - last_meteor_time > meteor_interval:
        meteor_x = random.randint(0, screen_width - 50)
        meteor_y = -50
        meteorites.append([meteor_x, meteor_y])
        last_meteor_time = current_time

    # Отрисовка и обновление позиций метеоритов
    for meteor in meteorites:
        meteor[1] += meteor_speed  # падаем вниз
        draw_meteorite(meteor[0], meteor[1])

        # Проверка на столкновение
        if collision_check(rocket_x, rocket_y, meteor[0], meteor[1]):
            running = False  # Завершаем игру, если произошло столкновение

        # Удаляем метеориты, которые вышли за экран
        if meteor[1] > screen_height:
            meteorites.remove(meteor)
            score+=1
        #Отображаем текст с очками
        #font.render() позволяет показать текст на экране
        label = font.render(f"Score: {score}", True, orange)
        screen.blit(label, (10,10))



    # Обновление экрана
    pygame.display.update()


