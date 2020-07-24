import pygame
# sasuke moves and techniques:
class sasuke:
    def __init__(self):
        self.standr = [pygame.image.load('sasukes\stand\s1.png'),pygame.image.load('sasukes\stand\s2.png'),
                        pygame.image.load('sasukes\stand\s3.png'),pygame.image.load('sasukes\stand\s4.png'),
                    ]
        self.standl = [pygame.image.load('sasukes\stand\s5.png'),pygame.image.load('sasukes\stand\s6.png'),
                        pygame.image.load('sasukes\stand\s7.png'),pygame.image.load('sasukes\stand\s8.png'),
                    ]
        self.wr = [pygame.image.load('sasukes\move\m1.png'),pygame.image.load('sasukes\move\m2.png'),
                     pygame.image.load('sasukes\move\m3.png') ]  
        self.wl = [pygame.image.load('sasukes\move\l1.png'),pygame.image.load('sasukes\move\l2.png'),
                     pygame.image.load('sasukes\move\l3.png')]
        self.ju  = [pygame.image.load('sasukes\jump\j1.png'),pygame.image.load('sasukes\jump\j2.png'),
                    pygame.image.load('sasukes\jump\j3.png')]    
        self.jl =  [pygame.image.load('sasukes\jump\jl1.png'),pygame.image.load('sasukes\jump\jl2.png'),
                    pygame.image.load('sasukes\jump\jl3.png')]  
        self.dmr = [pygame.image.load('sasukes\damage\d1.png'),pygame.image.load('sasukes\damage\d3.png'),
                    pygame.image.load('sasukes\damage\d4.png'),pygame.image.load('sasukes\damage\d5.png'),
                    pygame.image.load('sasukes\damage\d5.png'),pygame.image.load('sasukes\damage\d5.png'),
                    pygame.image.load('sasukes\damage\d6.png'),pygame.image.load('sasukes\damage\d6.png'),
                    pygame.image.load('sasukes\damage\d6.png')] 
        self.dml = [pygame.image.load('sasukes\damage\dl1.png'),pygame.image.load('sasukes\damage\dl3.png'),
                    pygame.image.load('sasukes\damage\dl4.png'),pygame.image.load('sasukes\damage\dl5.png'),
                    pygame.image.load('sasukes\damage\dl5.png'),pygame.image.load('sasukes\damage\dl5.png'),
                    pygame.image.load('sasukes\damage\dl6.png'),pygame.image.load('sasukes\damage\dl6.png'),
                    pygame.image.load('sasukes\damage\dl6.png')]        
        self.fright = False
        self.wc = 0
        self.right = False
        self.left = False
        self.jump = False
        self.x = 600
        self.y = 350
        self.wco = 0  
        self.speed = 10
        self.jcount = 10
        self.jc = 0
        self. damaged =False
        self.takedam = False
        self.dc = 0
        self.attack1 = False
        self.dcounter = 0
        self.pos = -1
    def Set_enemy(self,enemy):
        self.enemy = enemy
    def draw(self,win):
        if self.wc+1> 12 or self.wco+1>9 or self.jc+1>36 :
            self.wc = 0
            self.wco = 0
            self.jc = 0
        if self.damaged :
            self.takedam = False
            if self.x<710 and self.x>20 :
                self.x+= 10 *self.pos
                if self.pos<1:
                    win.blit(self.dmr[self.dc//3],(self.x,self.y))
                else:
                    win.blit(self.dml[self.dc//3],(self.x,self.y))
                self.dc+=1
                if self.dc+1>24 :
                    self.dc = 0 
                    self.damaged = False
            else:
                self.Clear()
                self.damaged= False
                self.dc = 0
        elif self.takedam:
            if self.fright:
                win.blit(self.dmr[0],(self.x,self.y))
            else:
                win.blit(self.dml[0],(self.x,self.y))
            if self.enemy.a+1>self.enemy.fa:
                self.takedam = False
                self.enemy.attack1 = False
                self.damaged = True
                if self.enemy.fright:
                    self.pos = 1
                else:
                    self.pos = -1
            elif self.enemy.a==0 and self.enemy.nosp:
                self.takedam = False
            self.Clear()
        elif self.jump :
            if self.fright:
                win.blit(self.ju[self.jc//12],(self.x,self.y))
            else :
                win.blit(self.jl[self.jc//12],(self.x,self.y))
            self.jc+=1
            if self.jcount >= -10:
                neg = 1
                if self.jcount <0:
                    neg=-1
                self.y-=self.jcount**2 *0.5*neg
                self.jcount-=1
            else:
                self.jump = False
                self.jcount=10   
        elif self.right:
            win.blit(self.wr[self.wco//3], (self.x,self.y))
            self.wco+=1
            self.x+= self.speed
        elif self.left:
            win.blit(self.wl[self.wco//3], (self.x,self.y))
            self.wco+=1
            self.x-= self.speed
        else:
            if self.fright:
                win.blit(self.standr[self.wc//3],(self.x,self.y))
            else:
                win.blit(self.standl[self.wc//3],(self.x,self.y))
            self.wc+=1
    def Clear(self):
        self.right = False
        self.left = False 
    def Ready(self):
        return True
    def Takingdamage(self,enemy):
        self.enemy = enemy
        self.takedam = True
    def Set_Enemy(self,enemy):
        self.enemy = enemy
