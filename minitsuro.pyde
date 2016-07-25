from time import sleep
global shoulddraw
wh = 700
gutter=36
qwh = wh/4
hwh = wh/2
twh = wh/3
ewh = wh/8
sxwh = wh/16
tilerules = (((0,1),(2,3),(4,5),(6,7)),((0,1),(2,3),(4,6),(5,7)),((0,1),(2,3),(4,7),(5,6)),((0,1),(2,4),(3,6),(5,7)),((0,1),(2,4),(3,7),(5,6)),((0,1),(2,5),(3,6),(4,7)),((0,1),(2,5),(3,7),(4,6)),((0,1),(2,6),(3,4),(5,7)),((0,1),(2,6),(3,5),(4,7)),((0,1),(2,6),(3,7),(4,5)),((0,1),(2,7),(3,4),(5,6)),((0,1),(2,7),(3,5),(4,6)),((0,1),(2,7),(3,6),(4,5)),((0,2),(1,3),(4,6),(5,7)),((0,2),(1,3),(4,7),(5,6)),((0,2),(1,4),(3,6),(5,7)),((0,2),(1,4),(3,7),(5,6)),((0,2),(1,5),(3,6),(4,7)),((0,2),(1,5),(3,7),(4,6)),((0,2),(1,6),(3,4),(5,7)),((0,2),(1,6),(3,5),(4,7)),((0,2),(1,7),(3,4),(5,6)),((0,2),(1,7),(3,5),(4,6)),((0,3),(1,2),(4,7),(5,6)),((0,3),(1,4),(2,6),(5,7)),((0,3),(1,4),(2,7),(5,6)),((0,3),(1,5),(2,6),(4,7)),((0,3),(1,6),(2,5),(4,7)),((0,4),(1,2),(3,6),(5,7)),((0,4),(1,2),(3,7),(5,6)),((0,4),(1,3),(2,6),(5,7)),((0,4),(1,5),(2,6),(3,7)),((0,4),(1,5),(2,7),(3,6)),((0,5),(1,4),(2,7),(3,6)),((0,7),(1,2),(3,4),(5,6)))
tileindices = ((twh, wh), (2*twh, wh), (wh, 2*twh), (wh, twh), (2*twh, 0), (twh, 0), (0, twh), (0, 2*twh))

def renderborder():
    #bottom
    line(twh,wh+gutter,twh,wh-3)
    line(2*twh, wh+gutter, 2*twh, wh-3)
    #top
    line(2*twh,0-gutter,2*twh,0+3)
    line(twh,0-gutter,twh,0+3)
    #left
    line(0-gutter,twh,0+3,twh)
    line(0-gutter,2*twh,0+3,2*twh)
    #right
    line(wh-3,twh,wh+gutter,twh)
    line(wh-3,2*twh,wh+gutter,2*twh)
    
def starttile():
    #bottom
    line(twh,wh+gutter,twh,(wh-gutter*2))
    line(2*twh, wh+gutter, 2*twh, wh-(gutter*2))
    #top
    line(2*twh,0-gutter,2*twh,(0+gutter*2))
    line(twh,0-gutter,twh,0+(gutter*2))
    #left
    line(0-gutter,twh,0+(gutter*2),twh)
    line(0-gutter,2*twh,0+(gutter*2),2*twh)
    #right
    line(wh-(gutter*2),twh,wh+gutter,twh)
    line(wh-(gutter*2),2*twh,wh+gutter,2*twh)

def countcrossovers(rule):
    print(tilerules.index(rule))
    crossovers = 0
    colist = []
    sides = {}
    #2 on the same side is different from 2 on different sides or 4 on all sides
    for tile in rule:
        p1 = tile[0]
        p2 = tile[1]
        if p1%8 == (p2+4)%8:
            crossovers += 1
            colist.insert(0, tile)
    #determine if any are on the same side
    for co in colist:
        #add to sides
        sides[int(co[0]/2)] = True
        sides[int(co[1]/2)] = True
    print(len(sides))   
    return(crossovers, len(sides))

def settings():
    size(wh+(2*gutter), wh+(2*gutter), P3D)

def setup():
    global shoulddraw
    shoulddraw = True

def draw():
    global shoulddraw
    if shoulddraw:
        noFill()
        smooth()
        strokeWeight(20)
        stroke(217,187,100)
        translate(gutter,gutter)
        bg = loadImage("bg.jpg")

        def renderconnection(p1,p2, tile):
            p1x = tileindices[p1][0]
            p1y = tileindices[p1][1]
            p2x = tileindices[p2][0]
            p2y = tileindices[p2][1]
            
            #loops, same side
            if int(p1/2) == int(p2/2):
                ("LOOP")
                if p1x == p2x and abs(p1y-p2y) is not wh:
                    bezier(p1x, p1y, abs(p1x-qwh), p1y, abs(p2x-qwh), p2y, p2x, p2y)
                elif p1y == p2y and abs(p1x-p2x) is not wh:
                    bezier(p1x, p1y, p1x, abs(p1y-qwh), p2x, abs(p2y-qwh), p2x, p2y)
                return
            #opposite sides
            elif (abs(p1y-p2y) == wh and p1x == p2x) or (abs(p1x-p2x) == wh and p1y == p2y):
                ("OPPOSITE")
                line(p1x,p1y,p2x,p2y)
                return
            #cross over
            elif p1%8 == (p2+4)%8:
                print("CROSSOVER")
                #up down
                co=countcrossovers(tile)
                print(co)
                if int(p1/2) == 0 or int(p1/2) == 2:
                    if co[0] == 4:
                        bezier(p1x, p1y, p1x, abs(p1y-qwh), p2x, abs(p2y-qwh), p2x, p2y)
                    elif (co[0] == 2 and co[1] == 2) or co[0] == 1:
                        bezier(p1x, p1y, p1x, abs(p1y-hwh-qwh), p2x, abs(p2y-hwh-qwh), p2x, p2y)
                    else:
                        bezier(p1x, p1y, p1x, hwh+qwh, hwh, p1y-qwh, hwh, hwh)
                        bezier(hwh, hwh, hwh, p2y+qwh, p2x, qwh, p2x, p2y)
                #left right
                elif int(p1/2) == 1 or int(p1/2) == 3:
                    if co[0] == 4:
                        bezier(p1x, p1y, abs(p1x-qwh), p1y, abs(p2x-qwh), p2y, p2x, p2y)
                    elif (co[0] == 2 and co[1] == 2) or co[0] == 1:
                        bezier(p1x, p1y, abs(p1x-hwh-qwh), p1y, abs(p2x-hwh-qwh), p2y, p2x, p2y)
                    else:
                        bezier(p1x, p1y, hwh+qwh, p1y, p1x-qwh, hwh, hwh, hwh)
                        bezier(hwh, hwh, p2x+qwh, hwh, qwh, p2y, p2x, p2y)
                return
            #corners
            elif abs(p1-p2) == 1  or abs(p1-p2) == 7:
                ("CORNER")
                #p1 is left or right
                if p1x % wh == 0:
                    bezier(p1x, p1y, abs(p1x-qwh), p1y, p2x, abs(p2y-qwh), p2x, p2y)
                else:
                    bezier(p1x, p1y, p1x, abs(p1y-qwh), abs(p2x-qwh), p2y, p2x, p2y)
                return
            #curves
            elif abs(p1-p2) == 2 or (p1 == 1 and p2 == 7) or (p1 == 7 and p2 == 1):
                ("CURVE")
                #p1 is left or right
                if p1x % wh == 0:
                    bezier(p1x, p1y, abs(p1x-3*ewh), p1y, p2x, abs(p2y-3*ewh), p2x, p2y)
                else:
                    bezier(p1x, p1y, p1x, abs(p1y-3*ewh), abs(p2x-3*ewh), p2y, p2x, p2y)
                return
            #big arc
            else:
                bz1x = p1x
                bz1y = p1y
                bz2x = p2x
                bz2y = p2y
                ("BIG ARC")
                #p1 is left or right
                smaller = 3*sxwh
                larger = 13*sxwh
                if p1x == 0:
                    #left
                    bz1x = smaller
                elif p1x == wh:
                    #right
                    bz1x = larger
                if p1y == 0:
                    #top
                    bz1y = smaller
                elif p1y == wh:
                    #bottom
                    bz1y = larger
                
                if p2x == 0:
                    bz2x = smaller
                elif p2x == wh:
                    bz2x = larger
                if p2y == 0:
                    bz2y = smaller
                elif p2y == wh:
                    bz2y = larger
                bezier(p1x, p1y, bz1x, bz1y, bz2x, bz2y, p2x, p2y)
                #color(255,0,0)
                #point(bz1x - 20, bz1y)
                #point(bz2x, bz2y)
                #color(0,0,0)

                return

        shoulddraw = False

        # renderconnection(0,4)
        # renderconnection(1,5)
        # for rule in tilerules:
        #     print(countcrossovers(rule))

        count = 0
        for tile in tilerules:
            clear()
            smooth(8)
            #background(193,159,119)
            textureWrap(REPEAT)
            noStroke()
            translate(-gutter,-gutter)
            beginShape()
            background(0)
            texture(bg)

            vertex(0,0,0,0)
            vertex(wh+(2*gutter),0,wh+(2*gutter),0)
            vertex(wh+(2*gutter),wh+(2*gutter),wh+(2*gutter),wh+(2*gutter))
            vertex(0,wh+(2*gutter),0,wh+(2*gutter))
            
            endShape()
            stroke(217,187,100)
            noFill()
            translate(gutter,gutter)
            #calculate which way to render the cross overs
            # for rule in tilerules:
            #     print(countcrossovers(rule))
            
            #draw the lines for this tile
            for linedef in tile:
                renderborder()
                renderconnection(linedef[0], linedef[1], tile)
            save(str(count)+".png")
            count+=1
        clear()
        smooth(8)
        #background(193,159,119)
        textureWrap(REPEAT)
        noStroke()
        translate(-gutter,-gutter)
        beginShape()
        background(0)
        texture(bg)

        vertex(0,0,0,0)
        vertex(wh+(2*gutter),0,wh+(2*gutter),0)
        vertex(wh+(2*gutter),wh+(2*gutter),wh+(2*gutter),wh+(2*gutter))
        vertex(0,wh+(2*gutter),0,wh+(2*gutter))
        
        endShape()
        stroke(217,187,100)
        noFill()
        translate(gutter,gutter)
        starttile()
        save("border.png")
            
                
        