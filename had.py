import random

list=[]
for i in range(10):
    num=random.randint(1,8)
    num2=random.randint(1,8)
    while (num,num2) in list:
        num=random.randint(1,8)
        num2=random.randint(1,8)
    list.append((num,num2))
    
print(list)