with open('d11input.dat', 'r') as myfile:
  input = myfile.read()

ew = 0
ns = 0
maxew = 0
maxns = 0

i = 0

input = input.split(',')

## for every line
for i in input:
	for j in i:
		if j == "n": ns += 1
		if j == "s": ns -= 1
		if j == "e": ew += 1
		if j == "w": ew -= 1
	if abs(ns) > abs(maxns): maxns = ns
	if abs(ew) > abs(maxew): maxew = ew


if (ns > ew): print ns
else: print ew

if (maxns > maxew): print maxns
else: print maxew
