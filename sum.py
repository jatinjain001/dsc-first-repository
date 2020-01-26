n=int(input("Enter the number="))
summ=int(0)
while n>0:
    b=n%10
    summ+=b
    n=n/10
print(summ)
