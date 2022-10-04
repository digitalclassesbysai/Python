a = int(input("Enter an integer:"))
count = 0
for i in range(2,a,1):
  if(a%i==0):
    count = count + 1

if(count==2):
  print("Prime")
else:
  print("Not Prime")
