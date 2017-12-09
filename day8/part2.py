file = open('input.txt')

registers = {}

largest = 0
for instruction in file:
    instruction = instruction.split()
    reg = instruction[0]
    num = int(instruction[2])
    if reg not in registers.keys():
        registers[reg] = 0
    if instruction[4] not in registers.keys():
        registers[instruction[4]] = 0
    condition = eval('registers[instruction[4]]'+instruction[5]+instruction[6])
    # print 'registers[instruction[4]]'+instruction[5]+instruction[6],condition
    if  condition:
        if instruction[1] == 'inc':
            registers[reg] += num
        else:
            registers[reg] -= num
    if registers[reg] > largest:
        largest = registers[reg]


print ('largest value held is',largest)
