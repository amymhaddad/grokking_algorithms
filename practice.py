
# arr = [5, 2, 4, 9, 10]

# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0

#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index

# x = findSmallest(arr)

# def selectionSort(arr):
#     newArr = []

#     for i in range(len(arr)):
#         # import pdb; pdb.set_trace()
#         smallest = findSmallest(arr)
#         #smallest = 1 1 0 0 0 ---> the index of each of the smallest numbers, one at a time
#         newArr.append(arr.pop(smallest))
         
#     return newArr

# y = selectionSort(arr)

# print(y)


list = [2, 6, 10, 13]
item = 6

def binary_search(list, item):
    """If item in list, return position"""

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess < item:
            low = mid + 1

        else:
            high = mid - 1

    return None

print(binary_search(list, item))


# def greet(name):
#     print(f"Hello, {name}")
#     greet2(name)
#     print("Getting ready to say bye")
#     bye()

# def greet2(name):
#     print(f"How are you, {name}?")

# def bye():
#     print("ok, bye!")

# greet('maggie')

# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x -1)

# print(fact(3))

# i = 3
# def countdown(i):
#     print(i)
#     if i <= 0:
#         return
#     else:
#         countdown(i - 1)

# x = countdown(i)
# print(x)


# list = [2, 4, 6, 8]
# item = 6

# low = 0
# high = len(list) - 1

# mid = (low + high) // 3
# print("mid", mid)
# guess = list[mid]

# print(guess)