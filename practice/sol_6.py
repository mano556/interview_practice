import cProfile
def sum(a,b):
    return a+b
cProfile.run("sum")