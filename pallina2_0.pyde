x=80
y=80
xrett1=0
xrett2=0
altezzarett2=0
altezzarett1=375
versx=1
versy=1
raggio=50
punti1=0
punti2=0
def setup ():
     size(600,400)
     
def draw():
    global versx,versy,xpall,ypall,raggio,x,y,xrett1,xrett2,altezzarett1,punti1,punti2
    background(0, 0, 0)
    ellipse (x,y,20,20)
    x=x+(3*versx)
    y=y+(3*versy)
    if y+25>altezzarett1 and x>=xrett1 and x<=xrett1+80:
        versy*=-1
        fill(random(255),random(255),random(255))
    if y+25>altezzarett2 and  x>=xrett2 and x<=xrett2+80:
        versy*=-1
        fill(random(255),random(255),random(255))
    if x>width:
        versx*=-1
    if y>height:
        versy*=-1
    if x<0:
        versx*=-1
        punti2=punti2+10
    if y<0:
        versy*=-1
        punti1=punti1+10
  
    
    rect(xrett1,altezzarett1,80,25)
    rect(xrett2,altezzarett2,80,25)

def keyPressed():
    global xrett1, versx,xrett2, testo1, testo2
    if keyCode == LEFT:
        xrett1=xrett1-25
    if keyCode == RIGHT:
        xrett1=xrett1+25
    if keyCode == 65:
        xrett2=xrett2-25
    if keyCode == 83:
        xrett2=xrett2+25
    if xrett2>=width-50:
        xrett2=xrett2-50
    if xrett1>=width-50:
        xrett1=xrett1-50
    if xrett1<0:
        xrett1*=-1
    if xrett2<0:
        xrett2*=-1
    fill(white)
    text (punti1,50,30)
    fill(white)
    text(punti2,40,60)
