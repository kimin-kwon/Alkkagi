import pygame
from lib.display import text_old
import abc
# import music

LEFT_BOUNDARY = 0
RIGHT_BOUNDARY = 1280
UPPER_BOUNDARY = 0
LOWER_BOUNDARY = 720

# initialize
pygame.init()
screen_width, screen_height = RIGHT_BOUNDARY, LOWER_BOUNDARY
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision at boundary")




key_left=False
key_right=False
key_down=False
key_up=False
bestoutof=1
playernumber=2
idx=1
key_enter=False

class Image :
    def __init__(self, center, radius, path):
        self.center=center
        self.radius=radius
        self.path=path
        self.radius1=self.radius-1
        
    def drawstone(self):#load image
        self.img_width, self.img_height = 2* self.radius, 2* self.radius
        self.img = pygame. image.load('Resources/'+self.path)
        self.img = pygame.transform.scale(self.img, (self.img_width, self.img_height))
        
        self.img_rect = self.img.get_rect()
        self.img_rect.center = self.center
        screen.blit(self.img, self.img_rect)

    def changestonesize(self):
        if self.radius1 <= self.radius: 
            self.radius1=self.radius
            self.radius += 1
            self.drawstone()
            if self.radius > 80 :
                self.radius1=self.radius+1
        elif self.radius1>=self.radius :
            self.radius1=self.radius
            self.radius-=1
            self.drawstone()
            if self.radius<40 :
                self.radius1=self.radius-1
        
a_change=True
b_change=False
c_change=False
d_change=False
e_change=False
f_change=False

selectplayer=True
selectstone=False

a=Image((340,400), 60,'korea.png')
b=Image((640,400), 60, 'brazil.png')
c=Image((940, 400), 60, 'belgium.png')
d=Image((340, 560), 60, 'china.png')
e=Image((640, 560), 60, 'ukraina.png')
f=Image((940, 560), 60, 'ghana.png')

P1_determine=Image((220,225), 60, 'snu.png')
P2_determine=Image((540,225), 60, 'snu.png')
P3_determine=Image((860,225), 60, 'snu.png')
P4_determine=Image((1180,225), 60, 'snu.png')
key_enter_times=0

change_times=0


def drawstones4P():
    global a,b,c,d,e,f, key_enter, a_change, b_change, c_change, d_change, e_change, f_change, key_left, key_right, key_down, key_up,key_enter, P1_determine, P2_determine, P3_determine, key_enter_times
    
    text_stone=text_old.Text('Stone Select', 100, 'white')
    text_old.show(text_stone, (640, 100), screen)

    text_1P = text_old.Text('1P : ', 75, 'white')
    text_2P = text_old.Text('2P : ', 75, 'white')
    text_3P = text_old.Text('3P : ', 75, 'white')
    text_4P = text_old.Text('4P : ', 75, 'white')

    text_old.show(text_1P, (100, 225), screen)
    text_old.show(text_2P, (420, 225), screen)
    text_old.show(text_3P, (740, 225), screen)
    text_old.show(text_4P, (1060, 225), screen)
#키설명
    pygame.draw.rect(screen, '#aaaaaa', (75, 575, 185, 110), border_radius=30)
    text_old.show(esc, (167.5, 600), screen)
    text_old.show(enter, (167.5, 625), screen)
    text_old.show(z, (167.5, 650), screen)
 #끝   
    if a_change :
        a.changestonesize()
        if key_right :
            a_change=False
            b_change=True
            a.radius=60
        if key_down :
            a_change=False
            d_change=True
            a.radius=60

   
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=a.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=a.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=a.path
        if key_enter_times==4 :
            if P4_determine.path== 'snu.png' :
                P4_determine.path= a.path


    elif b_change :
        b.changestonesize()
        if key_left :
            b_change=False
            a_change=True
            b.radius=60
        if key_right :
            b_change=False
            c_change=True
            b.radius=60            
        if key_down :
            b_change=False
            e_change=True
            b.radius=60
            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=b.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=b.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=b.path
        if key_enter_times==4 :
            if P4_determine.path== 'snu.png' :
                P4_determine.path= b.path            


    elif c_change :
        c.changestonesize()
        if key_left :
            c_change=False
            b_change=True
            c.radius=60
        if key_down :
            c_change=False
            f_change=True
            c.radius=60
            
            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=c.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=c.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=c.path
        if key_enter_times==4 :
            if P4_determine.path== 'snu.png' :
                P4_determine.path= c.path


    elif d_change :
        d.changestonesize()
        if key_right :
            d_change=False
            e_change=True
            d.radius=60
        if key_up :
            d_change=False
            a_change=True
            d.radius=60

            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=d.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=d.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=d.path
        if key_enter_times==4 :
            if P4_determine.path== 'snu.png' :
                P4_determine.path= d.path


    elif e_change :
        e.changestonesize()
        if key_left :
            e_change=False
            d_change=True
            e.radius=60
        if key_right :
            e_change=False
            f_change=True
            e.radius=60
        if key_up :
            e_change=False
            b_change=True
            e.radius=60

            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=e.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=e.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=e.path
        if key_enter_times==4 :
            if P4_determine.path== 'snu.png' :
                P4_determine.path= e.path            


    elif f_change :
        f.changestonesize()
        if key_left :
            f_change=False
            e_change=True
            f.radius=60
        if key_up :
            f_change=False
            c_change=True
            f.radius=60

            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=f.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=f.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=f.path
            
        if key_enter_times==4 :
            if P4_determine.path== 'snu.png' :
                P4_determine.path= f.path
    if key_enter_times == 5 :
        text_select = text_old.Text('Press \'Enter\' to determine', 75, 'white')
        text_old.show(text_select, (640, 460), screen)
        a.center=(10000,10000)
        b.center=(10000,10000)
        c.center=(10000,10000)
        d.center=(10000,10000)
        e.center=(10000,10000)
        f.center=(10000,10000)
    

    a.drawstone()        
    b.drawstone()
    c.drawstone()
    d.drawstone()
    e.drawstone()
    f.drawstone()


    if key_enter_times>=1 :
        P1_determine.drawstone()
    if key_enter_times>=2 :
        P2_determine.drawstone()
    if key_enter_times>=3 :
        P3_determine.drawstone()
    if key_enter_times>=4 :
        P4_determine.drawstone()


    key_right=False
    key_left=False
    key_up=False
    key_down=False
    key_enter=False

def drawstones3P():
    global a,b,c,d,e,f, key_enter, a_change, b_change, c_change, d_change, e_change, f_change, key_left, key_right, key_down, key_up,key_enter, P1_determine, P2_determine, P3_determine, key_enter_times
    
    text_stone=text_old.Text('Stone Select', 100, 'white')
    text_old.show(text_stone, (640, 100), screen)

    text_1P = text_old.Text('1P : ', 75, 'white')
    text_2P = text_old.Text('2P : ', 75, 'white')
    text_3P = text_old.Text('3P : ', 75, 'white')

    text_old.show(text_1P, (100, 225), screen)
    text_old.show(text_2P, (550, 225), screen)
    text_old.show(text_3P, (1000, 225), screen)

#키설명
    pygame.draw.rect(screen, '#aaaaaa', (75, 575, 185, 110), border_radius=30)
    text_old.show(esc, (167.5, 600), screen)
    text_old.show(enter, (167.5, 625), screen)
    text_old.show(z, (167.5, 650), screen)
#끝
    
    if a_change :
        a.changestonesize()
        if key_right :
            a_change=False
            b_change=True
            a.radius=60
        if key_down :
            a_change=False
            d_change=True
            a.radius=60
            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=a.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=a.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=a.path
            


    elif b_change :
        b.changestonesize()
        if key_left :
            b_change=False
            a_change=True
            b.radius=60
        if key_right :
            b_change=False
            c_change=True
            b.radius=60            
        if key_down :
            b_change=False
            e_change=True
            b.radius=60
            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=b.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=b.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=b.path
            


    elif c_change :
        c.changestonesize()
        if key_left :
            c_change=False
            b_change=True
            c.radius=60
        if key_down :
            c_change=False
            f_change=True
            c.radius=60
            
            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=c.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=c.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=c.path



    elif d_change :
        d.changestonesize()
        if key_right :
            d_change=False
            e_change=True
            d.radius=60
        if key_up :
            d_change=False
            a_change=True
            d.radius=60

            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=d.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=d.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=d.path



    elif e_change :
        e.changestonesize()
        if key_left :
            e_change=False
            d_change=True
            e.radius=60
        if key_right :
            e_change=False
            f_change=True
            e.radius=60
        if key_up :
            e_change=False
            b_change=True
            e.radius=60

            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=e.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=e.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=e.path
            


    elif f_change :
        f.changestonesize()
        if key_left :
            f_change=False
            e_change=True
            f.radius=60
        if key_up :
            f_change=False
            c_change=True
            f.radius=60

            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=f.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=f.path
        if key_enter_times==3 :
            if P3_determine.path == 'snu.png' :
                P3_determine.path=f.path
            


    a.drawstone()        
    b.drawstone()
    c.drawstone()
    d.drawstone()
    e.drawstone()
    f.drawstone()


    if key_enter_times>=1 :
        P1_determine.drawstone()
    if key_enter_times>=2 :
        P2_determine.drawstone()
    if key_enter_times>=3 :
        P3_determine.drawstone()

    if key_enter_times == 4 :
        text_select = text_old.Text('Press \'Enter\' to determine', 75, 'white')
        text_old.show(text_select, (640, 460), screen)
        a.center=(10000,10000)
        b.center=(10000,10000)
        c.center=(10000,10000)
        d.center=(10000,10000)
        e.center=(10000,10000)
        f.center=(10000,10000)

    key_right=False
    key_left=False
    key_up=False
    key_down=False


def drawstones2P():
    global a,b,c,d,e,f, key_enter, a_change, b_change, c_change, d_change, e_change, f_change, key_left, key_right, key_down, key_up,key_enter, P1_determine, P2_determine, key_enter_times
    
    text_stone=text_old.Text('Stone Select', 100, 'white')
    text_old.show(text_stone, (640, 100), screen)

    text_1P = text_old.Text('1P : ', 75, 'white')
    text_2P = text_old.Text('2P : ', 75, 'white')

    text_old.show(text_1P, (360, 225), screen)
    text_old.show(text_2P, (820, 225), screen)
#키설명
    pygame.draw.rect(screen, '#aaaaaa', (75, 575, 185, 110), border_radius=30)
    text_old.show(esc, (167.5, 600), screen)
    text_old.show(enter, (167.5, 625), screen)
    text_old.show(z, (167.5, 650), screen)
#끝
    if a_change :
        a.changestonesize()
        if key_right :
            a_change=False
            b_change=True
            a.radius=60
        if key_down :
            a_change=False
            d_change=True
            a.radius=60
            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=a.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=a.path

    elif b_change :
        b.changestonesize()
        if key_left :
            b_change=False
            a_change=True
            b.radius=60
        if key_right :
            b_change=False
            c_change=True
            b.radius=60            
        if key_down :
            b_change=False
            e_change=True
            b.radius=60
            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=b.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=b.path

    elif c_change :
        c.changestonesize()
        if key_left :
            c_change=False
            b_change=True
            c.radius=60
        if key_down :
            c_change=False
            f_change=True
            c.radius=60
            
            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=c.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=c.path


    elif d_change :
        d.changestonesize()
        if key_right :
            d_change=False
            e_change=True
            d.radius=60
        if key_up :
            d_change=False
            a_change=True
            d.radius=60

            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=d.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=d.path

    elif e_change :
        e.changestonesize()
        if key_left :
            e_change=False
            d_change=True
            e.radius=60
        if key_right :
            e_change=False
            f_change=True
            e.radius=60
        if key_up :
            e_change=False
            b_change=True
            e.radius=60

            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=e.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=e.path       


    elif f_change :
        f.changestonesize()
        if key_left :
            f_change=False
            e_change=True
            f.radius=60
        if key_up :
            f_change=False
            c_change=True
            f.radius=60

            
        if key_enter_times==1 :
            if P1_determine.path =='snu.png' :
                P1_determine.path=f.path
        if key_enter_times==2 :
            if P2_determine.path == 'snu.png' :
                P2_determine.path=f.path
        if key_enter_times == 3 :
            text_select = text_old.Text('Press \'Enter\' to determine', 75, 'white')
            text_old.show(text_select, (640, 460), screen)
            a.radius=1
            b.radius=1
            c.radius=1
            d.radius=1
            e.radius=1
            f.radius=1
    

    a.drawstone()        
    b.drawstone()
    c.drawstone()
    d.drawstone()
    e.drawstone()
    f.drawstone()


    if key_enter_times>=1 :
        P1_determine.drawstone()
    if key_enter_times>=2 :
        P2_determine.drawstone()
    
    if key_enter_times == 3 :
        text_select = text_old.Text('Press \'Enter\' to determine', 75, 'white')
        text_old.show(text_select, (640, 460), screen)
        a.center=(10000,10000)
        b.center=(10000,10000)
        c.center=(10000,10000)
        d.center=(10000,10000)
        e.center=(10000,10000)
        f.center=(10000,10000)
    key_right=False
    key_left=False
    key_up=False
    key_down=False
















text_a = text_old.Text('Number of Players',50,'black')
text_b = text_old.Text(str(playernumber),200,'black')
text_c = text_old.Text('Press Enter to select', 45, 'black')

text_d = text_old.Text('Number of Sets',50,'black')
text_e = text_old.Text(str(bestoutof),200,'black')
text_f = text_old.Text('Press Enter to select', 45, 'black')
a_=[[250, 250], [200, 325], [250, 400]]
b_=[[390, 250], [440, 325], [390, 400]]
asize_0=a_[0][1]+1
asize_1=a_[1][0]+1
asize_2=a_[2][1]-1 
default_a0=a_[0][1]
default_a2=a_[2][1]
default_a1=a_[1][0]
bsize_0=b_[0][1]+1
bsize_1=b_[1][0]-1
bsize_2=b_[2][1]-1 
default_b0=b_[0][1]
default_b2=b_[2][1]
default_b1=b_[1][0]

#text_old.show(text_b, (320, 325), screen)
#text_old.show(text_e, (960, 325), screen)
c_=[[890, 250],[840, 325],[890,400]]
d_=[[1030,250],[1080, 325],[1030,400]]
csize_0=c_[0][1]+1
csize_1=c_[1][0]+1
csize_2=c_[2][1]-1 
default_c0=c_[0][1]
default_c2=c_[2][1]
default_c1=c_[1][0]
dsize_0=d_[0][1]+1
dsize_1=d_[1][0]-1
dsize_2=d_[2][1]-1 
default_d0=d_[0][1]
default_d2=d_[2][1]
default_d1=d_[1][0]



def changepolygonsize1():
    global c_, d_, csize_0, csize_2, default_c0, default_c2, csize_1, default_c1, dsize_0, dsize_1, dsize_2, default_d1, default_d2, default_d3
    for i in range(0,3) :
        
        if i ==0 :
            if csize_0 >= c_[i][1]: 
                csize_0=c_[i][1]
                c_[i][1] -= 1
                if c_[i][1] <default_c0-20 :
                    csize_0=c_[i][1]-1
            elif csize_0<=c_[i][1] :
                csize_0=c_[i][1]
                c_[i][1]+=1
                if c_[i][1]>default_c0+20 :
                    csize_0=c_[i][1]+1
        elif i ==2 :
            if csize_2 >= c_[i][1]: 
                csize_2=c_[i][1]
                c_[i][1] -= 1
                if c_[i][1] <default_c2-20 :
                    csize_2=c_[i][1]-1
            elif csize_2<=c_[i][1] :
                csize_2=c_[i][1]
                c_[i][1]+=1
                if c_[i][1]>default_c2+20 :
                    csize_2=c_[i][1]+1                
        else :
            if csize_1 >= c_[i][0]: 
                csize_1=c_[i][0]
                c_[i][0] -= 1
                if c_[i][0] <default_c1-20 :
                    csize_1=c_[i][0]-1
            elif csize_1<=c_[i][0] :
                csize_1=c_[i][0]
                c_[i][0]+=1
                if c_[i][0]>default_c1+20 :
                    csize_1=c_[i][0]+1
            
    for i in range(0,3) :
            
        if i ==0 :
            if dsize_0 >= d_[i][1]: 
                dsize_0=d_[i][1]
                d_[i][1] -= 1
                if d_[i][1] <default_d0-20 :
                    dsize_0=d_[i][1]-1
            elif dsize_0<=d_[i][1] :
                dsize_0=d_[i][1]
                d_[i][1]+=1
                if d_[i][1]>default_d0+20 :
                    dsize_0=d_[i][1]+1
        elif i ==2 :
            if dsize_2 >= d_[i][1]: 
                dsize_2=d_[i][1]
                d_[i][1] -= 1
                if d_[i][1] <default_d2-20 :
                    dsize_2=d_[i][1]-1
            elif dsize_2<=d_[i][1] :
                dsize_=d_[i][1]
                d_[i][1]+=1
                if d_[i][1]>default_d2+20 :
                    dsize_2=d_[i][1]+1                
        else :
            if dsize_1 >= d_[i][0]: 
                dsize_1=d_[i][0]
                d_[i][0] -= 1
                if d_[i][0] <default_d1-20 :
                    dsize_1=d_[i][0]-1
            elif dsize_1<=d_[i][0] :
                dsize_1=d_[i][0]
                d_[i][0]+=1
                if d_[i][0]>default_d1+20 :
                    dsize_1=d_[i][0]+1
                    
    pygame.draw.polygon(screen, 'black', c_)
    pygame.draw.polygon(screen, 'black', d_)



def changepolygonsize():
    global a_, b_, asize_0, asize_2, default_a0, default_a2, asize_1, default_a1, bsize_0, bsize_1, bsize_2, default_b1, default_b2, default_b3
    for i in range(0,3) :
        
        if i ==0 :
            if asize_0 >= a_[i][1]: 
                asize_0=a_[i][1]
                a_[i][1] -= 1
                if a_[i][1] <default_a0-20 :
                    asize_0=a_[i][1]-1
            elif asize_0<=a_[i][1] :
                asize_0=a_[i][1]
                a_[i][1]+=1
                if a_[i][1]>default_a0+20 :
                    asize_0=a_[i][1]+1
        elif i ==2 :
            if asize_2 >= a_[i][1]: 
                asize_2=a_[i][1]
                a_[i][1] -= 1
                if a_[i][1] <default_a2-20 :
                    asize_2=a_[i][1]-1
            elif asize_2<=a_[i][1] :
                asize_2=a_[i][1]
                a_[i][1]+=1
                if a_[i][1]>default_a2+20 :
                    asize_2=a_[i][1]+1                
        else :
            if asize_1 >= a_[i][0]: 
                asize_1=a_[i][0]
                a_[i][0] -= 1
                if a_[i][0] <default_a1-20 :
                    asize_1=a_[i][0]-1
            elif asize_1<=a_[i][0] :
                asize_1=a_[i][0]
                a_[i][0]+=1
                if a_[i][0]>default_a1+20 :
                    asize_1=a_[i][0]+1
            
    for i in range(0,3) :
            
        if i ==0 :
            if bsize_0 >= b_[i][1]: 
                bsize_0=b_[i][1]
                b_[i][1] -= 1
                if b_[i][1] <default_b0-20 :
                    bsize_0=b_[i][1]-1
            elif bsize_0<=b_[i][1] :
                bsize_0=b_[i][1]
                b_[i][1]+=1
                if b_[i][1]>default_b0+20 :
                    bsize_0=b_[i][1]+1
        elif i ==2 :
            if bsize_2 >= b_[i][1]: 
                bsize_2=b_[i][1]
                b_[i][1] -= 1
                if b_[i][1] <default_b2-20 :
                    bsize_2=b_[i][1]-1
            elif bsize_2<=b_[i][1] :
                bsize_2=b_[i][1]
                b_[i][1]+=1
                if b_[i][1]>default_b2+20 :
                    bsize_2=b_[i][1]+1                
        else :
            if bsize_1 >= b_[i][0]: 
                bsize_1=b_[i][0]
                b_[i][0] -= 1
                if b_[i][0] <default_b1-20 :
                    bsize_1=b_[i][0]-1
            elif bsize_1<=b_[i][0] :
                bsize_1=b_[i][0]
                b_[i][0]+=1
                if b_[i][0]>default_b1+20 :
                    bsize_1=b_[i][0]+1
                    
    pygame.draw.polygon(screen, 'black', a_)
    pygame.draw.polygon(screen, 'black', b_)

#키설명 나타내기
esc=text_old.Text('esc : return', 30, 'black')
enter=text_old.Text('enter : select', 30, 'black')
z=text_old.Text('z : revert', 30, 'black')

# 플레이어 수 선택
def chooseplayer():
    global esc, enter, key_left,key_right, playernumber, key_enter, text_a, text_b, text_c, text_d, text_e, text_f

    if key_left:
        playernumber-=1
    elif key_right:
        playernumber+=1
    if playernumber >= 5 :
        playernumber=4
    if playernumber <=1 :
        playernumber=2

    key_left=False
    key_right=False
    


    
    pygame.draw.rect(screen, '#aaaaaa', (37.5, 115, 575, 430), border_radius=30)
    pygame.draw.rect(screen, '#aaaaaa', (675, 115, 575, 430), border_radius=30)

#옵션 키 나타내기
    pygame.draw.rect(screen, '#aaaaaa', (75, 575, 185, 85), border_radius=30)
    text_old.show(esc, (167.5, 600), screen)
    text_old.show(enter, (167.5, 625), screen)
#끝
    
    text_a.changetextsize()
    text_old.show(text_a,(320,165),screen)

    

    changepolygonsize()
    pygame.draw.polygon(screen, 'black', [[1030,250],[1080, 325],[1030,400]])
    pygame.draw.polygon(screen, 'black', [[890, 250],[840, 325],[890,400]])
    text_b.text=str(playernumber)
    text_b.changetextsize()
    text_old.show(text_b, (320, 325), screen)

    text_c.changetextsize()
    text_old.show(text_c, (320, 490), screen)

 
    text_old.show(text_d,(960,165),screen)


    text_old.show(text_e, (960, 325), screen)
    
    text_old.show(text_f, (960, 490), screen)

    
    key_enter=False
#몇세트 플레이할건지 선택
    
key_enter1=False
def bestoutof__():
    global bestoutof,key_enter1, key_left,key_right, key_enter, text_a, text_b, text_c, text_d, text_e, text_f
    if key_left:
        bestoutof-=1
    elif key_right:
        bestoutof+=1
        
    if bestoutof >= 5 :
        bestoutof=4
    if bestoutof <=0 :
        bestoutof=1

#옵션 나타내기        
    pygame.draw.rect(screen, '#aaaaaa', (75, 575, 185, 85), border_radius=30)
    text_old.show(esc, (167.5, 600), screen)
    text_old.show(enter, (167.5, 625), screen)
#끝
    
    key_left=False
    key_right=False
    pygame.draw.rect(screen, '#aaaaaa', (37.5, 115, 575, 430), border_radius=30)
    pygame.draw.rect(screen, '#aaaaaa', (675, 115, 575, 430), border_radius=30)

    text_a = text_old.Text('Number of Players',50,'black')
    text_old.show(text_a,(320,165),screen)

    pygame.draw.polygon(screen, 'black', ((250, 250), (200, 325), (250, 400)))
    pygame.draw.polygon(screen, 'black', ((390, 250), (440, 325), (390, 400)))

    changepolygonsize1()

    text_b = text_old.Text(str(playernumber),200,'black')
    text_old.show(text_b, (320, 325), screen)

    text_c = text_old.Text('Press Enter to select', 45, 'black')
    text_old.show(text_c, (320, 490), screen)

    text_d.changetextsize()
    text_old.show(text_d,(960,165),screen)

    text_e.text=str(bestoutof)
    text_e.changetextsize()
    text_old.show(text_e, (960, 325), screen)


    text_f.changetextsize()
    text_old.show(text_f, (960, 490), screen)

def determine():
    text_a = text_old.Text('Number of Players',50,'black')
    text_b = text_old.Text(str(playernumber),200,'black')
    text_c = text_old.Text('Press Enter to select', 45, 'black')

    text_d = text_old.Text('Number of Sets',50,'black')
    text_e = text_old.Text(str(bestoutof),200,'black')
    text_f = text_old.Text('Press Enter to select', 45, 'black')
    pygame.draw.rect(screen, '#aaaaaa', (37.5, 115, 575, 430), border_radius=30)
    pygame.draw.rect(screen, '#aaaaaa', (675, 115, 575, 430), border_radius=30)

    pygame.draw.polygon(screen, 'black', [[1030,250],[1080, 325],[1030,400]])
    pygame.draw.polygon(screen, 'black', [[890, 250],[840, 325],[890,400]])

    text_old.show(text_a,(320,165),screen)
    text_old.show(text_b, (320, 325), screen)
    text_old.show(text_c, (320, 490), screen)
    text_old.show(text_d,(960,165),screen)
    text_old.show(text_e, (960, 325), screen)
    text_old.show(text_f, (960, 490), screen)

#키설명
    pygame.draw.rect(screen, '#aaaaaa', (75, 575, 185, 85), border_radius=30)
    text_old.show(esc, (167.5, 600), screen)
    text_old.show(enter, (167.5, 625), screen)
# 끝
    a_=[[250, 250], [200, 325], [250, 400]]
    b_=[[390, 250], [440, 325], [390, 400]]
    pygame.draw.polygon(screen, 'black', a_)
    pygame.draw.polygon(screen, 'black', b_)
    
    if key_enter1 :
        text_g=text_old.Text('Press Enter to determine', 65, 'white')
        text_old.show(text_g, (640, 595), screen)
    key_enter=False

def display():
    screen.fill('black')
    
# clock=pygame.time.Clock()
# # Run until the user asks to quit
# running = True
# while running:
#     clock.tick(60) # set FPS    
#     display()
#     # Main Event Loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 key_right=True
#             if event.key == pygame.K_LEFT:
#                 key_left = True
#             if event.key == pygame.K_RETURN:
#                 key_enter=True
#                 key_enter1=True
#                 text_a.size=60
#                 text_a.size1=text_a.size-1
#                 text_a.size2=text_a.size
#                 text_b.size=200
#                 text_b.size1=text_b.size-1
#                 text_b.size2=text_b.size
#                 text_c.size=45
#                 text_c.size1=text_c.size-1
#                 text_c.size2=text_c.size
#                 a_=[[250, 250], [200, 325], [250, 400]]
#                 b_=[[390, 250], [440, 325], [390, 400]]
#                 asize_0=a_[0][1]+1
#                 asize_1=a_[1][0]+1
#                 asize_2=a_[2][1]-1 
#                 default_a0=a_[0][1]
#                 default_a2=a_[2][1]
#                 default_a1=a_[1][0]
#                 bsize_0=b_[0][1]+1
#                 bsize_1=b_[1][0]-1
#                 bsize_2=b_[2][1]-1 
#                 default_b0=b_[0][1]
#                 default_b2=b_[2][1]
#                 default_b1=b_[1][0]
                
#                 if idx==4:key_enter_times+=1
#                 idx+=1
#                 if idx==5:idx=4
#             if event.key==pygame.K_ESCAPE:
#                 idx-=1
#             if event.key==pygame.K_z :
#                 key_enter_times-=1
#                 if key_enter_times==0:
#                     P1_determine.path='snu.png'
#                     P2_determine.path='snu.png'
#                     P3_determine.path='snu.png'
#                     P4_determine.path='snu.png'                    
#                 if key_enter_times ==1 :
#                     P2_determine.path='snu.png'
#                     P3_determine.path='snu.png'
#                     P4_determine.path='snu.png'
#                 if key_enter_times==2 :
#                     P3_determine.path='snu.png'
#                     P4_determine.path='snu.png'
#                 if key_enter_times==3:
#                     P4_determine.path='snu.png'
                    
#             if event.key == pygame.K_DOWN:
#                 key_down=True
#             if event.key == pygame.K_UP:
#                 key_up = True
#     if idx==1 :
#         chooseplayer()
#     if idx==2:
#         bestoutof__()
#     if idx==3 :
#         determine()
#     if idx==4 :
#         if playernumber==2:
#             P1_determine.center=(480,225)
#             P2_determine.center=(940,225)
#             drawstones2P()
#         if playernumber==3:
#             P1_determine.center=(250,225)
#             P2_determine.center=(700,225)
#             P3_determine.center=(1150,225)
#             drawstones3P()
#         if playernumber==4:
#             drawstones4P()

        
#     # Update the screen
#     pygame.display.flip()

# pygame.quit()
