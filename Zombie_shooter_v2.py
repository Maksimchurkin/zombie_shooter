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
black = (0,0,0)
scr_width = 1000
scr_length = 600

mixer.init()
mixer.music.load("Ola Strandh — _LMB Battle Theme_ Tom Clancy's The Division.mp3")
mixer.music.play()

health = 5
kills = 0
ammo = 150

font.init()
font1 = font.SysFont('Arial', 32)
font2 = font.SysFont('Arial', 70)
font.init()
health_text = font1.render('Health:' + str(health), 1, (0, 0, 180))
kill_text = font1.render('Kills:'+ str(kills), 1, (0, 0, 180))
ammo_text = font1.render('Bullets:'+ str(ammo), 1, (0, 0, 180)) 
lose = font2.render('YOU LOST!',True, (180,0,0))
win = font2.render('YOU WIN!',True, (0,180,0))

screen = display.set_mode((scr_width, scr_length))
display.set_caption('Zombie_shooter')
screen.fill(back)

shooter = Soldier('soldier2.png', 250,300,5,100,100)
platform = GameSprite('concrete_floor.png', 0,400,5,1000,200)

bullets = sprite.Group()
monsters = sprite.Group()

def create_enemies(num_enemies):
    for i in range(num_enemies):
        monster = Enemy('zombie1.png', 1000, 275,randint(1, 7), 100, 130)
        monsters.add(monster)

create_enemies(5)

sprites_touch = sprite.spritecollide(shooter, monsters, False)
hit = sprite.groupcollide(monsters, bullets, True, True)


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
                ammo -= 1
    
    if finish != True:
        screen.fill(back)
        
        health_text = font1.render('Health:' + str(health), 1, (0, 0, 180))
        kill_text = font1.render('Kills:'+ str(kills), 1, (0, 0, 180))
        ammo_text = font1.render('Bullets:'+ str(ammo), 1, (0, 0, 180)) 
        
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
        
        sprites_touch = sprite.spritecollide(shooter, monsters, True)
        hit = sprite.groupcollide(monsters, bullets, True, True)
        
        if hit:
            kills += 1
            create_enemies(1)
        elif sprites_touch:
            health -= 1
            create_enemies(1)
        
        if kills >= 150:
            screen.fill(black)
            screen.blit(win,(400,150))
            finish = True
            mixer.music.load("victory_sJDDywi.mp3")
            mixer.music.play()
            

        elif health <= 0:
            screen.fill(black)
            screen.blit(lose,(380,150))
            finish = True
            mixer.music.load("the-price-is-right-losing-horn_2.mp3")
            mixer.music.play()
            

    display.update()
    clock.tick(FPS)