import fractions

#Software developed by Franco Hernandez

print("Matriz inversa 3x3")
print("Software by Francote Dev")

def main():
    print("A B C")
    print("D E F")
    print("G H I")

    A = int(input("Valor de A : "))
    B = int(input("Valor de B : "))
    C = int(input("Valor de C : "))
    D = int(input("Valor de D : "))
    E = int(input("Valor de E : "))
    F = int(input("Valor de F : "))
    G = int(input("Valor de G : "))
    H = int(input("Valor de H : "))
    I = int(input("Valor de I : "))

    print(A,B,C)
    print(D,E,F)
    print(G,H,I)
    print("")

#Determinante
    Aux1 = A * E * I
    Aux2 = G * E * C
    Aux3 = Aux2 * -1
    Aux4 = Aux1 + Aux3
    Determinante = Aux4

    print("Determinante : ",Aux4)
    print("")

    Mini1A = E,F,
    Mini1B = H,I

    Mini2A = D,F,
    Mini2B = G,I

    Mini3A = D,E
    Mini3B = G,H

    Mini4A = B,C
    Mini4B = H,I

    Mini5A = A,C
    Mini5B = G,I

    Mini6A = A,B,
    Mini6B = G,H

    Mini7A = B,C
    Mini7B = E,F

    Mini8A = A,C
    Mini8B = D,F

    Mini9A = A,B
    Mini9B = D,E

    ResM1 = (E*I) - (H*F)
    ResM2 = (D*I) - (G*F)
    ResM3 = (D*H) - (G*E)
    ResM4 = (B*I) - (H*C)
    ResM5 = (A*I) - (G*C)
    ResM6 = (A*H) - (G*B)
    ResM7 = (B*F) - (E*C)
    ResM8 = (A*F) - (D*C)
    ResM9 = (A*E) - (D*B)

#Seccion de mini determinantes

    print("Mini1  : ", Mini1A)
    print("         ", Mini1B)
    print("-------------------")
    print("Mini2  : ", Mini2A)
    print("         ", Mini2B)
    print("-------------------")
    print("Mini3  : ", Mini3A)
    print("         ", Mini3B)
    print("-------------------")
    print("Mini4  : ", Mini4A)
    print("         ", Mini4B)
    print("-------------------")
    print("Mini5  : ", Mini5A)
    print("         ", Mini5B)
    print("-------------------")
    print("Mini6  : ", Mini6A)
    print("         ", Mini6B)
    print("-------------------")
    print("Mini7  : ", Mini7A)
    print("         ", Mini7B)
    print("-------------------")
    print("Mini8  : ", Mini8A)
    print("         ", Mini8B)
    print("-------------------")
    print("Mini9  : ", Mini9A)
    print("         ", Mini9B)

    print("Resultado de los Minis : ")
#Resultado con Minis
    print(ResM1,ResM2,ResM3)
    print(ResM4, ResM5, ResM6)
    print(ResM7, ResM8, ResM9)
    print("")

    print("Resultado Translacion : ")
#Translacion
    print(ResM1,ResM4,ResM7)
    print(ResM2,ResM5,ResM8)
    print(ResM3,ResM6,ResM9)
    print("")

    R1 = fractions.Fraction(ResM1, Determinante)
    R2 = fractions.Fraction(ResM4, Determinante)
    R3 = fractions.Fraction(ResM7, Determinante)
    R4 = fractions.Fraction(ResM2, Determinante)
    R5 = fractions.Fraction(ResM5, Determinante)
    R6 = fractions.Fraction(ResM8, Determinante)
    R7 = fractions.Fraction(ResM3, Determinante)
    R8 = fractions.Fraction(ResM6, Determinante)
    R9 = fractions.Fraction(ResM9, Determinante)

    print("Inversa : ")
    print(R1, -1*R2, R3)
    print(-1*R4,R5,-1*R6)
    print(R7,-1*R8,R9)

main()
