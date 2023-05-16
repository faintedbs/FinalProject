# File created by Anthony Garland
"""
Goals:
Add Background (done)
Add Flies (Done)
Add Sounds
Add water bucket
"""
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/


# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
from math import pi
# from pg.sprite import Sprite

pg.mixer.init()
pg.mixer.music.load("BTD5.mp3")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.5)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "image")
print(game_folder)

# Create game class to import self
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
        

    def new(self):
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # Adds platforms to all sprites
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        # Adds player to all sprites
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,10):
            m = Mob(self,20,10,(0,0,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    # Determines wether window is running or not
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        
        # if the player is falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.standing = True
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
            else:
                self.player.standing = False
# draws text as well as imports images
    def draw(self):
        self.screen.fill(BLUE)
        # Displaying Player Image
        self.image = pg.image.load(os.path.join(game_folder, 'person.jpg')).convert()
        self.forest = pg.image.load(os.path.join(game_folder, 'forest.jpg')).convert()
        self.image.set_colorkey(BLUE)
        self.forest.set_colorkey(BLUE)
        forest_rect = self.forest.get_rect()   
        self.screen.blit(self.forest, forest_rect)
        self.all_sprites.draw(self.screen)
        pg.display.flip()



    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('impact')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
        
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
    
    

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()