# import pygame as pg
# from pygame.sprite import Sprite, Group

# class Barrier(Sprite):
#     color = 255, 0, 0
#     black = 0, 0, 0

#     def __init__(self, game, rect):
#         super().__init__()
#         self.screen = game.screen
#         self.rect = rect
#         self.settings = game.settings
#         self.image = pg.image.load(f'images/barrier1.png')
#         self.rect= self.image.get_rect()
#         self.rect.y = self.rect.height
#         self.dead =False
#         self.damage = 1
#         # self.settings = game.settings
#         # self.image = pg.image.load('images/alien0.bmp')
#         # self.rect = self.image.get_rect()
#         # self.rect.y = self.rect.height
#         # self.x = float(self.rect.x)
        
#     def hit(self): 
#         if not self.dead:
#             self.damage +=1
#             self.image = pg.image.load(f'images/barrier{self.damage}.png')
#             if self.damage > 7:
#                 self.dead = True
#                 self.kill()
            
            
#     def update(self): self.draw()
#     def draw(self): 
#         spacing_list = [6, 3, 1.9, 1.3]
#         for barier_number in range(4):
#             self.screen.blit(self.image, (self.settings.screen_width/spacing_list[barier_number], 600))
            
#         #pg.draw.rect(self.screen, Barrier.color, self.rect, 0, 20)
#         #pg.draw.circle(self.screen, self.settings.bg_color, (self.rect.centerx, self.rect.bottom), self.rect.width/6)


# class Barriers:
#     def __init__(self, game):
#         self.game = game
#         self.settings = game.settings
        
#         self.ship_lasers = game.ship_lasers
#         self.alien_lasers = game.alien_lasers
#         self.barriers = Group()

#         self.create_barriers()
        

#     def create_barriers(self):     
#         barrier_width = self.settings.screen_width // 10
#         barrier_height = self.settings.screen_height // 20
#         spacing = self.settings.screen_width // 5

#         # Calculate the y-coordinate for the barriers
#         y = self.settings.screen_height - barrier_height - 20

#         for i in range(4):
#             x = (i + 1) * spacing - barrier_width // 2
#             rect = pg.Rect(x, y, barrier_width, barrier_height)
#             barrier = Barrier(game=self.game, rect=rect)
#             self.barriers.add(barrier)
#         # width = self.settings.screen_width / 3
#         # height = 2.0 * width / 4.0
#         # top = self.settings.screen_height - 2.1 * height
#         # rects = [pg.Rect(x * 2 * width + 1.5 * width, top, width, height) for x in range(4)]   # SP w  3w  5w  7w  SP
#         # barriers = [Barrier(game=self.game, rect=rects[i]) for i in range(4)]
#         # # barrier = Barrier(game = self.game, rect= rects)
#         # self.barriers.add(barriers)
        

    

#     # def hit(self): pass 
    
#     def check_collisions(self):
#         barrier_collisions = pg.sprite.groupcollide(
#             self.barriers, self.alien_lasers.lasers, False, True
#         )
#         for barrier, lasers in barrier_collisions.items():
#             for laser in lasers:
#                 barrier.hit()

#         barrier_collisions = pg.sprite.groupcollide(
#             self.barriers, self.ship_lasers.lasers, False, True
#         )
#         for barrier, lasers in barrier_collisions.items():
#             for laser in lasers:
#                 barrier.hit()

#         # collisions = pg.sprite.groupcollide(self.barriers,self.alien_lasers.lasers, True, True)
#         # if collisions:
#         #     for barrier in collisions:
#         #         barrier.hit()
#         # print("hello")
#         # collisions = pg.sprite.groupcollide(self.barriers, self.ship_lasers.lasers, True, True)
#         # if collisions:
#         #     for barrier in collisions:
#         #         barrier.hit()

#     def reset(self):
#         self.create_barriers()

#     def update(self):
#         for barrier in self.barriers: barrier.update()
#         self.check_collisions()

#     def draw(self):
#         for barrier in self.barriers: barrier.draw()


import pygame as pg
from pygame.sprite import Sprite, Group

class Barrier(Sprite):
    color = 255, 0, 0
    black = 0, 0, 0

    def __init__(self, game, rect):
        super().__init__()
        self.screen = game.screen
        self.rect = rect
        self.settings = game.settings
        self.image = pg.image.load(f'images/barrier1.png')
        self.rect.y = self.rect.height
        self.dead = False
        self.damage = 1

    def hit(self):
        if not self.dead:
            self.damage += 1
            self.image = pg.image.load(f'images/barrier{self.damage}.png')
            if self.damage > 3:
                self.dead = True
                self.kill()  # Remove the barrier from the group

    def update(self):
        self.draw()

    def draw(self):
        # spacing_list = [6, 3, 1.9, 1.3]
        # for barier_number in range(4):
        #     self.screen.blit(self.image, (self.settings.screen_width/spacing_list[barier_number], 600))
        self.screen.blit(self.image, self.rect)


class Barriers:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.ship_lasers = game.ship_lasers
        self.alien_lasers = game.alien_lasers
        self.barriers = Group()
        self.create_barriers()

    def create_barriers(self):
        barrier_width = self.settings.screen_width // 10
        barrier_height = self.settings.screen_height // 1.25
        spacing = self.settings.screen_width // 5

        # Calculate the y-coordinate for the barriers
        y = self.settings.screen_height - barrier_height 

        for i in range(4):
            x = (i + 1) * spacing - barrier_width // 2
            rect = pg.Rect(x, y, barrier_width, barrier_height)
            barrier = Barrier(game=self.game, rect=rect)
            self.barriers.add(barrier)

    def check_collisions(self):
        barrier_collisions = pg.sprite.groupcollide(
            self.barriers, self.alien_lasers.lasers, False, True
        )
        for barrier, lasers in barrier_collisions.items():
            for laser in lasers:
                barrier.hit()

        barrier_collisions = pg.sprite.groupcollide(
            self.barriers, self.ship_lasers.lasers, False, True
        )
        for barrier, lasers in barrier_collisions.items():
            for laser in lasers:
                barrier.hit()

    def reset(self):
        self.create_barriers()

    def update(self):
        for barrier in self.barriers:
            barrier.update()
        self.check_collisions()

    def draw(self):
        for barrier in self.barriers:
            barrier.draw()
