'''Write a program that examines three variables— x , y , and z —
and prints the largest odd number among them. If none of them are odd, it
should print a message to that effect.'''

x = 22
y = 3
z = 5

if x % 2 != 0 and (x >= y or y % 2 == 0) and (x >= z or z % 2 == 0):
  print x
elif y % 2 != 0 and (y >= x or x % 2 == 0) and (y >= z or z % 2 == 0):
  print y
elif z % 2 != 0 and (z >= y or y % 2 == 0) and (z >= x or x % 2 == 0):
  print z
else:
  print "All numbers are even."
