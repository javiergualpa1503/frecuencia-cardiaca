numeros = []

while True:
  entrada  = input('Introduce tu numero o finish para terminar: ')

  if entrada  == 'finish':
    break
  else:
    try:
      numero = float(entrada )
      numeros.append(numero)
    except ValueError:
      print('valor no valido')

if numeros:
  promedio = sum(numeros) / len(numeros)
  resultado = promedio * 4
  print(f"El resultado es: {resultado} pulsaciones por minuto:", )
else:
  print("No se ingresaron números.")
  
# print(numeros)