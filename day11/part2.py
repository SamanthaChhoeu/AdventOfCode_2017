direction = open('input.txt')
def findSteps(x,y):
    count = 0
    diag = abs(x)/2
    vert = (abs(y) - diag)/2
    count += (diag+vert)
    return count

for line in direction:
#     line = 'se,sw,se,sw,sw'
    directions = line.split(',')
furthest = 0
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
    distance = findSteps(x,y)    
    if distance >furthest:
        furthest = distance

print 'Furthest it has been from start',furthest
