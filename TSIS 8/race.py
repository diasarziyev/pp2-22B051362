
 

import pygame
import random
import time
pygame.init()#initializing 
run = True
FPS = 60#setting framerite
H=800
W=600
score = 0
level=0#display

def show_score(): 
	font = pygame.font.SysFont('Georgia', 30)
	Font = font.render('Score : ' + str(score), True, 'red')	
	rect = Font.get_rect()	
	screen.blit(Font, rect)#showing score
        
def show_coins():
    font = pygame.font.SysFont('Georgia', 30)
    Font = font.render('Coins: ' + str(coins), True, 'blue')	
    rect = Font.get_rect()	
    screen.blit(Font, (0,40))
    #showing coins
     
cra = pygame.mixer.music.load("/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/TSIS-8_images_img_crash.wav")

def game_over():
    boom = pygame.image.load("/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/bomb.png")
    boom=pygame.transform.scale(boom,(300,300))
    gameover = pygame.Surface(screen.get_size())
    gameover.fill('red')
    font = pygame.font.SysFont("", 80)
    text = font.render("GAME OVER", False, 'black')
    crash_sound = pygame.mixer.Sound("/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/TSIS-8_images_img_crash.wav")

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    gameover.blit(text, (25, 200))
    screen.blit(boom, (25, 150))
    pygame.display.update()
    time.sleep(2)
    screen.blit(gameover, (0, 0))
    pygame.display.update()
    time.sleep(1)
    pygame.quit()#game over function


clock = pygame.time.Clock()#helps to set up framerite
screen = pygame.display.set_mode((W,H))
pygame.time.set_timer(pygame.USEREVENT,2000)
pygame.display.set_caption("TOKYOOOOOO DRIIIIFT!!!!!!!!")
crash = pygame.mixer.music.load("/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/TSIS-8_images_img_crash.wav")
music = pygame.mixer.music.load("/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/tok.mp3")
bg = pygame.image.load("/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/background.png")
bg = pygame.transform.scale(bg,(600,800))
speed = 5
coins = 0
coin = pygame.image.load("/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/coin.png")
coin = pygame.transform.scale(coin,(30,30))
enemy = pygame.image.load('/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/Enemy.png')
Player = pygame.image.load("/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/player.png")
pygame.mixer.music.play() #loading materials to work
class Player_car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Player
        self.rect = self.image.get_rect()
        self.rect.center = (200,500)
    def movement(self):
         pressed = pygame.key.get_pressed()
         if self.rect.left>0:
              if pressed[pygame.K_LEFT]:
                   self.rect.move_ip(-10,0)
         if self.rect.right<W:
              if pressed[pygame.K_RIGHT]:
                   self.rect.move_ip(10,0)
         if self.rect.bottom < H:
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0, 10)
         if self.rect.top > 0:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0, -10)#function to customize Player's movement and initial point

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed,3000)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy
        self.rect=self.image.get_rect()
        self.rect.center = (random.randint(48,W-48),0)
    def movement(self):
          global score
          self.rect.move_ip(0,speed)
          if self.rect.top>H:
                score +=1
                self.rect.top=0
                self.rect.center = (random.randint(48,W-48),0)#writing function 
class co(pygame.sprite.Sprite):
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = coin
          self.rect = self.image.get_rect()
          self.rect.center = (random.randint(30,W-30),0)
     def movement(self):
          global score
          self.rect.move_ip(0,speed)
          if self.rect.top>H:
                self.rect.top=0
                self.rect.center = (random.randint(30,W-30),0)
     def new(self):
          self.rect.move_ip(0,speed)
          self.rect.top=0
          self.rect.center = (random.randint(30,W-30),0)#function 
                    

coin1 = co()  
coinss= pygame.sprite.Group()
coinss.add(coin1)
racer = Player_car()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()
sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies.add(enemy1)
enemies.add(enemy2)
sprites.add(racer)
sprites.add(enemy1)
sprites.add(enemy2)
sprites.add(coin1)
#adding objects

exit = True
while exit:
    for event in pygame.event.get():#making a for 
        if event.type == pygame.QUIT:
            exit = False
        if event.type == inc_speed:
             speed += 0.5
    if score >= 15:
        enemies.add(enemy2)
        sprites.add(enemy2)
    if score >= 30:
        enemies.add(enemy3)
        sprites.add(enemy3)
    screen.blit(bg, (0, 0))
    for sprite in sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.movement()
    if pygame.sprite.spritecollideany(racer, enemies):#check for collide
        game_over()
    if pygame.sprite.spritecollideany(racer, coinss):
        coins += 1
        sound1= pygame.mixer.Sound("/Users/dias/Desktop/КБТУ Учебники/pp2/TSIS 8/images/TSIS-8_images_img_cashier-quotka-chingquot-sound-effect-129698.mp3")
        pygame.mixer.find_channel(True).play(sound1)
        for c in coinss:
             c.kill()
        coin2 = co()
        coinss.add(coin2)
        sprites.add(coin2)
        coin2.new()#add new coins after collecting previous
    show_coins()
    show_score()
    pygame.display.update()
    clock.tick(FPS)
    