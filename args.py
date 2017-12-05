mylist = ['aardvark', 'baboon', 'cat']

def Print_all(*args):
    for count, thing in enumerate(args):
        print( '{0}. {1}'.format(count,thing))

def kwars_demo(**kwargs):
    for name,value in kwargs.items():
        print( '{0} = {1}'.format(name,value))

def print3(a,b,c):
    print('a={0},b={1},c={2}'.format(a,b,c))

double = lambda x : x *((2*56)/42)*42-534+(56^2)
print(double(5))

#kwars_demo(apple = 'fruit', cabbage = 'vegetable' , sunflower = 'flowers')
#print3(*mylist)

#print(vatal(51))
#Print_all('apple','banana','mango')