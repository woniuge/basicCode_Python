
'''
def add_end(L=[]):
    L.append('END')
    return L
'''

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
