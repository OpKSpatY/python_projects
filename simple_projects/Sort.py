# Missão 4: Implementar o Algoritmo de Ordenação "Selection sort".


class Sort:
    def CreateList():
        listnum = []
        listnum2 = []
        listnum.clear()
        listnum2.clear()
        y = " "
        x = float(input("Oi! Digite aqui um valor para ser adicionado a sua lista: "))
        listnum.append(x)
        while True:
            while y not in "YyNn":
                y = str(input("Deseja adicionar mais algum número? Y/N "))
            if y in "Yy":
                x = float(input("Oi! Digite aqui um valor para ser adicionado a sua lista: "))
                listnum.append(x)
                y = " "
            if y in "Nn":
                break
        listnum2 = sorted(listnum)
        Sort.Organize(listnum,listnum2)



    def Organize(x,y):
        print(f"A lista de números fornecidos foi:",end="\033[32m ")
        for num in x:
            print(num,end=" ")
        print("\n\033[mAo organiza-los, a lista agora ficou como: ",end="\033[33m")

        for num in y:
            print(f"{num}", end=" ")

        cont = " "
        while cont not in "YyNn":
            cont = str(input("\n\033[mDeseja escrever outra lista? Y/N"))
        if cont in "Yy":
            Sort.CreateList()
        else:
            exit()

if __name__ == "__main__":
	Sort.CreateList()
