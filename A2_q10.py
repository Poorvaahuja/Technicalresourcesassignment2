n = int(input('Enter the the total no. of rows to be printed:'))
Osp=n//2
Isp= -1
for i in range(n):
  for j in range(Osp):
    print("\t",end="")
  print("*\t",end="");
  for j in range(Isp):
    print("\t",end="")
  if (i!=0 and i!=n-1):
    print("*\t",end="")
  if (i<n//2):
    Osp-=1
    Isp+=2
  else:
    Osp+=1
    Isp-=2
  print("\n")
