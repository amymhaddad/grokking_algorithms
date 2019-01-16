#4.1

list = [1, 2, 3, 4]

def sum(list):
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])

# print(sum(list))


#4.2

# count = 0

def count(list):
    # count += 1
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])

x = count(list)
# print(x)

def countdown(x):
    print(x)
    if x <= 0:
        return 
    else:
        return countdown(x - 1)

print(countdown(4))