def BTUtoPA(BTU):
    PA = BTU * 1055.0559
    print("PA = ",PA)
    
def SABTUtoSize(BTU):
    NoOfOuts = eval(input("Enter number of fans : "))
    Litre = BTU / (345.74 * NoOfOuts)
    if (48 >= Litre <= 70):
        print("Diameter's 150!")
    elif (71 >= Litre <= 125):
        print("Diameter's 200!")    
    elif (126 >= Litre <= 200):
        print("Diameter's 250!")    
    elif (201 >= Litre <= 250):
        print("Diameter's 300!")
    else:
        print("Diameter's 350!")

def RABTUtoSize(BTU):
    NoOfOuts = eval(input("Enter number of fans : "))
    Litre = BTU / (345.74 * NoOfOuts)
    if (48 >= Litre <= 84):
        print("Diameter's 150!")
    elif (85 >= Litre <= 151):
        print("Diameter's 200!")    
    elif (152 >= Litre <= 250):
        print("Diameter's 250!")    
    elif (251 >= Litre <= 311):
        print("Diameter's 300!")
    else:
        print("Diameter's 350!")
        
i = True
while i == True:
    x = eval(input("Enter your BTU : "))
    BTUtoPA(x)
    SARAEA = (str(input("Enter duct type ( SA // RA // EA ): ")))
    SARAEA = SARAEA.upper()
    if SARAEA == "SA":
        SABTUtoSize(x)
    if SARAEA == "RA":
        RABTUtoSize(x)
    iterate = input("Enter something if you're done : ")
    print(".\n.\n.\n.\n")
    if iterate != "":
        i = False
        
    
