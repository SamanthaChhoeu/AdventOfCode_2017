maze = open('input.txt')

instructions = {}

# go through list of instructions
for i,ins in enumerate(maze):
    instructions[i] = int(ins)
end = len(instructions)

i = 0
ins = instructions[i]
steps = 0
while i < end:
    ins = instructions[i]
    if ins >= 3:
        instructions[i] -= 1
    else:
        instructions[i] += 1
    i += ins
    steps += 1
print 'number of steps is',steps
