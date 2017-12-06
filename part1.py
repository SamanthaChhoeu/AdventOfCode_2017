
puzzle = '11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11'
puzzle = '0 2 7 0'

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
config = ''
newMost = 0
iNewMost = 0
length = len(memory)
print 'hi'
print memory,length
while config not in seen.keys():
    memory[iMost] = 0
    i = iMost
    while most > 0:
        i = (i+1)%length
        memory[i]+=1
        if memory[i] > newMost:
            newMost = memory[i]
            iNewMost = i
        most -= 0
    config = str(seen)
    seen[config] = 1
