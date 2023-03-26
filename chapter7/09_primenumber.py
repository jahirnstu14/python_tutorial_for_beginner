num = int(input("enter the value of integer number"))
prime=False
for i in range(2,num):
    if (num%i==0):
        prime=True
        break

if prime:
    print("this not prime number")
else:
    print("prime number")