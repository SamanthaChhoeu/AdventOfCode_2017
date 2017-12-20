programs = 'abcdefghijklmnop'
# programs = 'abcde'
position = {} # keep track of items position
slot = {} # keep track of item in each slot

for i,prog in enumerate(programs):
    position[prog] = str(i)
    slot[str(i)] = prog
    
length = len(programs)
print(length)

# based on index in slot
def swap(x,y):

    let1 = slot[x]
    let2 = slot[y]
    num1 = position[let1]
    num2 = position[let2]
    
    slot[num1] = let2
    slot[num2] = let1
    
    position[let1] = num2
    position[let2] = num1  
    
#     print (slot)

moves = open('input.txt')
for item in moves:
    moves = item.split(',')

count = 0

seen = {}
while count < 1:
    start = ''
    for key in slot.keys():
        start += slot[key]
        
    if start in seen.keys():
        slot = seen[start]
    else:
        for move in moves:
            dance = move[0]
            indexes = move[1:]
            indexes = indexes.split('/')
            if dance != 's':
                ind1 = indexes[0]
                ind2 = indexes[1] 
                if ind1 in position.keys():
                # its a letter
                    # swap the letters
                    idx1 = position[ind1]
                    idx2 = position[ind2]

                    slot[idx1] = ind2
                    slot[idx2] = ind1

                    position[ind1] = idx2
                    position[ind2] = idx1

                else:
                # its a number
                    swap(ind1,ind2)

            else:
                num = int(move[1:])
                for item in position.keys():
                    index = position[item]
                    newIndex = (int(index)+num)%length
                    position[item] = str(newIndex)
                for item in position.keys():
                    index = position[item]
                    slot[index] = item
#     print(slot)
    seen[start] = slot.copy()
    count += 1

        
answer = ''
for key in slot.keys():
    answer += slot[key]
    
print(answer)
