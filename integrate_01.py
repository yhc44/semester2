def testFunction(x):
  return x*x

def width(a, b, n):
  return (b-a) / n

def o(function, a, b, n = 1000):
  sum = 0
  res = 0
  w = width(a, b, n)
  for i in range(0, n-1):
    sum = sum + function(a + (w / 2) + (i * w))
  return w * sum

# slow convergence 
print(o(testFunction, 0, 100))
print(o(testFunction, 0, 100, n = 10000))
print(o(testFunction, 0, 100, n = 100000))
print(o(testFunction, 0, 100, n = 1000000))
print(o(testFunction, 0, 100, n = 10000000))
