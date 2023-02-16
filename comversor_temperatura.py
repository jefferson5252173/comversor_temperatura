#programa para convertir una cantidad dada de grados centigrados a su equivalente en grados fahrenheit

Print("----------------------------")
print("--conversor de temperatura--")
Print("----------------------------")

# input
c = int(input(" digite el valor de c: "))

#processing
F =(c * 1.8 + 32)
k =(c + 273.15)

#output
Print("----------------------------")
print("---------resultado----------")
Print("----------------------------")
Print("la convercion de " + str(c)+" grados celcius a grados fahrenheit es") + str (F)
print("La convercion de " + str(c)+" grados celcius a grados kelvin es") + str (k)





