n=int(input())
flag=False
if n==0 or n==1:
    print(n," is a prime number")
elif n>2:
    for i in range(2,n):
        if n%i==0:
            flag=True
if flag:
    print(n," is not a prime number")
else:
    print(a," is a prime number")