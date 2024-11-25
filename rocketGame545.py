import  pygame
import random

pygame.init()

# Определение параметров экрана
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flying Rocket")

# Загрузка изображений
back =  pygame.image.load("img/space_background.jpg")#это фон
back = pygame.transform.scale(back, (screen_width, screen_height))#изменили размер

#Ракета
# Используйте PNG или другой совместимый формат для ракеты
rocket_img = pygame.image.load("img/rocket.svg")  # измените на подходящее изображение
rocket_img = pygame.transform.scale(rocket_img, (50, 50))#размер

#Астероиды или метеориты
meteor_img = pygame.image.load("img/asteroid.png")
meteor_img = pygame.transform.scale(meteor_img, (50, 50))

# Функция отрисовки ракеты на экране
def draw_rocket(x, y):
    screen.blit(rocket_img, (x, y))

#Ваша задача создать такую же функцию но про метеорит
#назвать строго draw_meteor

def draw_meteorite(x, y):
    screen.blit(meteor_img, (x, y))


#Функция столкновения
# Функция для проверки столкновения объектов
def collision_check(rocket_x, rocket_y, meteor_x, meteor_y):
    if rocket_x < meteor_x + 50 and rocket_x + 50 > meteor_x and rocket_y < meteor_y + 50 and rocket_y + 50 > meteor_y:
        return  True
    return  False




# Управление ракетой
rocket_x = screen_width // 2 #ширину делим на два тем самым ставим ракету по середине
rocket_y = screen_height - 70 #аналогично
rocket_speed = 2 #скорость ракеты пока будет равна 2

#Создание списка метеоритов
meteorites = []
meteor_speed = 0.5
last_meteor_time = 0
meteor_interval = 500

#очки
score  = 0
# Шрифты
font = pygame.font.SysFont("arial", 30)
game_over_font = pygame.font.SysFont("arial", 50)
orange = (255, 165, 0)

def draw_text(text, font, color,x,y):
    label = font.render(text,True,color)
    screen.blit(label, (x,y))





# Основной цикл
running = True
while running:
    # Обновление фона
    screen.blit(back, (0, 0))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Управление ракетой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rocket_x > 0:
        rocket_x-=rocket_speed
    if keys[pygame.K_RIGHT] and  rocket_x < screen_width - 50:
        rocket_x += rocket_speed

    # Отрисовка ракеты
    draw_rocket(rocket_x, rocket_y)

    current_time = pygame.time.get_ticks()#получаем текущее время

    #Генерация метеоритов
    if current_time - last_meteor_time > meteor_interval:
        meteor_x = random.randint(0, screen_width-50)
        meteor_y = -50
        meteorites.append([meteor_x,meteor_y])
        last_meteor_time = current_time

    #отображение
    for meteor in meteorites:#проходимся по списку метеоритов
        meteor[1] += meteor_speed  # падаём вниз
        draw_meteorite(meteor[0], meteor[1])  # отображаем

        #Проверка на столкновенме
        if collision_check(rocket_x,rocket_y,meteor[0],meteor[1]):
            running = False
        #удаляем метеориты, которые вышли за экран
        if meteor[1] > screen_height:
            meteorites.remove(meteor)
            score+=1
            print(score)
    #вызываем функция отображение текста
    draw_text(f'Score: {score}',font,orange,10,10)




    # Обновление экрана
    pygame.display.update()

    # Завершение игры, если произошло столкновение
    if not running:
        screen.fill( (0, 0, 0) )#это черный цвет
        draw_text("Game Over", game_over_font, orange,screen_width//2 -150, screen_height//2 - 50)
        draw_text(f"Final Score: {score}", game_over_font, orange, screen_width // 2 - 150, screen_height // 2  + 10)
        pygame.display.update()
        # Задержка перед закрытием игры
        pygame.time.delay(2000)

        #Для перезапуска игры
        running = True
        score = 0  # Обнуляем счётчик очков
        meteorites.clear() #очищаем список метеоритов
        rocket_x = screen_width // 2  # Возвращаем ракету в центр
        rocket_y = screen_height - 70  # Начальная позиция ракеты




