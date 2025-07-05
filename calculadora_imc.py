#variables
saludo = 'Hola, te damos la bienvenida a la calculadora de IMC (Índice de masa corporal). Para poder obtenerlo, por favor sigue las siguientes indicaciones.'
print(saludo)
nombre = input('Introduce tu nombre: ')
apellido_p = input ('Introduce tu apellido paterno: ')
apellido_m = input ('Introduce tu apellido materno: ')
edad= int(input('¿Cuántos años tienes?: '))
peso = float (input('Introduce tu peso en kilogramos. Puedes colocar un decimal: '))
estatura = float(input('Introduce tu estatura en metros: '))
imc = (peso)/(estatura * estatura)
#definimos que tipo de variable serán para evitar se introduzcan datos erroneos. 
#textos
# print(nombre)
# print(apellido_p)
# print (apellido_m)
# print (edad) no es necesario el print, ya se ejecuta con el input de arriba
print ('\nGracias. A continuación estará mostrandose tu información e IMC calculado.' + '\n\nInformación para: ' + nombre + " " + apellido_p + " " + apellido_m +'\nEdad: ' + str(edad) + ' años'+ '\nTu IMC es de:' + str(round(imc,1)))
print("""De acuerdo con ISSTE, el IMC puede brindar indicios sobre la condición de salud en la que se encuentra la persona.

Menor a 18.9 = Peso bajo

18.50 a 24.99 = Peso normal

25.00 a 29.99 = Sobrepeso

30.00 a 34.99 = Obesidad leve

35.00 a 39.99 = Obesidad media

Mayor a 40.0 = Obesidad mórbida

Fuente: ¿Qué es el índice de masa corporal? gob.mx. Recuperado el 26 de junio de 2025, de https://www.gob.mx/issste/articulos/que-es-el-indice-de-masa-corporal""")