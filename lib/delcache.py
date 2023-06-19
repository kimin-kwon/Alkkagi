import os
def delete_cache():
    for item in os.listdir('Cache/image/'):
        os.remove('Cache/image/'+item)