
x = lambda a: a + 10
print (x(5))

y = lambda b, c: b * c
print(y(2,3))

def myfunc(n):
  return lambda d : d * n

mydoubler = myfunc(2)

print(mydoubler)

print(mydoubler(11))