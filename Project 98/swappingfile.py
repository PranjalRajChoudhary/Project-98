def swapFileData():
    file1name = input("Enter file 1 name")
    file2name = input("Enter file 2 name")

    file1 = open(file1name)
    data_a = file1.readlines()


    file2 = open(file2name)
    data_b = file2.readlines()

    a = open(file1name,'w')
    a.writelines(data_b)

    b = open(file2name,'w')
    b.writelines(data_a)


swapFileData()
