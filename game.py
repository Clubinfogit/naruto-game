import pygame
#we import the characters:
from naruto import naruto 
from sasuke import sasuke
pygame.init()

win = pygame.display.set_mode((792,449))
clock = pygame.time.Clock()
pygame.display.set_caption("First Game")
bg = pygame.image.load('bg.png')

istaking = True       
run = True
sas = sasuke()
nar = naruto()
sas.Set_enemy(nar)
nar.Set_enemy(sas)
# here the game starts :
while run:
    win.blit(bg,(0,0))
    clock.tick(27)

    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys = pygame.key.get_pressed()
# we check if any of these buttons is pressed for naruto:
    if keys[pygame.K_RIGHT] and nar.x<710 and nar.Ready() :
        nar.x+= nar.speed
        nar.right = True
        nar.left = False
        nar.fright = True
        nar.attack1 = False
    elif keys[pygame.K_LEFT]and nar.x>20 and nar.Ready() :
        nar.x-= nar.speed
        nar.right = False
        nar.left = True
        nar.fright = False
        nar.attack1 = False
    elif keys[pygame.K_j] and nar.x>20 and nar.x<710 and nar.Ready():
            nar.attack1 = True
            nar.right =False
            nar.left = False
            if nar.x < sas.x+10 and nar.x>sas.x-40 and nar.y == sas.y :
                sas.Takingdamage(nar)
    elif keys[pygame.K_i]and nar.Ready() :
        nar.ra = True
        nar.Clear()
    elif keys[pygame.K_o] and nar.Ready():
        nar.miniras = True
        nar.Clear()
    else:
        nar.Clear()
        nar.wrc=0
    if not nar.jump:
        if keys[pygame.K_UP] and nar.Ready():
            nar.jump = True
            nar.right = False
            nar.left = False
            nar.wrc=0
            nar.attack1 = False
    else:
        if nar.jcount >= -10:
            neg = 1
            if nar.jcount <0:
                neg=-1
            nar.y-=nar.jcount**2 *0.5*neg
            nar.jcount-=1
        else:
            nar.jump = False
            nar.jcount=10
    # now we check the movement for sasuke:      
    if keys[pygame.K_d] and sas.x<710 and sas.Ready() :
        sas.right = True
        sas.left = False
        sas.fright = True
        sas.attack1 = False
    elif keys[pygame.K_a]and sas.x>20 and sas.Ready() :
        sas.right = False
        sas.left = True
        sas.fright = False
        sas.attack1 = False
    elif keys[pygame.K_f] and sas.x>20 and sas.x<710 and sas.Ready():
            sas.attack1 = True
            sas.right =False
            sas.left = False
    elif keys[pygame.K_r] and sas.Ready():
        sas.ch = True
        sas.Clear()
    elif keys[pygame.K_t] and sas.Ready():
        sas.kir = True
        sas.Clear()
    else:
        sas.Clear()
        sas.wrc=0
    if not sas.jump:
        if keys[pygame.K_w] and sas.Ready():
            sas.jump = True
            sas.Clear()
            sas.wrc=0
            sas.attack1 = False     
    nar.draw(win)
    sas.draw(win)
    pygame.display.update()
        
pygame.quit()            
