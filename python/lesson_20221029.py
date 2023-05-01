
## 1. Defs and Lambdas

def double_def(x):
    return x * 2

double_lambda = lambda x: 2*x

print(double_def(5))
print(double_lambda(5))

## 2. Functions that make functions
def make_multiplier(n):
    return lambda x: x*n

double_func = make_multiplier(2)
triple_func = make_multiplier(3)
print(double_func(5))
print(triple_func(5))

## Partial application

# Haskell
#  add x y = x + y
#  add1 = add 1
#  add1 5 # evaluates to 6

# Python:
def add(x, y):
    return x + y
add1 = lambda x: add(x, 1)
#def add1(x):
#    return add(x, 1)
add1(5) # evaluates to 6

## 3. Scoping

# Define n in the global scope
n = 6
def add_n(x):
    # has a parameter, x, which is in the local scope
    # references n from the outer (global) scope
    return x + n

print("Add n")
print(add_n(1))
n = 10
print(add_n(1))


## 4. Functions like classes

def PersonFuncClass(first_name, last_name):
    def get_full_name():
        return first_name + ' ' + last_name
    def set_first_name(new_first_name):
        nonlocal first_name
        first_name = new_first_name
    return get_full_name, set_first_name


# The PersonFuncClass function returns a 2-tuple
# Use tuple assignment syntax for convenience/readability
steve_full_name, steve_set_name = PersonFuncClass("Steven", "Mitchell")
print(steve_full_name())
steve_set_name("Bob")
print(steve_full_name())

# Or, without the syntactic sugar:
#steve_tuple = PersonFuncClass("Steven", "Mitchell")
#print(steve_tuple[0]())
#steve_tuple[1]("Bob")
#print(steve_tuple[0]())

# Demonstrate that we can use it to make different instances
dan_full_name, dan_set_name = PersonFuncClass("Daniel", "Gajeski")
print(dan_full_name())
dan_set_name("Billy")
print(dan_full_name())

## 5. More on scopes

# nonlocal experiment
def outer(x):
    def inner1():
        x = 10
        def inner2():
            nonlocal x
            x += 1
            print(x)



