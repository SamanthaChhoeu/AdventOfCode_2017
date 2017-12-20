buffer = 370
curr = 1
i = 1
locks = [0,1]
length = 2

while locks[curr] < 2017:
    
    curr = (curr+buffer+1)%length
#     print(locks,'current',curr,length)
    i+=1
    
    if curr != length:
#         print (locks,locks[0:curr],locks[curr:])
        locks = locks[0:curr]+[i]+locks[curr:]
    else:
        locks += [i]

    length += 1

print('value after 2017 is',locks[curr+1])
