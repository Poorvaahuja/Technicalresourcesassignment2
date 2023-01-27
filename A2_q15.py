n = int(input('Enter the the total no. of rows to be printed:'))
nsp=int(n/2)
nst=1
count=1
row=1
while(row<=n):
  sp=1
  while(sp<=nsp):
    print("\t",end="")
    sp+=1
  st=1
  while(st<=nst):
    print(count,end="")
    print("\t",end="")
    if (st<=int(nst/2)):
      count+=1
    else:
      count-=1
    st+=1
  print()
  count+=1
  if (row<=int(n/2)):
    count+=1
    nsp-=1
    nst+=2
  else:
    count-=1
    nsp+=1
    nst-=2
  row+=1 
