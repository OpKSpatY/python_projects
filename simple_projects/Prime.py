# Missão2:Gerar uma lista de números primos.
def CriaLista(self):
    list_num = list()
    cont = 0
    try:
        while True:
            if cont < numrange:
                cont += 1
                list_num.append(cont)
            else:
                notPrime(list_num)
                break
    except:
       return "Ocorreu um erro."

def notPrime(x):
    list_notprime = list()
    list_prime = list()
    prime = 0
    try:
        for value in x:
            prime = 0
            for c in range(1, len(x) + 1):
                if value % c == 0:
                    prime += 1
                    if prime > 2 and value not in list_notprime:
                        list_notprime.append(value)
        for v in x:
            if v not in list_notprime and v != 1 and v != 0:
                list_prime.append(v)

        print("A lista dos valores não primos são:")
        for v in list_notprime:
             print(v,end=" ")
        print("\nA lista dos valores primos é:")
        for v in list_prime:
            print(v,end=" ")
    except:
        return "Ocorreu um erro.."
numrange = 0
while numrange == 0:
    numrange = int(input("Oi! Digite um número até onde deseja contar: "))

CriaLista(numrange)


