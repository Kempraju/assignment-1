manu =int(input("enter the series"))
manu1 =int(input("enter the series"))
manu2=int(input("enter the series"))
manu3 =int(input("enter the series"))
count=0
count1=0
for i in [1,2,3,4,5,6,7,8,9]:
   if i%2==0:
      count+=1
   else :
      count1+=1
print(count," count of even number")
print(count1,"count of odd number")