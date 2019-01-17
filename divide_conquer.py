#4.1

# list = [1, 2, 3, 4]

# def sum(list):
#     if list == []:
#         return 0
#     else:
#         return list[0] + sum(list[1:])

# print(sum(list))


#4.2

# count = 0

# def count(list):
#     # count += 1
#     if list == []:
#         return 0
#     else:
#         return 1 + count(list[1:])

# x = count(list)
# # print(x)

# def countdown(x):
#     print(x)
#     if x <= 0:
#         return 
#     else:
#         return countdown(x - 1)

# print(countdown(4))


# list = [2, 3, 4]


# def count(list):
#     if list == []:
#         return 0
#     else:
#         return 1 + count(list[1:])

# x = count(list)

# list = [2, 4, 6]

def max(list):
    #base case: if length of list is 2:
    #return ele at list[0] if list[0] is greater than list[1]. Otherwise return ele at list[1]
    ###ie, the list is whittled down to two elements and you're going to find the biggest of the 2
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]

    #recursive call to function via a variable, 
    #recursive call uses max, which is a built-in function, starting at value 1 and continues through the len of the list
    sub_max = max(list[1:])
    import pdb; pdb.set_trace()
    #set up comparison: return list[0] if list[0] is greater than submax; otherwise return sub_max
    return list[0] if list[0] > sub_max else sub_max

    #In this ex, list[0] > sub_max so return sub_max and go thru the function again and stop at the first conditional, since len(list) now == 2
x = max(list)



# list = [2, 4, 6]
# sub_max = max(list[1:])
