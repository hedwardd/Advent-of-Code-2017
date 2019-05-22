input = 361527

found = False
ringRoot = 1

## First step to find what ring it's in

while (found == False):
	if (ringRoot * ringRoot) > input:
		found = True
	else:
		ringRoot += 2

# Calculates what number ring the input is in

ringNum = (ringRoot - 1) / 2

## Finds what place the input is in the ring

adjustedNum = input - (ringRoot-2)*(ringRoot-2)


## Finds distance to a middle number of the ring

distanceToMiddle = abs(ringNum - (adjustedNum % (ringNum*2)))

## distance is distance to middle of ring plus n (ringNum) steps to center

distance = distanceToMiddle + ringNum

print distance


