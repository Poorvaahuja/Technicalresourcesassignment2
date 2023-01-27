n = int(input('Enter the the total no. of rows to be printed:'))
nst=1
nsp=2*n-3
row=1
while(row<=n):
  st=1
  while(st<=nst):
    print(st,end="")
    print("\t",end="")
    st+=1
  sp=1
  while(sp<=nsp):
    print("\t",end="")
    sp+=1
  if (row==n):
    nst-=1
  st1=nst
  while(st1>=1):
    print(st1,end="")
    print("\t",end="")
    st1-=1
  print()
  nst+=1
  nsp-=2
  row+=1
