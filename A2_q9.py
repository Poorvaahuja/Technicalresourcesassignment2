n = int(input('Enter the the total no. of rows to be printed:'))
for i in range(n):
  for j in range(n):
    if ((i==j)or(i+j==n-1)):
      print("*\t",end="")
    else:
      print("\t",end="")
  print("\n")
