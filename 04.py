'''import os
os.system("clear")

def foo(a):
    a = [*a]
    for i in range(len(a)):
        if a [i]==5:
            a[i]=3
    return(a)

test = [1,2,3,4,5]

res = foo(test)

print(res)
print(test)'''

import os
os.system("clear")



a = [
    [
    [1,2,3],
    [4,5,6]
    ],
    ["a"]
]

def reversed_list(a):
        reversed (a)
        a.reverse()
        print(*a[0])
        for item in a:
            item.reverse()
        for sub_item in item:
              sub_item.reverse()
              print(*sub_item, sep="\n", end="\n")

reversed_list(a)



# def foo(l, res):
#       if type(l) in list:
#         for e in l:
#              foo(e)
#         else:
#              print(a)
            
             



# def foo(date):
#     if type (date) is list:
#         for d in date:
#             foo(d)
#     else:
#         print (date)

# foo(a)
