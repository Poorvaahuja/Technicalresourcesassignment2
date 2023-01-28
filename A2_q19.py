n = int(input('Enter the the total no. of rows to be printed:'))
m=int(n/2)+1
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==1:
      if(j<=m or j==n):
        print("*\t", end="")
      else:
        print("\t", end="")
    elif (i>1 and i<m):
      if (j==m or j==n):
        print("*\t", end="")
      else:
        print("\t", end="")
    elif (i==m):
      print("*\t", end="")
    elif (i>m and i<n):
      if(j==1 or j==m):
        print("*\t", end="")
      else:
        print("\t", end="")
    elif(i==n):
      if (j==1 or j>=m):
        print("*\t", end="")
      else:
        print("\t", end="")
  print()
