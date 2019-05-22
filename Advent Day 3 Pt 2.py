
## Builds a 2-dim array of 2000 by 2000 spots filled with 0s

x = 0
y = 0
a = []

while x < 2000:
	newList = []
	while y < 2000:
		newList.append(0)
		y += 1
	y = 0
	a.append(newList)
	x += 1


## Sets starting point to center of 2-dim array (1000,1000)

x = 1000
y = 1000


## Initiates starting direction to "Right"

global direction
direction = "Right"


## Initiates step function that moves position based on direction
## Then turns left if it can

def step():

	global x
	global y
	global direction

	if direction == "Right":
		x += 1
		if a[x][y+1] == 0:
			direction = "Up"
	elif direction == "Down":
		y -= 1
		if a[x+1][y] == 0:
			direction = "Right"
	elif direction == "Left":
		x -= 1
		if a[x][y-1] == 0:
			direction = "Down"
	elif direction == "Up":
		y += 1
		if a[x-1][y] == 0:
			direction = "Left"

done = False

while (done == False):
	if (x == 1000) & (y == 1000):
		a[x][y] = 1
	else:
		a[x][y] = a[x][y+1] + a[x+1][y+1] + a[x+1][y] + a[x+1][y-1] + a[x][y-1] + a[x-1][y-1] + a[x-1][y] + a[x-1][y+1]
	print a[x][y]
	step()
	if a[x][y] >= 361527:
		print "it should be done"
		done = True

