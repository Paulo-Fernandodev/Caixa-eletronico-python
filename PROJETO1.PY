#Jogo de adivinhação
#Nesse jogo o usuário precisa acertar o número secreto.
#Pode tentar até acertar.

numero_secreto = 5
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Entre 1 e 10, qual é o número secreto? "))


    if tentativa < numero_secreto:
        print ("O número secreto é maior!")
    elif tentativa > numero_secreto:
        print ("O número secreto é menor!")
    else: 
        print ("Parabéns, você acertou o número secreto!") 