# Missão 3: Implementar um algoritmo para mover um robô do canto superior esquerdo para o canto inferior direito de uma grade
def Grade(x):
    grade = ["""0 - 0 - 0
0 - 0 - 0
0 - 0 - 0
        """,
        """0 - 0 - 0
0 - 0 - 0
0 - 0 - F""",
        """0 - 0 - 0
0 - 0 - 0
0 - F - 0
        """,
        """0 - 0 - 0
0 - 0 - 0
F - 0 - 0
        """,
        """0 - 0 - 0
0 - 0 - F
0 - 0 - 0
        """,
        """0 - 0 - 0
0 - F - 0
0 - 0 - 0
        """,
        """0 - 0 - 0
F - 0 - 0
0 - 0 - 0
        """,
        """F - 0 - 0
0 - 0 - 0
0 - 0 - 0
        """,
        """0 - F - 0
0 - 0 - 0
0 - 0 - 0
        """,
        """0 - 0 - F
0 - 0 - 0
0 - 0 - 0
        """

    ]
    print(grade[x])

def main():
    a = "Controlador de foguetes"
    print("-=-" * 20)
    print(f"{a:^50}")
    print("-=-" * 20)
    Grade(0)
    while True:
        while True:
            v = int(input("Oi! Deseja que seu foguete vá para qual posição?\nConsidere seu teclado NUMPAD como as posições do foguete!"))
            if v >= 0  and v <= 9:
                break
        Grade(v)
        keep = str(input("Deseja continuar? Y/N"))
        if keep in "Yy":
            continue
        if keep in "Nn":
            print("Foi ótimo jogar com você!")
            break

if __name__ == "__main__":
	main()