# Using break to get out of loop
for x in range(0, 5):
    if(x >= 3):
        break
    print(x)


print("")
print("")

# Using continue to skip something in a loop
for y in range(1, 11):
    if(y % 2 == 0):
        continue
    print(y)
