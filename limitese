from math import sqrt

print("Limite de número e")

def main():
    print("e = (1[a] + 1[b] / n[c])^n[d]")
    a = int(input("Introduce valor de A : "))
    b = int(input("Introduce valor de B : "))
    c = int(input("Introduce valor de C : "))
    d = int(input("Introduce valor de D : "))
    e = int
    p1 = float
    p2 = float

    print("1 - (1[a] + 1[b] / n[c])^n[d]")
    print("2 - (1[a] + 1[b] / n[c])^x.n[d]")
    print("3 - [( polinomio_a ) / polinomio_b ]^n[d]")
    print("4 - (1[a] + 1[b] / n[c])^n + c[d]")

    e_type = int(input("Determina la morfología de operación : "))

    if e_type == 1:
        e = b
        print("e = e^", e)

    elif e_type == 2:
        aux1 = b*d
        e = aux1
        print("e = e^", e)

    elif e_type == 3:
     an = int(input("Introduce grado del polinomio : "))
     if an >= 2:
            a1 = float(input("Introduce valor de A_1 : "))
            b1 = float(input("Introduce valor de B_1 : "))
            c1 = float(input("Introduce valor de C_1 : "))
            a2 = float(input("Introduce valor de A_2 : "))
            b2 = float(input("Introduce valor de B_2 : "))
            c2 = float(input("Introduce valor de C_2 : "))

#Sumatoria en resolvente de polinomio 1
            auxa0 = 2*a1
            auxa1 = b1 * -1
            auxa2 = b1 * b1
            auxa3 = auxa2 - 4 * a1 * c1
            print(auxa3)
            auxa4 = sqrt(auxa3)
            print(auxa4)
            auxa5 = (auxa1 + auxa4)
            print(auxa5)
            auxa6 = auxa5/auxa0
            print(auxa6)
            pol1_suma = auxa6
            print("Resolvente del primer polinomio en sumatoria : ",pol1_suma)

#Resta en resolvente de polinomio 1
            auxa0a = 2*a1
            auxa1a = b1 * -1
            auxa2a = b1 * b1
            auxa3a = auxa2a - 4 * a1 * c1
            auxa4a = sqrt(auxa3a)
            auxa5a = (auxa1a - auxa4a)
            auxa6a = auxa5a/auxa0a
            pol1_resta = auxa6a
            print("Resolvente del primer polinomio en resta : ", pol1_resta)

#Sumatoria en resolevnte en polimonio 2
     auxb0 = 2*a2
     auxb1 = b2 * -1
     auxb2 = b2 * b2
     auxb3 = auxb2 - 4 * a2 * c2
     auxb4 = sqrt(auxb3)
     auxb5 = (auxb1 + auxb4)
     auxb6 = auxb5/auxb0
     pol2_suma = auxb6
     print("Resolvente del segundo polinomio en sumatoria : ", pol2_suma)

     # Sumatoria en resolevnte e polimonio 2
     auxb0b = 2*a2
     auxb1b = b2 * -1
     auxb2b = b2 * b2
     auxb3b = auxb2b - 4 * a2 * c2
     auxb4b = sqrt(auxb3b)
     auxb5b = (auxb1b - auxb4b)
     auxb6b = auxb5b/auxb0b
     pol2_resta = auxb6b
     print("Resolvente del segundo polinomio en resta : ", pol2_resta)

    #Multiplicacion de polinomios
    r1 = pol1_resta - pol2_resta
    r2 = r1 * d
    if r2 < 0:
        r3 = r2 * -1
    else:
        r3 = r2 * 1
    print("e ^", r3)
    
    #Eleccion 4 a desarrollar !!

main()
