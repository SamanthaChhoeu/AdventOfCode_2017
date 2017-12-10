file = open('input.txt')

input = ''
for line in file:
	input = line
	break


ignore = 1
prev = ''

garbage = 0

for char in input:
	if char == '>' and prev != '!':
		ignore = 1
	elif prev != '!' and ignore != 1:
		garbage += 1
		if char == '!' :
			garbage -= 1
	elif char == '<':
		ignore = 0
	if prev == '!':
		prev = ''
	else:		
		prev = char




print 'non cancelled characters in garbage is', garbage