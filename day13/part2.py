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
delay = 0
while delay != None:
    
    i = 0
    while i < highest+1:
        j = i + delay
#         print(j)
        if i not in depths.keys():
            i += 1
            continue
        else:
    #         print (i,depths[i])
            if (j)%(depths[i]*2-2) == 0:
                delay += 1
#                 print (delay)
                i = 0
            else:
                i += 1
    print ('delay',delay)
    delay = None

