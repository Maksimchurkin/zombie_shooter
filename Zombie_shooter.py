from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed, weight, height):
        sprite.Sprite().__init__()
        self.image = transform.scale(image.load(sprite_image), (weight, height))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x 
        self.rect.y = sprite_y
        self.speed = sprite_speed
        
    
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

back = (180,190,180)
scr_width = 1000
scr_length = 600

mixer.init()
mixer.music.load("Ola Strandh — _LMB Battle Theme_ Tom Clancy's The Division.mp3")
mixer.music.play()

screen = display.set_mode((scr_width, scr_length))
display.set_caption('Zombie_shooter')
screen.fill(back)

class Soldier(GameSprite):
    def movement(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < scr_width - 80:
            self.rect.x += self.speed

shooter = Soldier('soldier2.png', 250,300,5,100,100)
platform = GameSprite('concrete_floor.png', 0,400,5,1000,200)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        screen.fill(back)
        shooter.movement()
        shooter.reset()
        platform.reset()

    display.update()
    clock.tick(FPS)