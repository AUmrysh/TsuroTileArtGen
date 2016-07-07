wh = 600
qwh = wh/4
hwh = wh/2
twh = wh/3
tilerules = (((0,1),(2,3),(4,5),(6,7)),((0,1),(2,3),(4,6),(5,7)),((0,1),(2,3),(4,7),(5,6)),((0,1),(2,4),(3,6),(5,7)),((0,1),(2,4),(3,7),(5,6)),((0,1),(2,5),(3,6),(4,7)),((0,1),(2,5),(3,7),(4,6)),((0,1),(2,6),(3,4),(5,7)),((0,1),(2,6),(3,5),(4,7)),((0,1),(2,6),(3,7),(4,5)),((0,1),(2,7),(3,4),(5,6)),((0,1),(2,7),(3,5),(4,6)),((0,1),(2,7),(3,6),(4,5)),((0,2),(1,3),(4,6),(5,7)),((0,2),(1,3),(4,7),(5,6)),((0,2),(1,4),(3,6),(5,7)),((0,2),(1,4),(3,7),(5,6)),((0,2),(1,5),(3,6),(4,7)),((0,2),(1,5),(3,7),(4,6)),((0,2),(1,6),(3,4),(5,7)),((0,2),(1,6),(3,5),(4,7)),((0,2),(1,7),(3,4),(5,6)),((0,2),(1,7),(3,5),(4,6)),((0,3),(1,2),(4,7),(5,6)),((0,3),(1,4),(2,6),(5,7)),((0,3),(1,4),(2,7),(5,6)),((0,3),(1,5),(2,6),(4,7)),((0,3),(1,6),(2,5),(4,7)),((0,4),(1,2),(3,6),(5,7)),((0,4),(1,2),(3,7),(5,6)),((0,4),(1,3),(2,6),(5,7)),((0,4),(1,5),(2,6),(3,7)),((0,4),(1,5),(2,7),(3,6)),((0,5),(1,4),(2,7),(3,6)),((0,7),(1,2),(3,4),(5,6)))
tileindices = ((twh, wh), (2*twh, wh), (wh, 2*twh), (wh, twh), (2*twh, 0), (twh, 0), (0, twh), (0, 2*twh))

def settings():
    size(wh, wh)

def draw():
    noFill()
    strokeWeight(20)
    
    def renderconnection(p1,p2):
        p1x = tileindices[p1][0]
        p1y = tileindices[p1][1]
        p2x = tileindices[p2][0]
        p2y = tileindices[p2][1]
        
        #loops, same side
        if int(p1/2) == int(p2/2):
            #print("LOOP")
            if p1x == p2x and abs(p1y-p2y) is not wh:
                bezier(p1x, p1y, abs(p1x-qwh), p1y, abs(p2x-qwh), p2y, p2x, p2y)
            elif p1y == p2y and abs(p1x-p2x) is not wh:
                bezier(p1x, p1y, p1x, abs(p1y-qwh), p2x, abs(p2y-qwh), p2x, p2y)
            return
        #opposite sides
        elif (abs(p1y-p2y) == wh and p1x == p2x) or (abs(p1x-p2x) == wh and p1y == p2y):
            #print("OPPOSITE")
            line(p1x,p1y,p2x,p2y)
            return
        #cross over
        elif p1%8 == (p2+4)%8:
            #print("CROSSOVER")
            #up down
            if int(p1/2) == 0 or int(p1/2) == 2:
                bezier(p1x, p1y, p1x, hwh, p2x, hwh, p2x, p2y)
            #left right
            elif int(p1/2) == 1 or int(p1/2) == 3:
                bezier(p1x, p1y, hwh, p1y, hwh, p2y, p2x, p2y)
            return
        #corners
        elif abs(p1-p2) == 1  or abs(p1-p2) == 7:
            #print("CORNER")
            #p1 is left or right
            if p1x % wh == 0:
                bezier(p1x, p1y, abs(p1x-qwh), p1y, p2x, abs(p2y-qwh), p2x, p2y)
            else:
                bezier(p1x, p1y, p1x, abs(p1y-qwh), abs(p2x-qwh), p2y, p2x, p2y)
            return
        #curves
        elif abs(p1-p2) == 2 or (p1 == 1 and p2 == 7) or (p1 == 7 and p2 == 1):
            #print("CURVE")
            #p1 is left or right
            if p1x % wh == 0:
                bezier(p1x, p1y, abs(p1x-qwh), p1y, p2x, abs(p2y-qwh), p2x, p2y)
            else:
                bezier(p1x, p1y, p1x, abs(p1y-qwh), abs(p2x-qwh), p2y, p2x, p2y)
            return
        #big arc
        else:
            #print("BIG ARC")
            #p1 is left or right
            if p1x % wh == 0:
                bezier(p1x, p1y, hwh, p1y, p2x, hwh, p2x, p2y)
            else:
                bezier(p1x, p1y, p1x, hwh, hwh, p2y, p2x, p2y)
            return
            
        #print("something went wrong")
    
    #renderconnection(1,7)
    
    count = 0
    for tile in tilerules:
        clear()
        background(128,128,128)
        
        #draw the lines for this tile
        for linedef in tile:
            renderconnection(linedef[0], linedef[1])
        save(str(count)+".png")
        count+=1
    
    # #         startx = tileindices[linedef[0]][0]
    # #         starty = tileindices[linedef[0]][1]
    # #         endx = tileindices[linedef[1]][0]
    # #         endy = tileindices[linedef[1]][1]
    # #         line(startx, starty, endx, endy)
    
            