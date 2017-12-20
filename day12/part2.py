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
group = {}


count = 0
iGroup = 0

for key in graph.keys():
    seen = {}
#     print (key)
    if key not in group.keys():
#         print (key,group)
        queue = [key]
        while len(queue) != 0:

            curr = queue.pop(0)
            if curr not in seen.keys():
                seen[curr] = 1
                group[curr] = iGroup
                for node in graph[curr]:
                    if node not in seen.keys():
                        queue += [node]
                queue += graph[curr] 
                count += 1
        iGroup += 1
print ('total number of groups',iGroup)
