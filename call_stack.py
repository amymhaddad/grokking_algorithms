

def greet2(name):
    print(f"How are you, {name}?")

def bye():
    print("ok, bye")

def greet(name):
    print(f"Hello, {name}!")
    #Next function call; computer allocates box of memory
    greet2(name)
    print("Getting ready to say bye...")
    bye()

greet('maggie')
#call funtion -- GREET -- and computer allocates box of memory for function call
#NAME is set to "maggie" so it needs saved in memory
#Computer saves values for all variables in function call


#stack call
#call function greet(name) and computer allocates a box of memory. The variable "name" is set to "maggie", which needs saved to memory
#call second function greet2(name), and computer allocates a box of memory
#computer runs greet2(name), which causes this box of memory to "pop" off from the top of the stack and we're back to the "greet(name)" function

###the greet(name) function was partially completed: when you call a function within a function, the calling function(greet(name)) is paused in a partially complete state

#back to greet(name), a line is printed and another function is called: bye(). This function is added to the call stack.