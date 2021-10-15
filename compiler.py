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
  resultado = int(somador1) * int(somador2)
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
  print("resultado:" + resultado)

def VerificaDigito(digito, resultado):
  if digito.isdigit():
    numeros.append(digito)
    global contador
    contador = contador + 1
    # print(numeros)
    # print(contador)
  else:
    if digito == "+":
      if contador >= 2:
        contador = 0
        resultado = EscreveSoma(numeros[len(numeros)-2], numeros[len(numeros)-1])
        numeros.remove(numeros[len(numeros)-2])
        numeros.remove(numeros[len(numeros)-1])
      else:
        contador = 0
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
resultado = 0
contador = 0
for i in range(len(operacao)):
  resultado = VerificaDigito(operacao[i], resultado)
  
Finaliza(resultado)

arquivo.close() 
