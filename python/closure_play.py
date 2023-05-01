
def closure_play1_lambda():
    print("Closure closure_play1_lambda - start!")
    closures = []
    for i in range(0, 10):
        closures.append(lambda: "Value is {}".format(i))
    # Uncomment this and it'll change the value of `i` that is used above
    # i = "lol"
    print("Closure closure_play1_lambda - end!")
    return closures

def closure_play2_def():
    print("Closure closure_play2_def - start!")
    closures = []
    for i in range(0, 10):
        def closure():
            return "Value is {}".format(i)
        closures.append(closure)
    print("Closure closure_play2_def - end!")
    return closures

def closure_play3_def_copy():
    print("Closure closure_play3_def_copy - start!")
    closures = []
    for i in range(0, 10):
        def make_closure(i2):
            return lambda: "Value is {}".format(i2)
        closures.append(make_closure(i))
    print("Closure closure_play3_def_copy - end!")
    return closures


f = closure_play2_def
f = closure_play1_lambda
#f = closure_play3_def_copy
print("Using {}".format(f))
my_closures = f()

print("0: ", my_closures[0])
print("0 called: ", my_closures[0]())

print("1: ", my_closures[1])
print("1 called: ", my_closures[1]())

print("9: ", my_closures[9])
print("9 called: ", my_closures[9]())
