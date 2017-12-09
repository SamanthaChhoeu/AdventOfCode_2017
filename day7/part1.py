file = open('input.txt')

seen = {}
for line in file:
    items = line.split()
    curr = items[0]
    if '->' in items:
        store = items[3:]
        seen[curr] = store

count = {}
for key in seen.keys():
    test = seen[key]

    for i in test:
        i = i.replace(',', '')
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 0
# print (seen.keys())
# print (count.keys())
for key in seen.keys():
#     print (key)
    if key not in count.keys():
        print key
