def main():
    #escribe tu código abajo de esta línea
print("Bigger Number indicator")

n1 = int(input("Input number 1: "))
n2 = int(input("Input number 2: "))
n3 = int(input("Input number 3: "))

if (n1>n2) and (n1>n3):
    print("The biggest number is",n1)

if (n2>n1) and (n2>n3):
    print("The biggest number is",n2)

if (n3>n2) and (n3>n1):
    print("The biggest number is",n3)


if __name__=='__main__':
    main()
