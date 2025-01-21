palavraSecreta = "python"
letrasAcertadas = ""
tentativas = 0

while True:
    letraDigitada = input("Digite uma letra: ")
    tentativas += 1

    if len(letraDigitada) > 1:
        print("Digite apenas uma letra!")
        continue

    if letraDigitada in palavraSecreta:
        letrasAcertadas += letraDigitada

    palavraFormada = ""
    for letraSecreta in palavraSecreta:
        if letraSecreta in letrasAcertadas:
            palavraFormada += letraSecreta
        else:
            palavraFormada += "*"
        
    print(palavraFormada)

    if palavraFormada == palavraSecreta:
        print("Você venceu!")
        print(f"Número de tentativas: {tentativas}")
