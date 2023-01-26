n = int(input('Enter the the total no. of rows to be printed:'))
a=0
b=1
for i in range(n):
  for j in range(i):
    print(a,end="\t")
    c=a+b
    a=b
    b=c
  print("\n")
