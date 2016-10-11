'''Write a program that asks the user to input 10 integers, and
then prints the largest odd number that was entered. If no odd number was
entered, it should print a message to that effect.'''

max = None

i = 0
while i < 10:
  n = int(raw_input('> '))
  if (max and n % 2 != 0 and n > max) or (not max and n % 2 != 0):
    max = n
  i += 1

if max:
  print max
else:
  print "All even."
