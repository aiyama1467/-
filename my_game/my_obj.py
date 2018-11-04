from my_game import vector, manager


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
        self.size = vector.Point2D(x=80, y=40)
        self.pos = vector.Point2D(x * self.size.x, y * self.size.y)

    def draw(self, screen, image):
        if self.is_Exist:
            screen.blit(image, (self.pos.x, self.pos.y))


class Blocks:
    def __init__(self):
        self.blocks = [[Block(i, j) for j in range(4)] for i in range(5)]

    def draw(self, screen, image):
        for i in range(5):
            for j in range(4):
                self.blocks[i][j].draw(screen, image)


class Ball:
    def __init__(self, w_size):
        self.size = vector.Point2D(20, 20)
        self.pos = vector.Point2D(0, (w_size.y * 5/6) - self.size.y)
        self.direction = vector.Point2D(0, -1)
        self.speed = 5
        self.collision_manager = manager.CollisionManager()

    def draw(self, screen, image):
        screen.blit(image, (self.pos.x, self.pos.y))

    def move(self):
        self.pos.x = self.pos.x + (self.speed * self.direction.x)
        self.pos.y = self.pos.y + (self.speed * self.direction.y)


