from pygame import *
from random import *
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed, weight, height):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (weight, height))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x 
        self.rect.y = sprite_y
        self.speed = sprite_speed
        
    
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Soldier(GameSprite):
    def movement(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < scr_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.right, self.rect.top, 15, 17, 10)
        bullets.add(bullet)

class Enemy(GameSprite):
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 5:
            self.rect.x = randint(80, scr_width - 80)
            self.rect.x = 1000
            
class Bullet(GameSprite):
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.kill()

back = (180,190,180)
scr_width = 1000
scr_length = 600

mixer.init()
mixer.music.load("Ola Strandh — _LMB Battle Theme_ Tom Clancy's The Division.mp3")
mixer.music.play()

health = 5
kills = 0
ammo = 10

font.init()
font1 = font.SysFont('Arial', 32)
font.init()
health_text = font1.render('Health:' + str(health), 1, (0, 0, 180))
kill_text = font1.render('Kills:'+ str(kills), 1, (0, 0, 180))
ammo_text = font1.render('Bullets:'+ str(ammo), 1, (0, 0, 180)) 

screen = display.set_mode((scr_width, scr_length))
display.set_caption('Zombie_shooter')
screen.fill(back)

shooter = Soldier('soldier2.png', 250,300,5,100,100)
platform = GameSprite('concrete_floor.png', 0,400,5,1000,200)

bullets = sprite.Group()
monsters = sprite.Group()

for i in range(0,5):
    monster = Enemy('zombie1.png', 1000, 275,randint(1, 7), 100, 130)
    monsters.add(monster)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                shooter.fire()
    if finish != True:
        screen.fill(back)
        screen.blit(health_text,(20,30))
        screen.blit(kill_text, (20,90))
        screen.blit(ammo_text, (20,60))

        shooter.movement()
        shooter.reset()
        
        platform.reset()
        
        bullets.update()
        bullets.draw(screen)

        monsters.update()
        monsters.draw(screen)

    display.update()
    clock.tick(FPS)