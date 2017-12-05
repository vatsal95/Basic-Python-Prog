def Openfile():
    file1 = open('newfile.txt','a')
    file1.write("hey \n")
    file1.write("how  \n")
    file1.write("are \n")
    file1.write("youu \n")

    file1.write("Write in file \n")
    print(file1.tell())

Openfile()
