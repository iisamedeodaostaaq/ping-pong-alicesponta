xposs=0
yposs=0
def setup():
    global xposs,yposs, varx,vary
    xposs=10
    yposs=100
    size (500,400)
    background (600)
    fill( 0,255,0)
    rect(100,50,100,100)
    fill (255, 255,255)
    rect (200, 50, 100, 100)
    fill(255,9,9)
    rect (300, 50, 100, 100)
    fill(255,0,0)
    rect(0,50,40,20)

def draw():
     global xposs,yposs
     xposs+=1
     yposs+=1
     background(600)
     ellipse (xposs,yposs,50,50)
     varx=xposs 
     vary=yposs
     if (var>400):
        xposs-=1
     if (vary>500):
        yposs=1


    
   

    
