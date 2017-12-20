a = 699
b = 124

match = 0

count = 0
while count <= 5000000:
    a = a*16807%2147483647#%65536
    b = b*48271%2147483647#%65536

    while a%4 != 0:

        a = a*16807%2147483647#%65536

    while b%8 != 0:
         b = b*48271%2147483647#%65536

    
    aBin = '{0:016b}'.format(a%65536)
    bBin = '{0:016b}'.format(b%65536)
    


    if aBin == bBin:
        match += 1

    count += 1


print (match)
