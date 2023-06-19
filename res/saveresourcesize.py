# import pygame
# import os
# file_list=os.listdir('Resources')
# pygame.init()
# save_path='data/resourcesize.txt'
# with open('Trigger.txt','w') as trigger:
#     trigger.write('0')
# def save():
#     with open(save_path,'w') as li:
#         for item in file_list:
#             try: 
#                 img_size = pygame.image.load('Resources/'+item).get_size()
#                 li.write(item+f' {img_size[0]} {img_size[1]}\n')
#             except: 
#                 print(item)
#                 file_list.remove(item)
#     with open('Trigger.txt','w') as trigger:
#         trigger.write('1')
