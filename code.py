input_lines = input()
input_lifes = input()
sum = 0

for char in input_lines:
  sum  += int(char)
if sum >= int(input_lifes):
  print('OK')
else:
  print('NG')
