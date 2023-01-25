n=int(input('Enter the the total no. of rows to be printed:'))
def Pattern(n):
  st=1
  sp=n//2
  for i in range(1,n+1):
    for space in range(1,sp+1):
      print(end="\t");
    for star in range(1,st+1):
      print ('*',end="\t");
    if (i<=n//2):
      sp=sp-1
      st=st+2
    else:
      sp=sp+1
      st=st-2
    print("\n")
Pattern(n)
