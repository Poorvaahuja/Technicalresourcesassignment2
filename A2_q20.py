n = int(input('Enter the the total no. of rows to be printed:'))
for i in range(1,n+1):
  for j in range(1,n+1):
    if (j==1 or j==n):
      print("*\t",end="")
    elif ((i>n/2) and (i==j or i+j==n+1)):
      print("*\t", end="")
    else:
      print("\t",end="")
  print()
