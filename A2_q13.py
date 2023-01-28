import math
n = int(input('Enter the the total no. of rows to be printed:'))
i=0
while(i<n):
  a=1
  j=0
  while(j<=i):
    print(a, end="\t")
    b= math.trunc(a*(i-j)/(j+1))
    a=b
    j+=1
  i+=1
  print()
