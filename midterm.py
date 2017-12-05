import sys
import math
counter=0
add=0
def b(var):
    global counter
    counter+=1
    var=var.strip()
    return var

def c(var):
    var=var[0].strip()
    addwholepart(var)
    return var 
    
def addwholepart(no):
          int(no)
          c=0
          print(no)
          for i in no:
              name=sys.argv[1]
              fopen=open(name)
              for var in fopen.read().split(" "):
                  rs1=b(var)
                  var1=var.split(".")
                  res2=c(var1)
                  res2=int(res2)
    
print("total numbrs:",counter-1)
print("addition:",add)

