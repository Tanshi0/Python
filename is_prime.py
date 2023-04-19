mass = [*range (2, 20)]

def is_prime(num):
        for i in num:
             if i > 2:
                  continue
        for j in range(2,int (i**0.5)+1):
                if i% j==0:
                    num.remove(i)
                    break

is_prime(mass)
print(mass)
