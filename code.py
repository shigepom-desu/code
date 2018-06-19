input_num = input()
input_q = input()
code = ''
met = ''
pl = ''

for i in range(int(input_num)):
  met = str(i + 1)
  if input_q[i] == 'L':
    code = met + code
  elif input_q[i] == 'R':
    code = code + met
codes = list(code)

for char in codes:
  pl += char + ' '

pl = pl.rstrip(' ') + '\r'

print(pl)