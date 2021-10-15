operacao = input("Digite o calculo que deseja realizar (em notação polonesa, separado por espaços): ").split()

arquivo = open('./teste.txt', 'w')
arquivo.truncate()

def EscreveSoma(somador1, somador2):
  string = "li $t0 " + str(somador1) + "\n"
  string2 = "li $t1 " + str(somador2) + "\n"
  string3 = "add $t0 $t0 $t1 \n"
  arquivo.writelines(string) 
  arquivo.writelines(string2) 
  arquivo.writelines(string3) 
  resultado = int(somador1) + int(somador2)
  return str(resultado)

def EscreveSub(somador1, somador2):
  string = "li $t0 " + str(somador1) + "\n"
  string2 = "li $t1 " + str(somador2) + "\n"
  string3 = "sub $t0 $t0 $t1 \n"
  arquivo.writelines(string) 
  arquivo.writelines(string2) 
  arquivo.writelines(string3) 
  resultado = int(somador1) - int(somador2)
  return str(resultado)

def EscreveMulti(somador1, somador2):
  string = "li $t0 " + str(somador1) + "\n"
  string2 = "li $t1 " + str(somador2) + "\n"
  string3 = "multi $t0 $t0 $t1 \n"
  arquivo.writelines(string) 
  arquivo.writelines(string2) 
  arquivo.writelines(string3) 
  resultado = int(float(somador1)) * int(float(somador2))
  return str(resultado)
  
def EscreveDiv(somador1, somador2):
  string = "li $t0 " + str(somador1) + "\n"
  string2 = "li $t1 " + str(somador2) + "\n"
  string3 = "div $t0 $t0 $t1 \n"
  arquivo.writelines(string) 
  arquivo.writelines(string2) 
  arquivo.writelines(string3) 
  resultado = int(somador1) / int(somador2)
  return str(resultado)

def EscreveFator(somador1, somador2):
  string = "li $t0 " + str(somador1) + "\n"
  string2 = "li $t1 " + str(somador2) + "\n"
  string3 = "sub $t0 $t0 $t1 \n"
  arquivo.writelines(string) 
  arquivo.writelines(string2) 
  arquivo.writelines(string3) 
  resultado = int(somador1) - int(somador2)
  return str(resultado)

def EscreveRaiz(somador1, somador2):
  string = "li $t0 " + str(somador1) + "\n"
  string2 = "li $t1 " + str(somador2) + "\n"
  string3 = "sub $t0 $t0 $t1 \n"
  arquivo.writelines(string) 
  arquivo.writelines(string2) 
  arquivo.writelines(string3) 
  resultado = int(somador1) - int(somador2)
  return str(resultado)

def EscrevePotencia(somador1, somador2):
  string = "li $t0 " + somador1 + "\n"
  string2 = "li $t1 " + somador2 + "\n"
  string3 = "sub $t0 $t0 $t1 \n"
  arquivo.writelines(string) 
  arquivo.writelines(string2) 
  arquivo.writelines(string3) 
  resultado = int(somador1) - int(somador2)
  return str(resultado)

def Finaliza(resultado):
  string = "move $a0, $t0\n"
  string2 = "li $v0, 1\n"
  string3 = "syscall\n"
  arquivo.writelines(string) 
  arquivo.writelines(string2) 
  arquivo.writelines(string3) 
  print("resultado:" + str(resultado))

def VerificaDigito(digito, resultado, resultadoAnterior):
  if digito.isdigit():
    numeros.append(digito)
    global contador
    contador = contador + 1
  else:
    global x
    x = x + 1
    if digito == "+":
      if contador >= 2:
        contador = 0
        resultado = EscreveSoma(numeros[len(numeros)-2], numeros[len(numeros)-1])
        numeros.remove(numeros[len(numeros)-2])
        numeros.remove(numeros[len(numeros)-1])
      else:
        contador = 0
        if len(numeros) == 0:
          resultado = EscreveSoma(resultadoAnterior, resultado)
        else:
          resultado = EscreveSoma(resultado, numeros[len(numeros)-1])
          numeros.remove(numeros[len(numeros)-1])
    elif digito == "-":
      if contador >= 2:
        contador = 0
        resultado = EscreveSub(numeros[len(numeros)-2], numeros[len(numeros)-1])
        numeros.remove(numeros[len(numeros)-2])
        numeros.remove(numeros[len(numeros)-1])
      else:
        contador = 0
        if len(numeros) == 0:
          resultado = EscreveSub(resultadoAnterior, resultado)
        else:
          resultado = EscreveSub(resultado, numeros[len(numeros)-1])
          numeros.remove(numeros[len(numeros)-1])
    elif digito == "/":
      if contador >= 2:
        contador = 0
        resultado = EscreveDiv(numeros[len(numeros)-2], numeros[len(numeros)-1])
        numeros.remove(numeros[len(numeros)-2])
        numeros.remove(numeros[len(numeros)-1])
      else:
        contador = 0
        if len(numeros) == 0:
          resultado = EscreveDiv(resultadoAnterior, resultado)
        else:
          resultado = EscreveDiv(resultado, numeros[len(numeros)-1])
          numeros.remove(numeros[len(numeros)-1])
    elif digito == "*":
      if contador >= 2:
        contador = 0
        resultado = EscreveMulti(numeros[len(numeros)-2], numeros[len(numeros)-1])
        numeros.remove(numeros[len(numeros)-2])
        numeros.remove(numeros[len(numeros)-1])
      else:
        contador = 0
        if len(numeros) == 0:
          resultado = EscreveDiv(resultadoAnterior, resultado)
        else:
          resultado = EscreveMulti(resultado, numeros[len(numeros)-1])
          numeros.remove(numeros[len(numeros)-1])
    elif digito == "f":
      EscreveFator(numeros[len(numeros)-1])
    elif digito == "p":
      EscrevePotencia(numeros[len(numeros)-1])
    elif digito == "s":
      EscreveRaiz(numeros[len(numeros)-1])
  return resultado
  
numeros = []
resultado = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
contador = 0
x = 1
for i in range(len(operacao)):
  resultado[x] = VerificaDigito(operacao[i], resultado[x-1], resultado[x-2])
  print(resultado[x])
  if resultado[x] != resultado[x-1]:
    x = x + 1
  
Finaliza(resultado[x-1])

arquivo.close() 
