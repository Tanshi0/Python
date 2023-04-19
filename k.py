

# a = [
#     [
#     [1,2,3],
#     [4,5,6]
#     ],
#     ["a"]
# ]

# def foo(data, mass=[]):
#     if type (data) is list:
#         for d in data:
#             foo(d)
#         else:
#             mass.insert(0, data)
#         return mass
# print(foo(a))

# n=28


# def find_perfect_sum():
#     for i in range(1,28):
#             sum=0
#     for i in range(1, n//2):
#             if 
#             sum+=1
#         else:
#             if sum==28:
#                 return sum

# find_perfect_sum()
        

n=28
def find_perfect_sum(n):
    sum = 0
    for i in range(1, (n//2)+1):
        if n//i==0:
            sum +=i
        if n ==sum:
            if i// n == 0:
                print("pxfmvlf")

find_perfect_sum(n)
print (find_perfect_sum(n))

# def is_prime(mass):
#     mass=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#     for i in mass:
#         if i <2:
#             continue
#     is_prime=True
#     for j in range(2, int (i**0.5)+1):
#         if i% j==0:
#             is_prime=False
#             break
#         if is_prime:
#             print(i) 
# print(is_prime(mass=[]))


# mass=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# def is_prime(numb):
#     if type(numb) in list:
#         for i in range(2,20):
#             if i+i in numb:
#                 mass.remove(i+i)
#             if i**2 in numb:
#                 mass.remove(i*i)
# is_prime(mass)
# print(mass)
    

#import os
#os.system("clear")

#def foo(*a):
    #for i in range(len(a[0])):