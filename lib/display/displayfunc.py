import lib
import res

def objects(object_list:list,screen):
    n=len(object_list)
    Objects=[]
    for i in range(n):
        Objects.append(lib.display.images.Image(object_list[i].path,
                                               object_list[i].position,
                                               tuple(item*object_list[i].size_mul_factor for item in res.loadresourcesize.size(object_list[i].path))))
    for item in Objects:
        lib.display.images.draw(item,screen)
    return Objects
class image:
    def __init__(self,path:str,position:tuple,size_mul_factor:int=1,button=False):
        self.path=path
        self.position=position
        self.size_mul_factor=size_mul_factor
        self.button=button