import sys, pygame as pg
import game_functions as gf

from alien import Alien
from alien import ufo
from settings import Settings
from ship import Ship


BLOODRED = (101, 28, 50)
RED= (150, 28, 50)
LIGHTRED = (255,114,118)
class Start_screen:
    
    alien_images0 = [pg.transform.rotozoom(pg.image.load(f'images/Cow_skull{n+1}.png'), 0, 0.7) for n in range(8)]
    alien_images1 = [pg.transform.rotozoom(pg.image.load(f'images/Orc_skull{n+1}.png'), 0, 0.7) for n in range(6)]
    ufo = [pg.transform.rotozoom(pg.image.load(f'images/Cyclop_skull{n+1}.png'), 0, 0.7) for n in range(8)]
    alien_images2 = [pg.transform.rotozoom(pg.image.load(f'images/Enemy_skull{n+1}.png'), 0, 0.7) for n in range(7)]

    

    def __init__(self, game):
        self.title_font = pg.font.SysFont(None, 100, True)
        self.title_bg = pg.image.load(f'images/desert2.png')
        # self.highscore = game.stats.get_highscore()
        self.screen = game.screen
        self.title_music = pg.mixer.Sound('sounds/undetale_spider_dance.wav')
        self.title_music.play()
        self.title_music.set_volume(0.15)
        self.setting = Settings()
        self.screen_width = self.setting.screen_width
        self.screen_height = self.setting.screen_height
        self.finish_start = False
        self.highscore = game.scoreboard.high_score
        print(self.highscore)
        # self.ship = Ship(game)

    def create_button(self,message, x, y, width, height, hover_color, normal_color):
        mouse = pg.mouse.get_pos()
        press = pg.mouse.get_pressed(3)
        if x +width > mouse[0] > x and y + height > mouse[1] >y: 
            pg.draw.rect(self.screen, hover_color, (x,y, width, height))
            if press[0] ==1:
                self.finish_start = True
                self.title_music.stop()
        else:
            pg.draw.rect(self.screen, normal_color, (x, y, width, height))

        play_button_text = self.title_font.render(message, True, RED)
        self.screen.blit(play_button_text, (int(x), int(y)))


    def draw(self):
        start_text = self.title_font.render("SKULL INVADERS ", True, BLOODRED)
        high_score = self.title_font.render(str(self.highscore),False, BLOODRED)
        high_score_text = self.title_font.render("High Score: ",False, BLOODRED)


        alien_images0 = (pg.image.load(f'images/Cow_skull1.png')) 
        alien_images1 =pg.image.load(f'images/Orc_skull1.png')
        alien_images3 = pg.image.load(f'images/Cyclop_skull1.png')
        alien_images2 = pg.image.load(f'images/Enemy_skull1.png')
        

        while not self.finish_start :
            self.title_bg = pg.image.load(f'images/desert2.png')
            
            
            self.screen.blit(self.title_bg, (0,0))
            self.create_button("PLAY", self.screen_width/2.5, 500, 200, 60, LIGHTRED, BLOODRED)
            self.screen.blit(start_text, ((self.screen_width - start_text.get_width())/2,90))
            self.screen.blit(high_score, (self.screen_width-250, 700))
            self.screen.blit(high_score_text, (self.screen_width -800, 700))

            self.screen.blit(alien_images0, (self.screen_width/2.5, 200))
            self.screen.blit(alien_images1, (self.screen_width/2.5, 270))
            self.screen.blit(alien_images2, (self.screen_width/2.5, 340))
            self.screen.blit(alien_images3, (self.screen_width/2.5, 410))
            

            alien1 = self.title_font.render("= 50", True, RED)
            alien2 = self.title_font.render("= 100", True, RED)
            alien3 = self.title_font.render("= 150", True, RED)
            alien4 = self.title_font.render("= ???", True, RED)
            list_of_scores= (alien1, alien2, alien3, alien4)

            start_position = 200 
            for score in list_of_scores:
                self.screen.blit(score, (self.screen_width/2, start_position))
                start_position +=70
           
            
            # gf.check_events(self.setting, self.ship)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.update()
            
