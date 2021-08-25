def main():
    #escribe tu código abajo de esta línea
w = float(input("Weight in kg: "))
h = float(input("Height in m: "))
if (w<=0 or h<=0):
    print("Check your values, they might be wrong")

if (w>0 and h >0):
    BMI = w/(h**2)
if (w> 0 and h>0 and(BMI < int(20) and BMI > int(0))):
    print("UNDERWEIGHT")
if (w> 0 and h>0 and(BMI < int(25) and BMI >= int(20))):
    print("NORMAL WEIGHT")
if (w> 0 and h>0 and(BMI < int(30) and BMI >= int(25))):
    print("OVERWEIGHT")
if (w> 0 and h>0 and(BMI < int(40) and BMI >= int(30))):
    print("OBESITY")
if (w> 0 and h>0 and(BMI >= int(40))):
    print("MORBID OBESITY")


if __name__=='__main__':
    main()
