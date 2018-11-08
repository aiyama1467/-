import pygame
from pygame.locals import *

from my_game import vector, my_obj, manager


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._bar_surf = None
        self._block_surf = None
        self._ball_surf = None
        self.size = vector.Point2D(x=400, y=600)

        self.player = my_obj.Player(self.size)
        self.blocks = my_obj.Blocks()
        self.ball = my_obj.Ball(self.size)
        self.collision_manager = manager.CollisionManager()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size.get_point(), pygame.HWSURFACE)

        self._bar_surf = pygame.image.load('image/bar.jpg')
        self._block_surf = pygame.image.load('image/block.png')
        self._ball_surf = pygame.image.load('image/ball.png')
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.K_ESCAPE:
            self._running = False

    def on_loop(self):
        self.collision_manager.is_collition_ball_blocks(self.ball, self.blocks)

        self.collision_manager.is_collition_ball_bar(self.ball, self.player)

        if self.collision_manager.is_collision_ball_wall(self.ball, self.size):
            self._running = False

        self.ball.move()

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.player.draw(self._display_surf, self._bar_surf)
        self.blocks.draw(self._display_surf, self._block_surf)
        self.ball.draw(self._display_surf, self._ball_surf)
        pygame.display.flip()

    def on_creanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            event = pygame.event.poll()
            self.on_event(event)

            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                self._running = False

            if keys[K_LEFT]:
                self.player.move_left()

            if keys[K_RIGHT]:
                self.player.move_right()

            self.on_loop()
            self.on_render()
            pygame.time.delay(10)

        self.on_creanup()
