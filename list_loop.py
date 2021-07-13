numbers=[]
num=int(input("Enter the numbers to be added in list: "))
for i in range(num):
    n=int(input("Enter number{}:".format(i+1)))
    numbers.append(n)
print(numbers)
      
for j in numbers:
    if(j>0):
        print(j)
        
