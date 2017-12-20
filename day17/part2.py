buffer = 370
curr = 0
i = 0
length = 1

watch = 1

for i in range(50000000):
#     print ('length before',curr,length)
    curr = (curr+buffer)%(length)
    i+=1
    if curr == 0:
#         print (length,i)
        watch = i
    curr += 1
#     print('current state',curr,length)
#     print(locks,'current',curr,length)
    
    length += 1

print('value after index 0 is',watch)
