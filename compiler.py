import math
operacao = input("Digite o calculo que deseja realizar (em notação polonesa, separado por espaços): ").split()

arquivo = open('./teste.txt', 'w')
arquivo.truncate()

string = '.data\n    resultado: .word 0\n    resultado2: .word 0\n    error_raiz: .asciiz "Nao e uma raiz quadrada perfeita"\n\n.text\n    move $t0, $zero'
arquivo.writelines(string) 

def VerificaSeUsaResultado(ComResultado, somador1, somador2):
  if ComResultado == 2:
    string = "\n    sw $t0, resultado2\n    lw $t0, resultado\n"
    string2 = "    lw $t1, resultado2\n"
  elif ComResultado == 1:
    string = "\n    sw $t0, resultado\n    lw $t0, resultado\n"
    string2 = "    li $t1, " + str(somador2) + "\n"
  else:
    string = "\n    sw $t0, resultado\n    li $t0, " + str(somador1) + "\n"
    string2 = "    li $t1, " + str(somador2) + "\n"
  arquivo.writelines(string)
  arquivo.writelines(string2) 
  return

def EscreveSoma(somador1, somador2, ComResultado):
	string = "\n\n#ALGORITMO SOMA\n"
	arquivo.writelines(string)
	VerificaSeUsaResultado(ComResultado, somador1, somador2)
	string3 = "\n    add $t0 $t0 $t1\n"
	arquivo.writelines(string3)
	resultado = int(float(somador1)) + int(float(somador2))
	return str(resultado)

def EscreveSub(somador1, somador2, ComResultado):
	string = "\n\n#ALGORITMO SUBTRACAO\n"
	arquivo.writelines(string)
	VerificaSeUsaResultado(ComResultado, somador1, somador2)
	string3 = "\n    sub $t0 $t0 $t1\n"
	arquivo.writelines(string3) 
	resultado = int(float(somador1)) - int(float(somador2))
	return str(resultado)

def EscreveMulti(somador1, somador2, ComResultado):
	string = "\n\n#ALGORITMO MULTIPLICACAO\n"
	arquivo.writelines(string) 
	VerificaSeUsaResultado(ComResultado, somador1, somador2)
	string3 = "    mul $t0, $t0, $t1\n"
	arquivo.writelines(string3) 
	resultado = int(float(somador1)) * int(float(somador2))
	return str(resultado)
	
def EscreveDiv(somador1, somador2, ComResultado):
  string = "\n\n#ALGORITMO DIVISAO\n"
  arquivo.writelines(string) 
  VerificaSeUsaResultado(ComResultado, somador1, somador2)
  string3 = "    div $t0 $t1\n    mflo $t0\n"
  arquivo.writelines(string3) 
  resultado = int(somador1) / int(somador2)
  resultado = RetiraPontosDecimais(resultado)
  return str(resultado)

def EscreveFator(somador1, ComResultado):
	string = "\n\n#ALGORITMO FATOR\n"
	arquivo.writelines(string)
	if ComResultado == 1:
		string2 = "\n    sw $t0, resultado\n    lw $s0, resultado\n"
	else:
		string2 = "    sw $t0, resultado\n    li $s0, " + str(somador1) + "\n"
	string3 = "    bgt $s0, 1, primeiramult\n    j exitloop\nfatorial:\n    bgt $s0, 1, recursao\n    j exitloop\nprimeiramult:\n    subi $s1, $s0, 1\n    mult $s0, $s1 \n    mflo $t0\n    subi $s0, $s0, 2\n    j fatorial\nrecursao:\n    mult $t0, $s0\n    mflo $t0\n    subi $s0, $s0, 1\n    j fatorial\nexitloop:\n"
	arquivo.writelines(string2) 
	arquivo.writelines(string3) 
	resultado = math.factorial(int(float(somador1)))
	return str(resultado)

def EscrevePotencia(potencia, somador1):
	string = "\n\n#ALGORITMO POTENCIA\n"
	string2 = "    sw $t0, resultado\n    j MAINPOTENCIA\nMULTIPLICAR:\n    addi $t3,$zero,1\n    add $t4,$zero,$a2\n    LOOP_2:\n    slt $t5,$t3,$a3\n    beq $t5,$zero,FIM2\n    add $t4,$t4,$a2\n    addi $t3,$t3,1\n    j LOOP_2\nFIM2:\n    add $v1,$zero,$t4\n    jr $ra\nEXPOENTE:\n    li $t0,1\n    li $t1,0\n    add $t9,$ra,$zero\nLOOP:\n    slt $t2,$t1,$a1\n    beq $t2,$zero,FIM\n    addi $t1,$t1,1\n    move $a2,$t0\n    move $a3,$a0\n    jal MULTIPLICAR\n    add $t0,$v1,$zero\n    j LOOP\nFIM:\n    move $v0,$t0\n    jr $t9\nMAINPOTENCIA:\n    lw $a0, resultado\n    li $a1, " + potencia + "\n    jal EXPOENTE\n    add $s2,$v0,$zero\n"
	arquivo.writelines(string) 
	arquivo.writelines(string2) 
	resultado = math.pow(int(float(somador1)), int(potencia))
	resultado = RetiraPontosDecimais(resultado)
	return str(resultado)

def EscreveRaiz(somador1, ComResultado):
	string = "\n\n#ALGORITMO RAIZ\n"
	arquivo.writelines(string)
	if ComResultado == 1:
		string2 = "\n    sw $t0, resultado\n    lw $s0, resultado\n"
	else:
		string2 = "    li $s0, " + str(somador1) + "\n"
	string3 = "    li $t0, 0\n    jal isqrt\nisqrt:\n    mul $s1, $t0, 2\n    add $s1, $s1, 1\n    sub $s0, $s0, $s1\n    add $t0, $t0, 1\n    beq $s0, $zero, success\n    slt $s1, $s0, $zero\n    beq $s1, 1, error\n    j isqrt\nerror:\n    la $a0, error_raiz\n    la $v0, 4\n    syscall\n    la $v0, 10\n    syscall\nsuccess:\n"
	arquivo.writelines(string2)
	arquivo.writelines(string3) 
	resultado = math.sqrt(int(float(somador1)))
	resultado = RetiraPontosDecimais(resultado)
	return str(resultado)

def Finaliza(resultado):
	string = "\n\n#FINALIZACAO\n    sw $t0, resultado\n    lw $a0, resultado\n"
	string2 = "    li $v0, 1\n"
	string3 = "    syscall\n"
	arquivo.writelines(string) 
	arquivo.writelines(string2) 
	arquivo.writelines(string3) 
	print("resultado:" + str(resultado))

def RetiraPontosDecimais(numero):
  numeroNovo = str(numero).split('.')
  numero = numeroNovo[0]
  return numero

def VerificaDigito(digito, resultado, resultadoAnterior, ComResultado):
	if digito.isdigit():
		numeros.append(digito)
		global contadorPilha
		contadorPilha = contadorPilha + 1
	else:
		global x
		x = x + 1
		if digito == "+":
			if contadorPilha >= 2:
				contadorPilha = 0
				ComResultado = 0
				resultado = EscreveSoma(numeros[len(numeros)-2], numeros[len(numeros)-1], ComResultado)
				numeros.remove(numeros[len(numeros)-2])
				numeros.remove(numeros[len(numeros)-1])
			else:
				contadorPilha = 0
				if len(numeros) == 0:
					ComResultado = 2
					resultado = EscreveSoma(resultadoAnterior, resultado, ComResultado)
				else:
					ComResultado = 1
					resultado = EscreveSoma(resultado, numeros[len(numeros)-1], ComResultado)
					numeros.remove(numeros[len(numeros)-1])
		elif digito == "-":
			if contadorPilha >= 2:
				contadorPilha = 0
				ComResultado = 0
				resultado = EscreveSub(numeros[len(numeros)-2], numeros[len(numeros)-1], ComResultado)
				numeros.remove(numeros[len(numeros)-2])
				numeros.remove(numeros[len(numeros)-1])
			else:
				contadorPilha = 0
				if len(numeros) == 0:
					ComResultado = 2
					resultado = EscreveSub(resultadoAnterior, resultado, ComResultado)
				else:
					ComResultado = 1
					resultado = EscreveSub(resultado, numeros[len(numeros)-1], ComResultado)
					numeros.remove(numeros[len(numeros)-1])
		elif digito == "/":
			if contadorPilha >= 2:
				contadorPilha = 0
				ComResultado = 0
				resultado = EscreveDiv(numeros[len(numeros)-2], numeros[len(numeros)-1], ComResultado)
				numeros.remove(numeros[len(numeros)-2])
				numeros.remove(numeros[len(numeros)-1])
			else:
				contadorPilha = 0
				if len(numeros) == 0:
					ComResultado = 2
					resultado = EscreveDiv(resultadoAnterior, resultado, ComResultado)
				else:
					ComResultado = 1
					resultado = EscreveDiv(resultado, numeros[len(numeros)-1], ComResultado)
					numeros.remove(numeros[len(numeros)-1])
		elif digito == "*":
			if contadorPilha >= 2:
				contadorPilha = 0
				ComResultado = 0
				resultado = EscreveMulti(numeros[len(numeros)-2], numeros[len(numeros)-1], ComResultado)
				numeros.remove(numeros[len(numeros)-2])
				numeros.remove(numeros[len(numeros)-1])
			else:
				contadorPilha = 0
				if len(numeros) == 0:
					ComResultado = 2
					resultado = EscreveMulti(resultadoAnterior, resultado, ComResultado)
				else:
					ComResultado = 1
					resultado = EscreveMulti(resultado, numeros[len(numeros)-1], ComResultado)
					numeros.remove(numeros[len(numeros)-1])
		elif digito == "f":
			contadorPilha = 0
			if len(numeros) == 0:
				ComResultado = 1
				resultado = EscreveFator(resultado, ComResultado)
			else:
				ComResultado = 0
				resultado = EscreveFator(numeros[len(numeros)-1], ComResultado)
				numeros.remove(numeros[len(numeros)-1])
		elif digito == "p":
			contadorPilha = 0
			if len(numeros) == 0:
				resultado = "impossivel calcular, informe o valor da potencia!"
			else:
				resultado = EscrevePotencia(numeros[len(numeros)-1], resultado)
				numeros.remove(numeros[len(numeros)-1])
		elif digito == "s":
			contadorPilha = 0
			if len(numeros) == 0:
				ComResultado = 1
				resultado = EscreveRaiz(resultado, ComResultado)
			else:
				ComResultado = 0
				resultado = EscreveRaiz(numeros[len(numeros)-1], ComResultado)
				numeros.remove(numeros[len(numeros)-1])
	return resultado
	
numeros = []
resultado = [0]*(len(operacao)+3)
contadorPilha = 0
ComResultado = 0

x = 1
for i in range(len(operacao)):
	resultado[x] = VerificaDigito(operacao[i], resultado[x-1], resultado[x-2], ComResultado)
	if resultado[x] != resultado[x-1]:
		x = x + 1

Finaliza(resultado[x-1])

arquivo.close() 
