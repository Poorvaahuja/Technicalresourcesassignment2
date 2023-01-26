n = int(input('Enter the the total no. of rows to be printed:'))
num=1
for i in range(n):
  for j in range(i+1):
    print(num,end="\t")
    num=num+1
  print("\n")
