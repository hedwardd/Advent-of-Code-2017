input = 361527

found = False
ringRoot = 1

# Finds what "ring" it's in
while (found == False):
	ringNum = (ringRoot - 1) / 2


	if (ringRoot * ringRoot) > input:
		found = True
	else:
		ringRoot += 2

print ringNum
print ringRoot
ringMax = ringRoot*ringRoot
print ringMax


adjustedNum = input - (ringRoot-2)*(ringRoot-2)
print adjustedNum


## distance is distance to middle plus nth ring

distanceToMiddle = abs(ringNum - (adjustedNum % (ringNum*2)))
distance = distanceToMiddle + ringNum
print distance


