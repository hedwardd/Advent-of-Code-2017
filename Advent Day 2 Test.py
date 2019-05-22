lines = """5 1 9 5
7 5 3
2 4 6 8"""

checksum = 0

lines = lines.splitlines()
i = 0

## for every line
while i < len(lines):
	thisRow = lines[i]
	thisRow = thisRow.split(' ')

	## new low and high

	low = thisRow[0]
	high = thisRow[0]

	## new counter
	column = 1

	## for every column
	while column <= len(thisRow)-1:

		if thisRow[column] < low:
			low = thisRow[column]
		if thisRow[column] > high:
			high = thisRow[column]
		column = column + 1

	## add up checksum
	checksum = checksum + int(high) - int(low)

	## count
	i = i + 1
	print(checksum)

print(checksum)