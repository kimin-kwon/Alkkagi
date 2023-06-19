# import os
# file_list=os.listdir('Resources')
# save_path='data/resourcesize.txt'
        
# def size(file_name):
#     file_index=file_list.index(file_name)
#     with open(save_path,'r') as li:
#         for _ in range(file_index):li.readline()
#         return tuple(list(map(int,li.readline().split()[1:])))
    
from res import ls
save_path='data/resourcesize.txt'
def size(file_name:str):
    resource_size=ls.load(save_path)
    return resource_size[file_name]