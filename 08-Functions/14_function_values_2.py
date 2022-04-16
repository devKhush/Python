def anyFunc(a):
    # for mutables objects, the function calls are call by reference

    a[1] = 10
    a.append(100)


l = [1, 2, 3]
print(l)
anyFunc(l)
print(l)

'''
For Immutable objects (like Integer, String), new objects (new instances/variables with diff. addresses) are
created when their values are changed inside the functions. 

For Mutable objects (like List, Set), if any changes are done with them inside the functions, then changes are 
reflected back in the original objects outside the functions.  
'''
