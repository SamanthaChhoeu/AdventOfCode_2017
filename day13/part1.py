file = open('input.txt')

depths = {}
# record location of scanner
index = {}
highest = 0
for line in file:
    nums = line.split()
    packet = int(nums[0].replace(':',''))
    depths[packet] = int(nums[1])
    if packet > highest:
        highest = packet


severity = 0


severity = 0
for i in range (highest+1):

    if i not in depths.keys():
        continue
    else:
#         print ()
        if (i)%(depths[i]*2-2) == 0:
            severity += i*depths[i]

print ('severity is',severity)
