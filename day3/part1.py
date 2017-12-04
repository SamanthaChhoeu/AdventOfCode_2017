side = 1
i = 1
data = 277678
end = 1

# find distance from centre
while end < data:
    side = side+2
    i += 1
    end += side*4-4
halfway = (side-1)/2

# get shortest distance to align with centre
absdist = min (abs(end-halfway-data),abs(end-halfway*3-data),
     abs(end-halfway*5-data),abs(end-halfway*7-data))

print 'distance from 1 is',int(i+absdist-1)
