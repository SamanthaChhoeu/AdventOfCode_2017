file = open('input.txt')

graph = {}
# record location of scanner
highest = 0
for line in file:
    nums = line.split()
    program = int(nums[0])
    connected = nums[2:]
    newCon = []
    for node in connected:
        newCon += [int(node.replace(',',''))]
    graph[program] = newCon
# print(graph)

seen = {}
queue = [0]


count = 0

while len(queue) != 0:
    curr = queue.pop(0)
    if curr not in seen.keys():
        seen[curr] = 1
#         print (seen)
        for node in graph[curr]:
            if node not in seen.keys():
                queue += [node]
        queue += graph[curr] 
        count += 1
print ('number of program groups',count)
    
