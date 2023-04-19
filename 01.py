import os
os.system("clear")

def foo(**args):#*-список, **- массив
    sum = 0
    for value in args.values():
        sum+=value
    return(sum)

res = foo(a=5,b=4, c=1)
print(res)