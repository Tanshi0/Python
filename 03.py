#import os
#os.system("clear")

#def foo(*a):
    #for i in range(len(a[0])):
        #if a[0[i]]==5:
            #a[0[i]]=3
        #print("---",a)

#test = [1,2,3,4,5,5,5]
#print(test)

#foo(test)
#print(test)


'''import os
os.system("clear")

a = [1,2,3,4,5]
print(a)
print(*a)#raspakovka spiska'''


import os
os.system("clear")
person = {
    "name":"Natalya",
    "age": 17
}
def foo(name, age):
    print(f"your name is {name} and your age is {age}")

foo(**person)
