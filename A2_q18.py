n = int(input('Enter the the total no. of rows to be printed:'))
nsp=0
nst=n
for i in range(1,n+1):
  for j in range(1,nsp+1):
    print("\t",end="")
  for j in range(1,nst+1):
    if (i>1 and i<=n/2 and j>1 and j<nst):
      print("\t",end="")
    else:
      print("*\t", end="")
  if i<=n/2:
    nsp+=1
    nst-=2
  else:
    nsp-=1
    nst+=2
  print()
