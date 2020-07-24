import pygame
# naruto character and moves:
class naruto:
    def __init__(self):
        self.wr = [pygame.image.load('move\R1.png'),pygame.image.load('move\R2.png'),pygame.image.load('move\R3.png'),pygame.image.load('move\R4.png'),pygame.image.load('move\R5.png'),pygame.image.load('move\R6.png')]
        self.wl = [pygame.image.load('move\L77.png'),pygame.image.load('move\L88.png'),pygame.image.load('move\L99.png'),pygame.image.load('move\L110.png'),pygame.image.load('move\L111.png'),pygame.image.load('move\L112.png')]
        self.rstand=[pygame.image.load('stand\s1.png'),pygame.image.load('stand\s2.png'),pygame.image.load('stand\s3.png'),pygame.image.load('stand\s4.png')]
        self.lstand=[pygame.image.load('stand\s5.png'),pygame.image.load('stand\s6.png'),pygame.image.load('stand\s7.png'),pygame.image.load('stand\s8.png')]
        self.jr = [pygame.image.load('jump\j1.png'),pygame.image.load('jump\j2.png'),pygame.image.load('jump\j3.png'),pygame.image.load('jump\j4.png'),pygame.image.load('jump\j5.png'),pygame.image.load('jump\j5.png'),pygame.image.load('jump\j6.png')]
        self.jl = [pygame.image.load('jump\j7.png'),pygame.image.load('jump\j8.png'),pygame.image.load('jump\j9.png'),pygame.image.load('jump\j10.png'),pygame.image.load('jump\j11.png'),pygame.image.load('jump\j11.png'),pygame.image.load('jump\j12.png')]
        self.damaged =[pygame.image.load('damage\d0.png'),pygame.image.load('damage\d1.png'),pygame.image.load('damage\d2.png'),pygame.image.load('damage\d3.png')]
        self.attackr = [pygame.image.load('attack1\A1.png'),pygame.image.load('attack1\A2.png'),pygame.image.load('attack1\A3.png'),pygame.image.load('attack1\A4.png'),pygame.image.load('attack1\A5.png'),pygame.image.load('attack1\A6.png')]
        self.attackL = [pygame.image.load('attack1\A7.png'),pygame.image.load('attack1\A8.png'),pygame.image.load('attack1\A9.png'),pygame.image.load('attack1\A10.png'),pygame.image.load('attack1\A11.png'),pygame.image.load('attack1\A12.png')]
        self.ras = [pygame.image.load('special1\s1.png'),pygame.image.load('special1\s2.png'),pygame.image.load('special1\s3.png'),pygame.image.load('special1\s4.png'),pygame.image.load('special1\s5.png'),pygame.image.load('special1\s6.png'),pygame.image.load('special1\s7.png'),pygame.image.load('special1\s8.png'),pygame.image.load('special1\s9.png')]
        self.rasl = [pygame.image.load('special1\s10.png'),pygame.image.load('special1\s11.png'),pygame.image.load('special1\s12.png'),pygame.image.load('special1\s13.png'),pygame.image.load('special1\s14.png'),pygame.image.load('special1\s15.png'),pygame.image.load('special1\s16.png'),pygame.image.load('special1\s17.png'),pygame.image.load('special1\s18.png')]
        self.mnr = [pygame.image.load('sp2\s1.png'),pygame.image.load('sp2\s2.png'),pygame.image.load('sp2\s3.png'),pygame.image.load('sp2\s4.png')]
        self.mr = [pygame.image.load('mras\m1.png'),pygame.image.load('mras\m2.png'),pygame.image.load('mras\m3.png'),pygame.image.load('mras\m4.png'),pygame.image.load('mras\m5.png'),pygame.image.load('mras\m6.png'),pygame.image.load('mras\m7.png'),pygame.image.load('mras\m8.png'),pygame.image.load('mras\m9.png'),pygame.image.load('mras\m10.png'),pygame.image.load('mras\m11.png'),pygame.image.load('mras\m12.png'),pygame.image.load('mras\m13.png'),pygame.image.load('mras\m14.png'),pygame.image.load('mras\m15.png'),pygame.image.load('mras\m16.png'),pygame.image.load('mras\m17.png')]
        self.mnrl = [pygame.image.load('sp2\s5.png'),pygame.image.load('sp2\s6.png'),pygame.image.load('sp2\s7.png'),pygame.image.load('sp2\s8.png')]
        self.x = 100
        self.y= 350
        self.speed = 10
        self.jump = False
        self.jcount = 10
        self.left = False
        self.right = False
        self.wc = 0
        self.fright = True
        self.wrc = 0
        self.jc=0
        self.damage = False
        self.dc = 0
        self.attack1 = False
        self.a = 0
        self.ra = False
        self.r = 0
        self.miniras = False
        self.mnc = 0
        self.mc=0
        self.m =False
        self.xr = 21
        self.yr = 0
        self.rm = 0
        self.c = False
        self.explose = False
        self.fa = 24
        self.nosp = False
        self.tx = 0
        self.ty = 0
    def Set_enemy(self,enemy):
        self.enemy = enemy
    def draw(self,win):
        #here we set the counters to 0 if they are greater than the list max index:
        if self.wc+1>12 or self.wrc+1>18 or self.jc+1 >21 or self.dc+1> 18 or self.a+1>24   :
                self.wc =0
                self.wrc=0
                self.jc=0
                self.dc=0
                self.a=0
        if self.r+1>27:
            self.ra = False
            self.r = 0
            if self.enemy.takedam:
                self.enemy.damaged = True
            if self.fright:
                self.enemy.pos = 1
            else:
                self.enemy.pos  = -1
        # here we make the rasengan explose if it hits the enemy or when it goes over the screen:
        if self.explose :
            if self.fright!= self.enemy.fright:
                self.tx = 20
            self.enemy.fright = True
            self.enemy.pos = 1
            self.nosp = False
            win.blit(self.mr[self.mc//4],(self.xr-self.tx,self.yr-self.ty))
            self.mc+=1
            if self.c:
                self.tx = 120
            self.ty = 0
            if self.mc+1>68:
                self.mc =0
                self.explose = False
                self.m=False
                if self.enemy.takedam :
                    self.enemy.damaged = True
                    self.ty = 100
        # when naruto does the action , the rasengan starts to move until it touches something:
        if self.m:
            self.nosp = False
            win.blit(self.mr[self.mc//6],(self.xr,self.yr))
            self.mc+=1
            if  self.c:
                self.xr+=10
                self.enemy.pos = 1
            else :
                self.xr-=10
                self.enemy.pos = -1
            if self.mc+1> 30:
                self.mc = 23
            if self.xr>730 or self.xr<10:
                self.m = False
                self.explose = True
                self.mc = 30
                self.yr -=50
            if self.xr-20 < self.enemy.x and self.xr+20>self.enemy.x and self.yr == self.enemy.y :
                self.enemy.takedam = True
                self.yr -=50 
                self.xr = self.enemy.x-20
                self.m = False
                self.mc =24
                self.explose= True
        #when we press o , naruto releases minrasengan:
        if self.miniras:
            self.nosp =False
            if self.fright:
                win.blit(self.mnr[self.mnc//6],(self.x,self.y))
            else:
               win.blit(self.mnrl[self.mnc//6],(self.x,self.y)) 
            self.mnc+=1
            if self.mnc+1>24 :
                self.mnc = 0
                self.miniras = False
                self.m = True
                if self.fright:
                    # we set the rasengan x and y depending on where is naruto:
                    self.xr = self.x+100
                else:
                    self.xr = self.x-100
                self.c = self.fright # we tell the rasengan whether to go right or left
                self.yr = self.y
        #  when we press i the simple rasengan appear:
        elif self.ra :
            self.nosp  = False
            if self.fright:
                win.blit(self.ras[self.r//3],(self.x,self.y))
                self.r+=1
            else:
                win.blit(self.rasl[self.r//3],(self.x,self.y))
                self.r+=1
            if self.x < self.enemy.x+70 and self.x>self.enemy.x-80 and self.y == self.enemy.y :
                self.enemy.takedam = True
                self.enemy.Clear()
        elif self.jump and self.fright:
            win.blit(self.jr[self.jc//3],(self.x,self.y))
            self.jc+=1
        elif self.jump :
             win.blit(self.jl[self.jc//3],(self.x,self.y))
             self.jc+=1
        elif self.right:
            win.blit(self.wr[self.wrc//3],(self.x,self.y))
            self.wrc+=1
        elif self.left:
            win.blit(self.wl[self.wrc//3],(self.x,self.y))
            self.wrc+=1
        elif self.damage:
            win.blit(self.damaged[0],(self.x,self.y))
            self.dc+=1
            self.x-=3
        # when we press j naruto start punching:
        elif self.attack1:
            if  self.fright :
                self.x+=1
                win.blit(self.attackr[self.a//4],(self.x,self.y))
                self.a+=1
            else:
                self.x-=1
                win.blit(self.attackL[self.a//4],(self.x,self.y))
                self.a+=1     
        # the standing:           
        else:
            if self.fright:
                win.blit(self.rstand[self.wc//3],(self.x,self.y))
                self.wc+=1
            else:
                win.blit(self.lstand[self.wc//3],(self.x,self.y))
                self.wc+=1  
    # we check if naruto is not doing any of his special moves:
    def Ready(self):
        return not(self.ra or self.miniras)
    # we set all naruto's movements to false
    def Clear(self):
        self.right = False
        self.left = False
        self.attack1 = False
        self.a = 0
        self.nosp = True
    def Set_Enemy(enemy):
        self.enemy = enemy
