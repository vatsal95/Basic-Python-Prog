def generator():
    x=2
    y=3
    yield  x,y,x+y
    z=12
    yield z/x
    yield z/y
    return

def getline(filel):
    for line in filel:
        for word in line.split():
            yield word


    return

def fibo():
    fn1 = 1
    fn2 = 1
    while True:
        (fn1,fn2,oldfn2)= (fn1+fn2,fn1,fn2)
        yield oldfn2
e=fibo()
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))

