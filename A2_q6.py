n=int(input('Enter the the total no. of rows to be printed:'))
def Pattern(n):
  sp=1
  st=n//2+1
  for i in range(1,n+1):
    for star in range(1,st+1):
      print('*',end="\t");
    for space in range(1,sp+1):
      print (end="\t");
    for star in range(1,st+1):
      print('*',end="\t");  
    if (i<=n//2):
      st=st-1
      sp=sp+2
    else:
      st=st+1
      sp=sp-2
    print("\n")
Pattern(n)
