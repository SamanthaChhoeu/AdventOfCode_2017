lengths = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
numbers = {}
curr = 0
skip = 0
total = 256
for i in range (total):
    numbers[i] = i

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

print 'result is', numbers[0]*numbers[1]
