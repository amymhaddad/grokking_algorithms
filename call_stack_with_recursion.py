# def fact(x):
#     if x == 1:
#         return 1    
#     else:
#         return x * fact(x - 1)

# print(fact(3))


def countdown(i):
    print(i)
    if i <=0:
        return
    else:
        countdown(i-1)

print(countdown(3))

i = 3

# def countdown(i):
#    print(i)
#    if i <= 0:
#        return
#        #--->base case 
#    else:
#        countdown(i-1)
#        #--->recursive case

# x = countdown(i)
# print(x)