prime_factor=600851475143
i=2
while prime_factor!=1:
    rem=prime_factor%i
    if rem==0:
        prime_factor//=i
        print(i)
    else:
        i+=1
