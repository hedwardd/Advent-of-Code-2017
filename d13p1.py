with open('d13input', 'r') as myfile:
  input = myfile.read()

  input = input.splitlines()

  ## for every line in the input
  ## count it if picosecond % ((range - 1) * 2) is 0
  ## severity = picosecond * depth

count = 0

for s in input:
  	s = s.split(': ')
  	if int(s[0]) % ((int(s[1]) - 1) * 2) == 0:
  		count = count + int(s[0]) * int(s[1])

print count
  	   