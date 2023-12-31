from pprint import pprint

def add(x,y):
    def do_add():
        print("Adding", x, "&", y)
        return x + y
    return do_add
    
pprint(add(3, 6)())