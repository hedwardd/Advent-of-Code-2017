with open('d13inputsample', 'r') as myfile:
  input = myfile.read()

  input = input.splitlines()


delay = 0
found = 0

## move into a while loop

while found == 0:

	count = 0

	for s in input:
	  	s = s.split(': ')
	  	if (int(s[0]) + delay) % ((int(s[1]) - 1) * 2) == 0:
	  		count = count + 1
	  		break

	print "delay: ", delay, " count: ", count

	if count == 0: found = 1
	else: delay = delay + 1
	if delay > 100000: found = 1

## report number of moves delayed once finished
print delay
  	   