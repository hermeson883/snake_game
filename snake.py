import pygame
import random

pygame.init()
resolution = (500,500)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
preto = (0,0,0)
screen.fill(preto)

pygame.display.update() #ATUALIZANDO O PYGAME

class Snake:
    def __init__(self):
        self.color = [135, 206, 235]
        self.size = (10, 10)
        self.velocity = 5
        self.texture = pygame.Surface(self.size)
        self.texture.fill(self.color)

        self.body = [(250, 250)]
        self.direction = "right"
        self.pontos = 0

    def blit(self, screen):
        for position in self.body:
            screen.blit(self.texture, position)

    def crawl(self):
        head = self.body[0]
        x = head[0]
        y = head[1]

        if self.direction == "right":
            self.body.insert(0, (x + self.velocity, y))

        elif self.direction == "left":
            self.body.insert(0, (x - self.velocity, y))

        elif self.direction == "up":
            self.body.insert(0, (x, y-self.velocity))

        elif self.direction == "bottom":
            self.body.insert(0, (x, y+self.velocity))

        self.body.pop()
    def up(self):
        if self.direction != "bottom":
            self.direction = "up"

    def left(self):
        if self.direction != "right":
            self.direction = "left"

    def right(self):
        if self.direction != "left":
            self.direction = "right"

    def bottom(self):
        if self.direction != "up":
            self.direction = "bottom"

    def colision(self, fruit):
        return self.body[0] == fruit.position

    def eat(self):
        self.body.append((0,0))
        self.pontos+=1
        pygame.display.set_caption(f'Snake Game | Pontos {self.pontos}')

    def wall_colision(self):
        head = self.body[0]
        tail = self.body[1:]
        x = head[0]
        y = head[1]
        return x < 0 or y < 0 or x > 490 or y > 490 or head in tail

    def ouroboros(self):
        return self.body[0] == self.body[1:]


class Fruit:
    color=(255,0,0)
    size = (10, 10)
    velocity = 10

    def __init__(self, snake):
        self.texture = pygame.Surface(self.size)
        self.texture.fill(self.color)

        self.position = Fruit.check_position(snake)

    @staticmethod
    def check_position(snake):
        x = random.randint(0,48) * 10
        y = random.randint(0,48) * 10

        if (x,y) in snake.body:
            Fruit.check_position(snake)
        else:
            return x,y


    def blit(self, screen):
        screen.blit(self.texture, self.position)


#Start game
if __name__ == "__main__":
    snake = Snake()
    fruit = Fruit(snake)
    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.up()
                    break
                elif event.key == pygame.K_LEFT:
                    snake.left()
                    break
                elif event.key == pygame.K_RIGHT:
                    snake.right()
                    break
                elif event.key == pygame.K_DOWN:
                    snake.bottom()
                    break

        snake.crawl()

        if snake.colision(fruit):
            snake.eat()
            fruit = Fruit(snake)

        if snake.wall_colision():
            snake = Snake()
            fruit = Fruit(snake)

        screen.fill(preto)
        fruit.blit(screen)
        snake.blit(screen)
        pygame.display.update()
