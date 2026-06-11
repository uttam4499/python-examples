myfile = open("Uttam.txt",'a')
myfile.write("Hello world!")
myfile.close()

myfile2 = open("Uttam.txt",'r')
content = myfile2.read()
print(content)
myfile2.close()