import fractions
#Software by francote

print("Triangulacion de matrices 3x3")

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
    print("")

    AuxDA = fractions.Fraction(D,A)
    AuxDA2 = (AuxDA*A)
    AuxDA3 = D - AuxDA2
    AuxEB = (AuxDA*B)
    AuxEB2 = E - AuxEB
    AuxFC = (AuxDA*C)
    AuxFC2 = F - AuxFC
    AuxGD = fractions.Fraction(G,D)
    AuxGD2 = (AuxGD*D)
    AuxGD3 = G - AuxGD2
    AuxHE = (AuxGD*E)
    AuxHE2 = H - AuxHE
    AuxIF = (AuxGD*F)
    AuxIF2 = F - AuxIF
    print("")
    print(A,B,C)
    print(AuxDA3,AuxEB2,AuxFC2)
    print(AuxGD3,AuxHE2,AuxIF2)

    if AuxHE2 >= 0:
        AxHE = fractions.Fraction(AuxHE2,AuxEB2)
        AxHE2 = AxHE *AuxEB2
        AxHE3 = AuxHE2 - AxHE2
        AxIF = AxHE * AuxIF2
        AxIF2 = AuxIF2 - AxIF
        print("")
        print(A, B, C)
        print(AuxDA3, AuxEB2, AuxFC2)
        print(AuxGD3, AxHE3, AxIF2)
