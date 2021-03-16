# we give "a" as 2nd parameter in open function
# to tell open() to append the text & not overwrite
# append means writing below already existing

f = open("someFile.txt", "a")

for x in range(0, 11):
    if(x == 0):
        continue
    f.write("\nThis is Appended text and line # is " + str(x))
