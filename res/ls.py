import json
def load(path:str):
    with open(path) as load_file:
        settings=json.load(load_file)
    return settings
def init(path:str,file:dict):
    with open(path,'w') as store_file:
        json.dump(file,store_file)