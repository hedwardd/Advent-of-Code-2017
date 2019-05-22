characters = "{{<a!>},{<a!>},{<a!>},{<ab>}}"

intrash = False
skip = False

cleaned = []

for i in characters:
	if skip == True:
		skip = False
		print "1"
	elif i == "!":
		skip = True
		print "skip"
	elif i == ">" and intrash == True:
		intrash = False
		print "2"
	elif intrash == True:
		print "3"
	elif i == "<" and intrash == False:
		intrash = True
		print "4"
	else:
		cleaned.append(i)
		print "5"

print cleaned

level = 0
count = 0

for i in cleaned:
	print i
	if  i == "{":
		level += 1
		print "level increase"
	elif i == "}":
		print "count increase. level decrease."
		count += level
		level -= 1
	print "level = ", level
	print "count = ", count

print count
	
