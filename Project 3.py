total=1
num1=1
num2=0
fnum=0

while fnum<4000000:
    num1=num2
    num2=total
    total=num1+num2

    if total%2==0:
        fnum+=total
print(fnum)
