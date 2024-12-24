# range(start, stop, step)

"""
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1 

"""

x = range(6)
for n in x:
  print(n)

x = range(3, 6)
for n in x:
  print(n)

x = range(3, 20, 2)
for n in x:
  print(n)