

def openfile():

    global list1
    file1 = open('mydata.txt','r')
    str = (file1.read())
    list1 = str.split(" ",str.count(" "))
    print(list1)

def countno():
    count = 0

    for x in list1:
        count += 1
    print(count)


def total():
    total=0
    avg = 0
    couter = 0
    try:
        mylist = []
        for item in list1:
            mylist.append(float(item))
    except ValueError:
        pass
    finally:
        print(mylist)
        global floatlist
        floatlist = mylist
        for item in mylist:
            total += item
            couter += 1
        print(total)
        avg = (total/couter)
        print(avg)

def minmax():
    maxi = max(floatlist)
    mini = min(floatlist)

    print(mini)
    print(maxi)

def igonredecimals():
    intsum = 0
    try:
        intlist = []
        for items in floatlist:
            intlist.append(int(items))
    except ValueError:
        pass
    finally:
        print(intlist)

        for x in intlist:
            intsum += x
        print(intsum)

def cleanlist():
    cleanlst = ""
    for char in floatlist:
        if char.isdigit() or char.isdecimal():
            cleanlst += char
        else:
            cleanlst +=""
        print(cleanlst)


def sortedlist():
    sortlist = floatlist
    sortlist.sort()
    print(sortlist)

openfile()
countno()
total()
minmax()
igonredecimals()
#cleanlist()
sortedlist()


