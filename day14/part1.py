def knot(string):

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

    return hexa
        
def hex2bin(hexa):
    if hexa == 'a':
        return '1010'
    if hexa == 'b':
        return '1011'
    if hexa == 'c':
        return '1100'
    if hexa == 'd':
        return '1101'
    if hexa == 'e':
        return '1110'
    if hexa == 'f':
        return '1111'
    if hexa == '0':
        return '0000'
    if hexa == '1':
        return '0001'
    if hexa == '2':
        return '0010'
    if hexa == '3':
        return '0011'
    if hexa == '4':
        return '0100'
    if hexa == '5':
        return '0101'
    if hexa == '6':
        return '0110'
    if hexa == '7':
        return '0111'
    if hexa == '8':
        return '1000'
    if hexa == '9':
        return '1001'


string = 'xlqgujun'
squares = {}
count = 0
for i in range(128):
    hashIn = string+'-'+str(i)
    hashOut = knot(hashIn)
    new = ''
    for char in hashOut:
        new += hex2bin(char)
    for char in new:
        if char == '1':
            count += 1
print (count)
