file = open('input2.txt')

total = 0
for line in file:
    numbers = line.split()
    length = len(numbers)
    for i in range(0,length-1):
        num = numbers[i]
        for j in range(i+1,length):
            dvd = max(int(num),int(numbers[j]))
            dvr = min(int(num),int(numbers[j]))
            if dvd%dvr == 0:
                total += int(dvd/dvr)
print('checksum is',total)
