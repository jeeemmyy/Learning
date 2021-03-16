# To open existing file or create one if does not exists already
# open() takes 2 parameters
# 1st parameter takes path
# 2nd parameter write/read abilities
# & '+' means create a new file if it does not exist already
f = open("someFile.txt", "w+")


# write() writes into file | Takes Only 1 Parameter
for x in range(1, 11):
    f.write("This is some text & line # is " + str(x) + "\n")


# close() is used to close the file which was opened by open() function
f.close()
