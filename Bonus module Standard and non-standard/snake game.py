import pygame
import random

# инициализация Pygame
pygame.init()

# размеры игрового поля
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# размеры сегмента змейки и скорость перемещения
segment_size = 20
segment_speed = 1

clock = pygame.time.Clock()


# определение класса для каждого сегмента
class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([segment_size, segment_size])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Snake:
    def __init__(self):
        self.segments = []
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.score = 0
        self.game_over = False

    def add_segment(self):
        if len(self.segments) == 0:
            x = random.randint(1, (width - segment_size) // segment_size) * segment_size
            y = random.randint(1, (height - segment_size) // segment_size) * segment_size
        else:
            x = self.segments[-1].rect.x
            y = self.segments[-1].rect.y

        segment = Segment(x, y)
        self.segments.append(segment)

    def move(self):
        if self.direction == 'left':
            x = self.segments[0].rect.x - segment_size
            y = self.segments[0].rect.y
        elif self.direction == 'right':
            x = self.segments[0].rect.x + segment_size
            y = self.segments[0].rect.y
        elif self.direction == 'up':
            x = self.segments[0].rect.x
            y = self.segments[0].rect.y - segment_size
        elif self.direction == 'down':
            x = self.segments[0].rect.x
            y = self.segments[0].rect.y + segment_size

        segment = Segment(x, y)
        self.segments.insert(0, segment)

        # удаление последнего сегмента, если змейка не съела еду
        if self.segments[0].rect.colliderect(food.rect):
            food.respawn()
        else:
            self.segments.pop()

    def handle_collisions(self):
        if self.segments[0].rect.x < 0 or self.segments[0].rect.x >= width or self.segments[0].rect.y < 0 or \
                self.segments[0].rect.y >= height:
            self.game_over = True

        for segment in self.segments[1:]:
            if segment.rect.colliderect(self.segments[0].rect):
                self.game_over = True

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.direction != 'down':
            self.direction = 'up'
        elif keys[pygame.K_DOWN] and self.direction != 'up':
            self.direction = 'down'
        elif keys[pygame.K_LEFT] and self.direction != 'right':
            self.direction = 'left'
        elif keys[pygame.K_RIGHT] and self.direction != 'left':
            self.direction = 'right'

    def update_score(self):
        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Eugene production --Game Score: {self.score}", True, WHITE)
        screen.blit(score_text, (20, 20))

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, segment.rect)


# создание змеи
snake = Snake()
snake.add_segment()


# определение класса для еды
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([segment_size, segment_size])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def respawn(self):
        self.rect.x = random.randint(1, (width - segment_size) // segment_size) * segment_size
        self.rect.y = random.randint(1, (height - segment_size) // segment_size) * segment_size


# создание еды
food = Food()
food.respawn()

# главный игровой цикл
while not snake.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snake.game_over = True

    screen.fill(BLACK)
    snake.handle_input()
    snake.move()
    snake.handle_collisions()

    snake.draw()
    screen.blit(food.image, food.rect)
    snake.update_score()

    pygame.display.flip()
    clock.tick(10)

pygame.quit()