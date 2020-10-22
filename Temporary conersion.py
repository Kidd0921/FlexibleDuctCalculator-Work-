i = True
while i == True:
    X = eval(input("Enter value of X: "))
    X = X * 100
    X = (X * 127) / 100
    X = X / 100
    X = ("%.2f" % X)
    print("X after conversion is: ",X + "m")
