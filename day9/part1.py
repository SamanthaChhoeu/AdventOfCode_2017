file = open('input.txt')

input = ''
for line in file:
	input = line
	break

score = 0
openB = 0
closeB = 0
ignore = 0
prev = ''

group = 0

for char in input:
	
	if prev != '!':
		# print char
		if char == '!' :
			ignore = 1
		elif char == '<':
			ignore = 1
		elif char ==  '>' :
			ignore = 0
		elif ignore == 1:
			continue
		elif char  == '{':
			group += 1
		elif char == '}' and ignore != 1:
			print group
			score += group
			group -= 1

			
		prev = char
	else:
		prev = ''

print 'score is',score