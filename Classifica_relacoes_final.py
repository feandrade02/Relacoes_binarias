def produto_cartesiano(conj): #Conjunto AxA
    resultado = []
    for i in conj: #Para cada elemento de A
        for j in conj: #Relaciona-se um elemento de A
            resultado += [[i,j]] #Concatena na lista de resultado
    return resultado

def partes_de_conj(p, n):
  r = []
  for aux in range(2**(len(p))):
    r.append([])
    for i in range (len(p)):
      if(aux & 2**i > 0): # Verifica se o bit tá ligado
        r[aux].append(p[i])# Caso acenda, append na relacao
        
    classe = classifica(aux,n) #Classifica cada relacao
    resultado = str(r[aux]) + classe + "\n" #Faz uma string do resultado da relacao e sua classificacao
    arq.write(resultado) #Escreve a relacao no arquivo
  return None

def par(i, j, rel, n):
    return 1<<i*n + j & rel == 1<<i*n + j #Verifica se o par em análise está na relacao

def classifica(rel, n): #Acrescenta classificacoes a string classe para cada relacao, conforme a análise
    classe = ""
    if(reflexiva(rel,n)):
        classe += "R"
    if(simetrica(rel, n)):
        classe += "S"
    if(transitiva(rel, n)):
        classe += "T"
    if(irreflexiva(rel, n)):
        classe += "I"
    if(antissimetrica(rel, n)):
        classe += "As"
    if "R" in classe and "S" in classe and "T" in classe:
        classe += "E"
    if(funcao(rel, n) and rel != 0) :
        classe += "Fu"
        if injetora(rel, n) and sobrejetora(rel, n):
            classe += "FbFiFs"
        elif injetora(rel, n):
            classe += "Fi"
        elif sobrejetora(rel, n):
            classe += "Fs"

    
    return classe

#Reflexiva: para todo x em A, xRx
def reflexiva(rel, n):
    for x in range(n):
        if not(par(x,x,rel,n)):
            return False
    return True

#Simetrica: para todo x e todo y em A, se xRy, entao yRx
def simetrica(rel, n):
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n) and not par(j, i, rel, n):
                return False
    return True

#Transitiva: para todo x, y e z em A, se xRy e yRz, entao xRz
def transitiva(rel, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if par(i, j, rel, n) and par(j, k, rel, n) and not par(i, k, rel, n):
                    return False
    return True

#Para todo x em A, o par (x,x) nao esta nas relacoes
def irreflexiva(rel, n):
    for i in range(n):
        if par(i, i, rel, n):
            return False
    return True

#Antissimetrica: para todo x e y em A, se xRy e yRx, entao x == y
def antissimetrica(rel, n):
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n) and par(j, i, rel, n) and not i == j:
                return False
    return True

#Funcao: todo x se relaciona com apenas um y 
def funcao(rel, n):
    aux = 0
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n):
                aux += 1
        if aux == 0 or  aux > 1:
            return False
        aux = 0
    return True

#Injetora: cada x se relaciona com um y distinto
def injetora(rel, n):
    aux = 0

    for i in range(n):
        for j in range(n):
            if par(j, i, rel, n) and aux < 1:
                aux += 1
            elif(par(j, i, rel, n)):
                return False
        aux = 0
    return True

#Sobrejetora: Contradominio == Imagem
def sobrejetora(rel , n):
    aux = False

    for i in range(n):
        for j in range(n):
            if par(j, i, rel, n):
                aux = True
                continue
        if not aux:
            return False
        aux = False

    return True

arq = open("relacoes_classificadas_4elem", "w")
import time
antes = time.time()
r = [1,2,3,4] #Conjunto de análise de tamanho n   
p = produto_cartesiano(r)
partes_de_conj(p,len(r))

arq.close()
depois = time.time()
print(depois - antes) #Tempo de execução
