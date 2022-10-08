# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, 8]



# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, c: a*c, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))




o = [20,30,100,60,80,90]

#1 
print()
print(functools.reduce((lambda x,y:35*x+y),o)) # returns 380
#2
functools.reduce((lambda x,y,z=10:x+y+z),o) # returns 430 