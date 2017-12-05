def errorincode():

        try:
            x=int(input("Enter the number"))

            ans=(8/x)
            print(ans)

        except:
            var = str(x)
            print("The division of 8 and " + var + " is not possible")
            print("that", "is", " cool ", sep=' \t\t')

errorincode()