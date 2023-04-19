import os
os.system("clear")


a = [
    [
    [1,2,3],
    [4,5,6]
    ],
    [
    "a"
    ]
]


def flatten(data):
    res = []

    if type(data) is list:
        for elem in data:
            res = res + flatten(elem)
        else:
            res.append(data)
        
    return res
    
r = flatten(a)
print(r)