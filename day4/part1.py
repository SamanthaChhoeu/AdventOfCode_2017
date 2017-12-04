file = open('input.txt')
seen = {}
for line in file:
    words = line.split()
    valid = 0
    for word in words:
    #         print (word)
        if word in seen.keys():
            valid -= 1
            break
        else:
            seen[word] = 1
    valid += 1
print 'There are',valid,'passphrases'
