import pygame
import data
import res
import os
import importlib
import pip
from lib import delcache
from datetime import datetime
from lib.components import rock
import hm
try:
    from PIL import Image
except:
    pip.main(['install','pillow'])
    
# Check if necessary folders exist
current_directory=os.getcwd()
if not os.path.exists(current_directory+'/Screenshots'):
    os.mkdir(current_directory+'/Screenshots')

# Set game values
elastic_modulus = float(data.set.find('Elastic_modulus')) # Elastic Modulus
set_fps = int(data.set.find('FPS'))
friction_coefficient = float(data.set.find('Friction_coefficient'))

def update_settings():
    global elastic_modulus,set_fps,friction_coefficient
    elastic_modulus = float(data.set.find('Elastic_modulus')) # Elastic Modulus
    set_fps = int(data.set.find('FPS'))
    friction_coefficient = float(data.set.find('Friction_coefficient'))
    
# initialize
pygame.init()
screen_width, screen_height = data.set.find('Screen_size') # Screen size
screen = pygame.display.set_mode((screen_width, screen_height),pygame.DOUBLEBUF,32)
pygame.display.set_caption("Alkkagi") # Game Title
clock=pygame.time.Clock()
pygame.mouse.set_pos([i/2 for i in data.set.find('Screen_size')])
delcache.delete_cache()
hm.idx=0
hm.screen=screen

# Save images' Size
file_list=os.listdir('Resources')
resource_save_path='data/resourcesize.txt'
resource_size=dict()
for item in file_list:
    if os.path.splitext(item)[-1]=='.png':
        img_size=pygame.image.load('Resources/'+item).get_size()
        resource_size[item]=img_size
res.ls.init(resource_save_path,resource_size)
del file_list,resource_size,item,resource_save_path,img_size

from lib.display import input,pages

keydown = True
# Start the page before detection         
input.inputdetect()
page='Home'
places=[]
outbound_list=[]

# Manage set scores
game_number=0
sets=2
set_score=[]
idx_changed=True

# Sound mixer settings
# --------------------------------------------------
volume1=pages.settings.volume1
volume2=pages.settings.volume2
channel0=pygame.mixer.Channel(0)
channel0.set_volume(volume1)
sound0=pygame.mixer.Sound('Resources/background.mp3')
# --------------------------------------------------
music_played=False

# Manage display
def display():
    # Manage Pages
    global keydown,places,outbound_list,game_number,sets,set_score,idx_changed
    if page=='Home':pages.home.Screen(screen)
    elif page in['Settings','Settings_ingame']:
        pages.settings.Screen(screen)
    elif page=='Quit':
        pages.quit.Screen(screen)
    elif page=='Game':
        places=[]
        if pages.end.set_score_reset:
            set_score=[]
            pages.end.set_score=[0 for _ in range(pages.game.players)]
            pages.end.set_score_reset=False
        pages.end.gamerecordsaved=False
        outbound_list=[pages.game.outbound_1,pages.game.outbound_2,pages.game.outbound_3,pages.game.outbound_4]
        for i in range(4):
            if outbound_list[i]==3 and not i in places:
                places.append(i)
        
        if len(set_score)!=0:pages.game.set_score=set_score
        pages.game.Screen(screen)
        # pages.end.Screen(screen)
    elif page == 'End':
        
        # Show winner
        if len(places)!=pages.game.players:
            for i in range(4):
                if not (i in places):
                    places.append(i)
                    break
            game_number+=1
            if game_number>sets:
                game_number=1
            pages.end.game_number=game_number
            
            # Set score
            if len(set_score)==0:
                set_score=[0 for _ in range(pages.game.players)]
            set_score_list=[10,7,4,1]
            for i in range(pages.game.players):
                set_score[places[::-1][i]]+=set_score_list[i]
            # print(pages.end.game_number,pages.end.set_score)
            
        pages.end.set_score=set_score
        pages.end.sets=sets
        pages.end.players=pages.game.players
        pages.end.names=pages.game.player_name
        pages.end.places=places[::-1]
        pages.end.winner=places[-1]
        pages.end.score=[3-i for i in outbound_list]
        pages.end.clicked_object
        
        
        
        
        pages.end.Screen(screen)
    elif page == 'Pause':
        pages.pause.Screen(screen)
    elif page == 'Settings_ingame':
        pages.settings.Screen(screen)
    elif page == 'Settings_insetting':
        pages.settings.Screen(screen)
    elif page == 'Quit_ingame':
        pages.quit_ingame.Screen(screen)
    elif page == 'Idle':
        if idx_changed:
            hm.idx=1
            idx_changed=False
    elif page == 'Set_name':
        pages.set_name.Screen(screen)
    if page!='Idle' and page!='Set_name':
        idx_changed=True
            
    keydown = False

def gamereset():
    importlib.reload(pages.game)
    # # Set stone picture
    # pages.game.player_image_path=[
    #     hm.P1_determine.path,
    #     hm.P2_determine.path,
    #     hm.P3_determine.path,
    #     hm.P4_determine.path
    # ]
def idlereset():
    importlib.reload(hm)

# Set page
def page_set():
    global page,running
    if page == 'Home':
        page = pages.home.page()
    elif page == 'Settings':
        page = pages.settings.page()
    elif page == 'Quit':
        page = pages.quit.page()
        if page=='End game':running=False
    elif page == 'Game':
        page = pages.game.page()
        # page == pages.end.page()
    elif page == 'End':
        page = pages.end.page()
        if page=='Game':
            gamereset()
    elif page == 'Pause':
        page = pages.pause.page()
    elif page == 'Settings_ingame':
        page = pages.settings.page_ingame()
    elif page == 'Quit_ingame':
        page = pages.quit_ingame.page()
        if page=='Home':
            delcache.delete_cache()
    elif page == 'Set_name':
        page = pages.set_name.page()
        if page=='Game':
            gamereset()
            pages.game.player_name=pages.set_name.player_name
        if page!='Set_name':
            importlib.reload(pages.set_name)
        
    

    
n=0 # Variable for displaying current fps

# Run until the user asks to quit
running = True
while running:
    # Change Volume
    volume1=pages.settings.volume1 # Music Volume
    volume2=pages.settings.volume2 # SFX Volume
    channel0.set_volume(volume1*0.01)
    rock.channel1.set_volume(volume2*0.01)
    pages.game.channel2.set_volume(volume2*0.01)
    pages.end.channel3.set_volume(volume2*0.01)
    
    # Real game
    clock.tick(set_fps)
    if page=='Idle':screen.fill('black')
    if pages.end.idlereset:
        idlereset()
        pages.end.idlereset=False
    if pages.quit_ingame.idlereset:
        idlereset()
        pages.quit_ingame.idlereset=False
        
    if page in['Home','Idle','Settings','Quit','Set_name'] and not music_played:
        channel0.play(sound0)
        music_played=True
    elif not page in['Home','Idle','Settings','Quit','Set_name']:
        channel0.stop()
        music_played=False
    
    # Main Event Loop
    for event in pygame.event.get():
        input.inputdetect() # Detect inputs.
        if event.type == pygame.QUIT: # If user clicked close button
            running = False
            delcache.delete_cache()
        elif event.type == pygame.KEYDOWN and not keydown:
            keydown = True
            page_set()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input.mousedown=True
            page_set()
            
        elif event.type == pygame.MOUSEBUTTONUP:
            input.mouseup=True
            page_set()
            
        if event.type==pygame.KEYDOWN:
            pages.set_name.key_pressed=event.unicode
            input.keydown=True
            if event.key==pygame.K_F12:
                dateandtime=datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                pygame.image.save(screen,'Screenshots/'+dateandtime+'.png')
            
        if event.type==pygame.KEYUP:
            input.keyup=True
        
            
        # From here, the code manages variables from hm.py
        
        # -------------------------------------------------
        if page=='Idle':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    hm.key_right=True
                if event.key == pygame.K_LEFT:
                    hm.key_left = True
                if event.key == pygame.K_RETURN:
                    hm.key_enter=True
                    hm.key_enter1=True
                    hm.text_a.size=60
                    hm.text_a.size1=hm.text_a.size-1
                    hm.text_a.size2=hm.text_a.size
                    hm.text_b.size=200
                    hm.text_b.size1=hm.text_b.size-1
                    hm.text_b.size2=hm.text_b.size
                    hm.text_c.size=45
                    hm.text_c.size1=hm.text_c.size-1
                    hm.text_c.size2=hm.text_c.size
                    hm.a_=[[250, 250], [200, 325], [250, 400]]
                    hm.b_=[[390, 250], [440, 325], [390, 400]]
                    hm.asize_0=hm.a_[0][1]+1
                    hm.asize_1=hm.a_[1][0]+1
                    hm.asize_2=hm.a_[2][1]-1 
                    hm.default_a0=hm.a_[0][1]
                    hm.default_a2=hm.a_[2][1]
                    hm.default_a1=hm.a_[1][0]
                    hm.bsize_0=hm.b_[0][1]+1
                    hm.bsize_1=hm.b_[1][0]-1
                    hm.bsize_2=hm.b_[2][1]-1 
                    hm.default_b0=hm.b_[0][1]
                    hm.default_b2=hm.b_[2][1]
                    hm.default_b1=hm.b_[1][0]
                    
                    if hm.idx==4:hm.key_enter_times+=1
                    hm.idx+=1
                    if hm.idx==5:hm.idx=4
                    if hm.key_enter_times==hm.playernumber+2:
                        page='Set_name'
                        importlib.reload(pages.set_name)
                if event.key==pygame.K_ESCAPE:
                    hm.idx-=1
                if event.key==pygame.K_z :
                    if hm.key_enter_times!=hm.playernumber+1:
                        hm.key_enter_times-=1
                    if hm.key_enter_times==0:
                        hm.P1_determine.path='snu.png'
                        hm.P2_determine.path='snu.png'
                        hm.P3_determine.path='snu.png'
                        hm.P4_determine.path='snu.png'                    
                    if hm.key_enter_times ==1 :
                        hm.P2_determine.path='snu.png'
                        hm.P3_determine.path='snu.png'
                        hm.P4_determine.path='snu.png'
                    if hm.key_enter_times==2 :
                        hm.P3_determine.path='snu.png'
                        hm.P4_determine.path='snu.png'
                    if hm.key_enter_times==3:
                        hm.P4_determine.path='snu.png'
                        
                if event.key == pygame.K_DOWN:
                    hm.key_down=True
                if event.key == pygame.K_UP:
                    hm.key_up = True
    if page=='Idle':
        if hm.idx==0:
            page='Home'
            idlereset()
        if hm.idx==1 :
            hm.chooseplayer()
        if hm.idx==2:
            hm.bestoutof__()
            sets=hm.bestoutof
        if hm.idx==3 :
            hm.determine()
        if hm.idx==4 :
            if hm.playernumber==2:
                hm.P1_determine.center=(480,225)
                hm.P2_determine.center=(940,225)
                hm.drawstones2P()
            if hm.playernumber==3:
                hm.P1_determine.center=(250,225)
                hm.P2_determine.center=(700,225)
                hm.P3_determine.center=(1150,225)
                hm.drawstones3P()
            if hm.playernumber==4:
                hm.drawstones4P()

    
    
    
            
    # ---------------------------------------------------
            
            
            
            
            
            
            
            
            
            
    if pages.game.end:
        page='End'
        pages.game.end=False
            
    # Handle quit game
    # if quit_i:
    #     running=False
    #     delcache.delete_cache()
    
    
    
    
    
    # Displaying FPS on screen
    
    # n+=1
    # current_fps=int(clock.get_fps())
    # n=0
    # cfps_text=text.Text(str(current_fps),50,(300,300))
    # text.show(cfps_text,screen)
    
    # # Logging fps
    # log_path='data/log/fps_log.txt'
    
    # logging.basicConfig(filename=log_path,format='%(message)s',level=logging.INFO)
    # logging.info(f'{clock.get_fps()}')
    
    
    display()
    update_settings()
    # Update the screen
    pygame.display.flip()

pygame.quit()
