print("Ingrese su edad")
num =int(input())

if num > 10 and num <= 18:
    print ("Usted tiene ", num , "El costo de su boleto es $1000")
elif num > 18 and num <= 65:
    print ("Usted tiene ", num , "El costo de su boleto es $2000")
elif num > 65:
    print ("El costo de su boleto es ", num, "El costo de su boleto es $1500")
else: 
    print ("Usted tiene ", num , "El costo de su boleto es GRATIS")

