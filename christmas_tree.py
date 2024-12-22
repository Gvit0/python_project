import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600   # Размер
FPS = 60                   # Кадры

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ёлочка с снегом")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Настройки снега
SNOW_COUNT = 100            # Количество снежинок
MIN_SNOW_SPEED = 0.7        # Минимальная скорость падения снега
MAX_SNOW_SPEED = 1.2        # Максимальная скорость падения снега
MOVE_SNOW = True            # Включить движение снега влево и вправо
MOVE_DISTANCE = 1           # Максимальная дальность движения влево и вправо

# Настройки гирлянды
LIGHTS_ON = True            # Включить/Выключить
LIGHTS_ON_DURATION = 15000  # Время включения гирлянды (15 секунд)
FADE_DURATION = 10000       # Время затухания/появления (10 секунд)
NUM_LIGHTS = 40             # Количество огоньков гирлянды

#Выбрать рандомную точку в треугольнике
def random_point_in_triangle(p1, p2, p3, r=0):
    s, t = sorted([random.random(), random.random()])
    return (s * p1[0] + (t-s) * p2[0] + (1-t) * p3[0] + r,
            s * p1[1] + (t-s) * p2[1] + (1-t) * p3[1] + r)



#Выбрать рандомный треугольник и точку в нём
def random_point_in_triangles(x, y):
    triangle = random.choice([
        [(x, y), (x - 50, y + 100), (x + 50, y + 100)],
        [(x, y - 50), (x - 40, y + 50), (x + 40, y + 50)],
        [(x, y - 100), (x - 30, y - 20), (x + 30, y - 20)]
    ])
    return random_point_in_triangle(*triangle,r=5)

# Класс для снежинок
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-20, HEIGHT)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(MIN_SNOW_SPEED, MAX_SNOW_SPEED)  # Случайная скорость падения

    def fall(self):
        self.y += self.speed
        if MOVE_SNOW:
            # Двигаем снежинку влево или вправо
            self.x += random.randint(-MOVE_DISTANCE, MOVE_DISTANCE)
            # Ограничиваем движение снежинок в пределах экрана
            self.x = max(0, min(WIDTH, self.x))
        
        if self.y > HEIGHT:
            self.y = random.randint(-20, 0)
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

# Функция для рисования ёлочки
def draw_tree(x, y):
    # Рисуем ёлочку
    pygame.draw.rect(screen, BROWN, (x - 15, y + 100, 30, 20))  # Рисуем пень
    pygame.draw.polygon(screen, GREEN, [(x, y), (x - 50, y + 100), (x + 50, y + 100)])
    pygame.draw.polygon(screen, GREEN, [(x, y - 50), (x - 40, y + 50), (x + 40, y + 50)])
    pygame.draw.polygon(screen, GREEN, [(x, y - 100), (x - 30, y - 20), (x + 30, y - 20)])
#класс гирлянды
class Light:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice([RED, YELLOW, BLUE])
        self.alpha = 0 
        self.fade_in = True
        self.fade_timer = 0
        self.on_timer = 0

    def update(self):
        if self.fade_in:
            self.alpha += 1
            if self.alpha >= 255:
                self.fade_in = False
                self.on_timer = pygame.time.get_ticks()
        else:
            self.fade_timer = pygame.time.get_ticks() - self.on_timer
            if self.fade_timer >= FADE_DURATION:
                self.alpha -= 1
                if self.alpha <= 0:
                    self.fade_in = True
                    self.reset()  # Сбрасываем позицию лампочки

    def draw(self):
        light_surface = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(light_surface, (*self.color, self.alpha), (5, 5), 5)
        screen.blit(light_surface, (self.x, self.y))

    def reset(self):
        self.x, self.y = random_point_in_triangles(WIDTH // 2, HEIGHT // 2)
        self.on_timer = pygame.time.get_ticks()


# Функция для рисования гирлянды
def draw_lights(x, y):
    for _ in range(NUM_LIGHTS):
        print(random_point_in_triangles(x,y))
        light = Light(*random_point_in_triangles(x,y))
        light.update()
        light.draw()

# Основной цикл
def main():
    clock = pygame.time.Clock()
    x=WIDTH//2; y=HEIGHT//2
    snowflakes = [Snowflake() for _ in range(SNOW_COUNT)]
    running = True

    # Создаем список огоньков гирлянды
    lights = [Light(*random_point_in_triangles(x,y)) for _ in range(NUM_LIGHTS)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Очистка экрана

        # Рисуем ёлочку
        draw_tree(WIDTH // 2, HEIGHT // 2)

        # Рисуем гирлянду
        if LIGHTS_ON == True:
            for light in lights:
                light.update()
                light.draw()

        # Обновляем и рисуем снежинки
        for snowflake in snowflakes:
            snowflake.fall()
            snowflake.draw()

        pygame.display.flip()  # Обновляем экран
        clock.tick(60)  # Ограничение FPS

    pygame.quit()

if __name__ == "__main__":
    main()  # Запуск основного цикла
'''
#python + #pygame  
Ёлочка🎄 с снегом❄️ и гирляндой💡.
Есть настройки: снега и гирлянды
'''