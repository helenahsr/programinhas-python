a = input("Escreva um numero: ")

if int(a) == 0:
    print("É zero")
else:
    for i in range(2, int(a)):  
        
        if int(a) % i == 0:
            print("Numero não primo")
            break
    else:
        print("primo")