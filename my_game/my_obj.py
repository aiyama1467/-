from my_game import vector, manager
import math


class Player:
    def __init__(self, size):
        self.pos = vector.Point2D(0, size.y * (5 / 6))
        self.x_speed = 1
        self.max_x = size.x
        self.size = vector.Point2D(100, 10)

    def draw(self, surface, image):
        surface.blit(image, (self.pos.x, self.pos.y))

    def move_left(self):
        if self.pos.x > 0:
            self.pos.x -= 10

    def move_right(self):
        if self.pos.x + self.size.x < self.max_x:
            self.pos.x += 10


class Block:
    def __init__(self, x, y):
        self.is_Exist = True
        self.size = vector.Point2D(x=40, y=20)
        self.pos = vector.Point2D(x * self.size.x, y * self.size.y)

    def draw(self, screen, image):
        if self.is_Exist:
            screen.blit(image, (self.pos.x, self.pos.y))


class Blocks:
    def __init__(self):
        self.num_of_block = (10, 8)
        self.blocks = [[Block(i, j) for j in range(self.num_of_block[1])] for i in range(self.num_of_block[0])]

    def draw(self, screen, image):
        for i in range(self.num_of_block[0]):
            for j in range(self.num_of_block[1]):
                self.blocks[i][j].draw(screen, image)


class Ball:
    def __init__(self, w_size):
        self.size = vector.Point2D(5, 5)
        self.pos = vector.Point2D(0, (w_size.y * 5/6 - 1) - self.size.y)
        self.direction = vector.Point2D(1 / math.sqrt(2), -1 / math.sqrt(2))
        self.speed = 5
        self.collision_manager = manager.CollisionManager()

    def draw(self, screen, image):
        screen.blit(image, (self.pos.x, self.pos.y))

    def move(self):
        self.pos.x = self.pos.x + (self.speed * self.direction.x)
        self.pos.y = self.pos.y + (self.speed * self.direction.y)


