import pygame as pg 
import os
# import pygame.font

class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = 0
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.prep_score()
        self.high_score_file = open(f'highscore.txt', "r+" )
        if os.path.getsize('highscore.txt') == 0: self.high_score_file.write("0")
        
        else:
            score =self.high_score_file.readlines()
            
            a = []
            for line in score:
                for i in line:
                    if i.isdigit() == True:
                        print(a)
                        a.append(int(i))

            r= [str(integer) for integer in a]
            a_string = "". join(r)

            res = int(a_string)
            print(res)

            self.high_score = res
        

    def increment_score(self): 
        self.score += self.settings.alien_points
        self.prep_score()


    def open_high_score_file(self):
        self.high_score_file = open(f'highscore.txt', "r+")

    def close_high_score_file(self):
        self.high_score_file.close()

    def prep_score(self): 
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def reset(self): 
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)