# SE INGRESAN LOS TRES NUMEROS POR EL USUARIO
from pickle import FALSE, TRUE
# INGRESO DE LAS VARIABLES
nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese edad: "))
estatura = float(input("Ingrese su estatura: "))
felicidad = input("¿Usted es feliz?(Verdad o Falso) : ")
# DEFINICION DEL VALOR BOOLEANO 
if(felicidad=="Verdad"):
    felicidad=True
elif(felicidad=="Falso"):
    felicidad=False
# PRESENTACION DEL RESULTADO 
if(felicidad):
    print("Mi nombre es ",nombre," tengo ",edad," años, mido ",estatura," metros y soy feliz")
else:
    print("Mi nombre es ",nombre," tengo ",edad," años, mido ",estatura," metros y no soy feliz")

