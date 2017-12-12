string = '31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33'

lengths = []
for char in string:
    lengths += [ord(char)]

lengths += [17, 31, 73, 47, 23]
numbers = {}
curr = 0
skip = 0
total = 256
for i in range (total):
    numbers[i] = i

rounds = 64
while rounds > 0:
    for length in lengths:

        j = length + curr -1
        j = j % total
        i = curr

        swap = 0

        while swap < int(length/2):
            temp = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = temp
            i += 1
            j -= 1
            if j < 0:
                j = j + total
            i = i%total
            swap += 1
        curr = length + skip + curr
        curr = curr % total
        skip += 1
    rounds -= 1


dense = []

i = 0
block = 0
while i < 256:
    if block == 0:
        block = numbers[i]
    else:
        block = block ^ numbers[i]
        
    if (i+1)%16 == 0:
        dense += [block]
        block = 0
    
    i += 1

hexa = ''
for num in dense:
    note = hex(num)
    note = note.replace('0x','')
    if len (note) == 1:
        note = '0'+note
    hexa += note

print 'result is', hexa
