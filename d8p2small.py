lines = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""


## clean up input
lines = lines.splitlines()


dict = {}


def update(key, plusminus, value):
	print("key: ", key, " plusminus: ", plusminus, " value: ", value)
	if (plusminus == "inc"):
		dict[key] = dict.get(key, 0) + int(value)
	else:
		dict[key] = dict.get(key, 0) - int(value)


## main function
Max = 0
i = 0
while i < len(lines):
	thisRow = lines[i]
	thisRow = thisRow.split(' ')
	print "thisRow: ", thisRow


	if ((thisRow[5] == ">") and (dict.get(thisRow[4], 0) > int(thisRow[6]))): update(thisRow[0], thisRow[1], thisRow[2])
	if ((thisRow[5] == "<") and (dict.get(thisRow[4], 0) < int(thisRow[6]))): update(thisRow[0], thisRow[1], thisRow[2])
	if ((thisRow[5] == "<=") and (dict.get(thisRow[4], 0) <= int(thisRow[6]))): update(thisRow[0], thisRow[1], thisRow[2])
	if ((thisRow[5] == ">=") and (dict.get(thisRow[4], 0) >= int(thisRow[6]))): update(thisRow[0], thisRow[1], thisRow[2])
	if ((thisRow[5] == "==") and (dict.get(thisRow[4], 0) == int(thisRow[6]))): update(thisRow[0], thisRow[1], thisRow[2])
	if ((thisRow[5] == "!=") and (dict.get(thisRow[4], 0) != int(thisRow[6]))): update(thisRow[0], thisRow[1], thisRow[2])

	print "dict: ",dict

	if bool(dict):
		if dict[max(dict, key=dict.get)] > Max: Max = dict[max(dict, key=dict.get)]

	i += 1

print Max