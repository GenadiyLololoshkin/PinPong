from msilib.schema import Icon
from turtle import window_height
from pygame import *

win_weight = 600
win_height = 500

font.init()
font1= font.SysFont(None,40)

text_win_l = font1.render("ИГРОК СЛЕВА ПОБЕЖДАЕТ",  1, (200,0,0))
text_win_r = font1.render("ИГРОК СПРАВА ПОБЕЖДАЕТ",  1, (200,0,0))

back = (76,187,73)

main_win = display.set_mode((win_weight,win_height))
main_win.fill(back)
pyicon = image.load('pngwing.com (4).png')

FPS = 60
clock = time.Clock()

display.set_caption("ФУТБОООЛ")
display.set_icon(pyicon)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        main_win.blit(self.image,(self.rect.x, self.rect.y))
    def colliderect(self,rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 330:
            self.rect.y += self.speed  
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 330:
            self.rect.y += self.speed  

ply_r = Player('338447-Berserker.jpg',560,150,20,150,7)
ply_l = Player('101137479_w640_h640_gosudarstvennyj-flag-ukrainy.webp',20,150,20,150,7)

bll = GameSprite('pngegg(1).png', 250,200,60,60,7)
speed_x = 12
speed_y = 12

flag = False

finish=False
game=True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                flag = True

    if finish != True:
        main_win.fill(back)

        ply_r.reset()
        ply_r.update_r()

        ply_l.reset()
        ply_l.update_l()
         
        bll.reset()
        
        if flag:
            bll.reset()

            bll.rect.y += speed_y
            bll.rect.x += speed_x

            if bll.rect.y > 440 or bll.rect.y < 0:
                speed_y *= -1

            if bll.rect.x > 540:
                main_win.blit(text_win_l,(100,200))
                finish = True
            if bll.rect.x < 0:
                main_win.blit(text_win_r,(100,200))
                finish = True

            if bll.colliderect(ply_l.rect):
                speed_x *= -1
            if bll.colliderect(ply_r.rect):
                speed_x *= -1
        


    display.update()
    clock.tick(FPS)