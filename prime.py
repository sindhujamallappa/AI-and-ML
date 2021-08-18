num=int(input("Enter a number"))
flag=0
for i in range(2,num//2):
    if num%i==0:
        flag = True
        break
    else:
        flag = False

if flag:
    print("Not Prime")
else:
    print("Prime")
