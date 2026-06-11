with open("indus.txt","a") as myfile:
    mydata = myfile.write("\n Hello")

    with open("indus.txt","r") as myfile:
        mydata = myfile.read()
print(mydata)