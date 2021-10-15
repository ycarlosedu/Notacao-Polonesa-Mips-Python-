import math
operacao = input("Digite o calculo que deseja realizar (em notação polonesa, separado por espaços): ").split()

arquivo = open('./teste.txt', 'w')
arquivo.truncate()

def EscreveSoma(somador1, somador2):
	string = "    li $t0, " + str(somador1) + "\n"
	string2 = "    li $t1, " + str(somador2) + "\n"
	string3 = "    add $t0 $t0 $t1 \n"
	arquivo.writelines(string) 
	arquivo.writelines(string2) 
	arquivo.writelines(string3) 
	resultado = int(float(somador1)) + int(float(somador2))
	return str(resultado)

def EscreveSub(somador1, somador2):
	string = "    li $t0, " + str(somador1) + "\n"
	string2 = "    li $t1, " + str(somador2) + "\n"
	string3 = "    sub $t0 $t0 $t1 \n"
	arquivo.writelines(string) 
	arquivo.writelines(string2) 
	arquivo.writelines(string3) 
	resultado = int(float(somador1)) - int(float(somador2))
	return str(resultado)

def EscreveMulti(somador1, somador2):
	string = "    li $t0, " + str(somador1) + "\n"
	string2 = "    li $t1, " + str(somador2) + "\n"
	string3 = "    mult $t0 $t0 $t1 \n"
	arquivo.writelines(string) 
	arquivo.writelines(string2) 
	arquivo.writelines(string3) 
	resultado = int(float(somador1)) * int(float(somador2))
	return str(resultado)
	
def EscreveDiv(somador1, somador2):
	string = "    li $t0, " + str(somador1) + "\n"
	string2 = "    li $t1, " + str(somador2) + "\n"
	string3 = "    div $t0 $t0 $t1 \n"
	arquivo.writelines(string) 
	arquivo.writelines(string2) 
	arquivo.writelines(string3) 
	resultado = int(float(somador1)) / int(float(somador2))
	return str(resultado)

def EscreveFator(somador1):
	string = "    li $s0, " + str(somador1) + "\n"
	string2 = "    bgt $s0, 1, primeiramult\n    j exitloop\nfatorial:\n    bgt $s0, 1, recursao\n    j exitloop\nprimeiramult:\n    subi $s1, $s0, 1\n    mult $s0, $s1 \n    mflo $t0\n    subi $s0, $s0, 2\n    j fatorial\nrecursao:\n    mult $t0, $s0\n    mflo $t0\n    subi $s0, $s0, 1\n    j fatorial\nexitloop:\n"
	arquivo.writelines(string) 
	arquivo.writelines(string2) 
	resultado = math.factorial(int(float(somador1)))
	return str(resultado)

def EscrevePotencia(potencia, somador1):
	string = "li $t0 " + str(somador1) + "\n"
	string3 = "sub $t0 $t0 $t1 \n"
	arquivo.writelines(string) 
	arquivo.writelines(string3) 
	resultado = math.pow(int(float(somador1)), int(potencia))
	return str(resultado)

def EscreveRaiz(somador1):
	string = "li $t0 " + str(somador1) + "\n"
	string3 = "sub $t0 $t0 $t1 \n"
	arquivo.writelines(string) 
	arquivo.writelines(string3) 
	resultado = math.sqrt(int(float(somador1)))
	return str(resultado)

def Finaliza(resultado):
	string = "    move $a0, $t0\n"
	string2 = "    li $v0, 1\n"
	string3 = "    syscall\n"
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
					resultado = EscreveMulti(resultadoAnterior, resultado)
				else:
					resultado = EscreveMulti(resultado, numeros[len(numeros)-1])
					numeros.remove(numeros[len(numeros)-1])
		elif digito == "f":
			contador = 0
			if len(numeros) == 0:
				resultado = EscreveFator(resultado)
			else:
				resultado = EscreveFator(numeros[len(numeros)-1])
				numeros.remove(numeros[len(numeros)-1])
		elif digito == "p":
			contador = 0
			if len(numeros) == 0:
				resultado = "impossivel calcular, informe o valor da potencia!"
			else:
				resultado = EscrevePotencia(numeros[len(numeros)-1], resultado)
				numeros.remove(numeros[len(numeros)-1])
		elif digito == "s":
			contador = 0
			if len(numeros) == 0:
				resultado = EscreveRaiz(resultado)
			else:
				resultado = EscreveRaiz(numeros[len(numeros)-1])
				numeros.remove(numeros[len(numeros)-1])
	return resultado
	
numeros = []
resultado = [0]*(len(operacao)+3)
contador = 0
x = 1
for i in range(len(operacao)):
	resultado[x] = VerificaDigito(operacao[i], resultado[x-1], resultado[x-2])
	print(resultado)
	if resultado[x] != resultado[x-1]:
		x = x + 1

Finaliza(resultado[x-1])

arquivo.close() 
