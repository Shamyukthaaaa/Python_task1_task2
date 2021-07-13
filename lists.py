numbers=[]
num=int(input("Enter the numbers to be added in list: "))
for i in range(num):
    n=int(input("Enter numbers{}:".format(i+1)))
    numbers.append(n)
print(numbers)

positive_num=[]
for j in numbers:
    if(j>0):
        positive_num.append(j)
print(positive_num)
