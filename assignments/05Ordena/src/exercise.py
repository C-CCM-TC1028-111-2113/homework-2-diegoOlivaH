def main():
    # Escribe el código adecuado para completar el programa
x = int(input("Input the first number: "))
y = int(input("Input the second number: "))
z = int(input("Input the third number: "))

if (x>y>z):
    print(z)
    print(y)
    print(x)

if (x>z>y):
    print(y)
    print(z)
    print(x)

if (y>x>z):
    print(z)
    print(x)
    print(y)

if (y>z>x):
    print(x)
    print(z)
    print(y)

if (z>y>x):
    print(x)
    print(y)
    print(z)

if (z>x>y):
    print(y)
    print(x)
    print(z)


if __name__=='__main__':
    main()
