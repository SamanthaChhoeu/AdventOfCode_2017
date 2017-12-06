
puzzle = '11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11'

banks = puzzle.split()
memory = {}
iMost = 0
most = 0
for i,bank in enumerate(banks):
    memory[i] = int(bank)
    if int(bank) > most:
        most = int(bank)
        iMost = i

seen = {}
length = len(memory)

cycles = 0
stop = True

while stop:
    i = iMost
    memory[i] = 0
    while most > 0:
        i = (i+1)%length
        memory[i]+=1

        most -= 1
    cycles += 1
    for j in range(length):
        if memory[j] > most:
            iMost = j
            most = memory[j]
    config = str(memory)
    if config not in seen.keys():
        seen[config] = cycles
    else:
        diff = cycles - seen[config]
        print 'number of cycles is',diff
        seen[config] += 1
        stop = False
