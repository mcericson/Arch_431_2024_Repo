def setup():
    size(2000,2000)
    
def draw():
    background(255)
    x = mouse_x
    y = mouse_y
    line(0,0,mouse_x, mouse_y)