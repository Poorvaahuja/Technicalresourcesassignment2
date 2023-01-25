n=int(input('Enter the the total no. of rows to be printed:'))
def Pattern(n):
  st=n
  sp=0
  for i in range(1,n+1):
    for space in range(1,sp+1):
      print(end="\t");
    for star in range (1,st+1):
      print('*', end="\t");
    st=st-1
    sp=sp+1
    print(end="\n");
Pattern(n)
