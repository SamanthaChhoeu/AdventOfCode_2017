direction = open('input.txt')

for line in direction:
#     line = 'se,sw,se,sw,sw'
    directions = line.split(',')

# rep coords in x,y coordinates
x = y = 0
for move in directions:
#     print (move,x,y)
    if move == 'n':
        y += 2
    elif move == 's':
        y -= 2
    elif move == 'ne':
        x += 2
        y += 1
    elif move == 'se':
        x+=2
        y -= 1
    elif move == 'sw':
        x -= 2
        y -= 1
    elif move == 'nw':
        x -= 2
        y += 1
        
count = 0
while x!= 0 or y != 0:
    
    move = 'ne'
    if x > 0:
        if y < 0:
            move = 'sw'
        elif y > 0:
            move = 'se'
    elif x < 0:
        if y < 0:
            move = 'ne'
        elif y > 0: 
            move = 'nw'
    if x == 0:     
        if y < 0:
            move = 'n'
        elif y < 0:
            move = 's'
        
    if move == 'n':
        y += 2
    elif move == 's':
        y -= 2
    elif move == 'ne':
        x += 2
        y += 1
    elif move == 'se':
        x+=2
        y -= 1
    elif move == 'sw':
        x -= 2
        y -= 1
    elif move == 'nw':
        x -= 2
        y += 1
    count += 1

print 'step distance from start',count
    
