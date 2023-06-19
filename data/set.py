from res import ls
data_path='data/settings.txt'

# Settings
settings={
    'FPS': 60,
    'Friction_coefficient': 1.5,
    'Elastic_modulus': 0.7,
    'Screen_size': (1280,720),
    'Volume_song':50,
    'Volume_effect':50
}
l=len(settings)


try:
    # Load settings if it exists.
    settings = ls.load(data_path)
    if len(settings)!=l:ls.init(data_path,settings)
except:
    # Initialize settings if no saved settings.
    ls.init(data_path,settings)

def find(key:str):
    return settings[key]
def change(key:str,value):
    global settings
    settings[key]=value
    ls.init(data_path,settings)
    # for line in fileinput.input(data_path,inplace=True):
    #     if line.split()[0]==key:
    #         print(f'{key} {value}')
    #     else:print(f'{line}',end='')