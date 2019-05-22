lines = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


## clean up input
lines = lines.splitlines()


## main function
i = 0
dict = {}
while i < len(lines):
	thisRow = lines[i]
	thisRow = thisRow.split(' ')
	thisRow.pop(1)
	if len(thisRow)>1: thisRow.pop(1)
	for item in thisRow:
		item = item.rstrip(',')
		if item in dict:
			dict[item] += 1
		else:
			dict[item] = 1

	i += 1

print min(dict, key=dict.get)
