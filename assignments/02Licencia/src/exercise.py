
def main():
    #Escribe tu código debajo de esta línea
print("Information to get your Driving License")
e = int(input("Input your age: "))
if (e < int(18) and e > int(0)):
    print("You don't have the requirements")

if (e<=0):
    print("Wrong Answer")
if (e>=18):
    ID=str(input("Do you have an ID? (Y/N)"))

if (e>= 18 and ID== str("N")):
        print("You don't have the requirements")
if(e>= 18 and ID== str("Y")):
        print("Licensing procedure granted")
if not (e>=18 and((ID== str("N"))or (ID== str("Y")))):
        print("Wrong Answer")

if __name__ == '__main__':
    main()
