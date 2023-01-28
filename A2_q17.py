n = int(input('Enter the the total no. of rows to be printed:'))
nst=1
nsp=n/2
row=1
while(row<=n):
  sp=1
  while(sp<=nsp):
    if (row==n//2+1):
      print("*\t",end="")
    else:
      print("\t",end="")
    sp+=1
  st=1
  while(st<=nst):
    print("*\t",end="")
    st+=1
  print()
  if(row<=n/2):
    nst+=1
  else:
    nst-=1
  row+=1
