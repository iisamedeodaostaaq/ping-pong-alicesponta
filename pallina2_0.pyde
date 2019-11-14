## Prof. Inserire QUI il significato di queste variabili globali
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
     #Decido la grandezza della finestra di gioco
     size(600,400)
     
def draw():
    global versx,versy,xpall,ypall,raggio,x,y,xrett1,xrett2,altezzarett1,punti1,punti2,versx, versy
    background(0, 0, 0)
    fill(255,255,255)
    ellipse (x,y,20,20)
## Prof. Si poteva rendere anche il diametro della pallina una costante da riferire poi nel codice
    #X ed Y daranno il verso alla pallina 
## Prof.  In effetti rappresentano le coordinate della pallina
    x=x+(3*versx)
    y=y+(3*versy)
    #Se la pallina tocca la prima racchetta 
    if y>=altezzarett1-(20/2) and (x+(20/2)>xrett1 and x-(20/2)<xrett1+80): 
        #Cambieremo il verso della pallina
        versy*=-1
    #Se la pallina tocca la seconda racchetta 
    if y<=altezzarett2+35 and (x+(20/2)>xrett2 and x-(20/2)<xrett2+80):
       #Cambieremo il verso della pallina
       versy*=-1
    #Se la pallina tocca il bordo
    if x>width or x<=0:
        #Cambieremo il verso della pallina
        versx*=-1
    if y>height or y<=0:
        #Cambieremo il verso della pallina
        versy*=-1
    #Se la pallina tocca il bordo superiore aumento i punti del giocatore 1
    if y<0:
        punti1=punti1+10
    #Se la pallina tocca il bordo inferiore aumento i punti del giocatore 2
    if y>=height:
        punti2=punti2+10
    #Eseguo un controllo per far si che il rettangolo non esca dalla finestra
## Prof. La racchetta è larga 80. Se supero il limite, semplicemebte non incremento la posizione della racchetta
## Prof. Come è stato fatto, crea un rimbalzo della racchetta sui bordi
    if xrett2>=width-50:
        xrett2=xrett2-50
    if xrett1>=width-50:
        xrett1=xrett1-50
## Prof. ??? non capisco questa inversione dell'ascissa delle racchette
    if xrett1<0:
        xrett1*=-1
    if xrett2<0:
        xrett2*=-1
    #Conteggio punti per il risultato finale
    if punti1>=100:
        textSize(50)
        fill(255,0,0)
        text("Giocatore 1 vince", 100,200)
        delay(1000)
    if punti2>=100:
         textSize(50)
         fill(0,0,255)
         text("Giocatore 2 vince", 100,200)
         delay(1000)
    #Mostro i punti a video
    fill (255 )
    textSize ( 30 )
    fill(0,0,255)
    text ( punti2, 0,30 )
    fill (255 )
    textSize ( 30 )
    fill(255,0,0)
    text ( punti1, 10,400 )
    #Coloro i rettangoli con due colori diversi
    fill(255,0,0)
    rect(xrett1,altezzarett1,80,25)
    fill(0,0,255)
    rect(xrett2,altezzarett2,80,25)

def keyPressed():
    global xrett1, versx,xrett2
    #Se premo la freccia sinistra decremento la prosizione della racchetta in modo tale da farla muovere verso sinistra
    if keyCode == LEFT:
        xrett1=xrett1-25
    #Se premo la freccia destra incremento la prosizione della racchetta in modo tale da farla muovere verso destra
    if keyCode == RIGHT:
        xrett1=xrett1+25
    #Se premo il  tasto A incremento la decremento della racchetta in modo tale da farla muovere verso sinistra
    if keyCode == 65:
        xrett2=xrett2-25
     #Se premo il tasto S incremento la prosizione della racchetta in modo tale da farla muovere verso destra
    if keyCode == 83:
           xrett2=xrett2+25
