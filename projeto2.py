# Simulador de caixa eletronico

# O usuário tem um saldo inicial de $500
# E pode sacar o quanto quiser desse valor, e quanto vezes quiser até acabar o saldo.


saldo = 500


while saldo > 0:
    saque = float(input("Quanto você quer sacar? (ou digite 0 para sair): "))

    if saque == 0:
        break

    if saque > saldo:
        print ("Saldo insuficiente, esse saque não foi efetuado.")

    else:
        saldo -= saque
        print (f"Saque realizado com sucesso, seu saldo agora é de: R${saldo}")

print ("Operação finalizada!")