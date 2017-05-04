# Variable numebr of ordered arguments

def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

# Variable number of keyword arguments

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

# Variable number of arguments with default values
def do_this(*args):
    if not args: args = (2, 5, 21)

# or

def do_thtat(a=2, b=5, c=21, *args):
    args = (a,b,c)+args   

# Exercise

# edit the functions prototype and implementation
def foo(a, b, c, *more):
    return len(more)

def bar(a, b, c, **extra):
    if extra.get("magicnumber") == 7:
        return True
    return False


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")