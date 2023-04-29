#Создай собственный Шутер!


from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

background = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(background)
display.set_caption('пинг-понг')

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont('Arial', 36)
win1 = font1.render('Player 1 win', 1, (0, 0, 255))
win2 = font1.render('Player 2 win', 1, (255, 0, 0))

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)


speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.fill(background)
        racket1.update_left()
        racket2.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x = -speed_x
            
        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y = -speed_y

        if ball.rect.x < 0:
            finish = True
            window.blit(win2, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(win2, (200, 200))

            

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
        
    clock.tick(FPS)
