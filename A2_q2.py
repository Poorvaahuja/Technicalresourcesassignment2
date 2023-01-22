n=int(input('Enter the the total no. of rows to be printed:'))
for i in range(n,0,-1):
  for j in range(1,i+1):
    print('*', end= "\t");
  print(end="\n");
