
print(f''' 
    Bem Vindo ao nosso Banco!
        O que deseja fazer hoje ?
        
        [d] - Depósito
        [s] - Saque
        [e] - extrato 
        [q] - Sair ''')



saldo = 0
saque = 0.0
limite = 500
LIMITES_SAQUES = 3
cont_saques = 0
extrato = ""

while True:

 opcao = input()

 if opcao == "q":
     break
 elif opcao == "d":
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
     saldo+=valor
     extrato += f"Deposito de: R${valor: .2f} \n"
     print("Deposito concluido com sucesso")
    else:
     print("Operação invalida", end="\n")
 elif opcao == "e":
    print("Não foram realizadas transações" if not extrato else extrato)
    print(" Seu extrato é:", end="\n")
    print(extrato)

 elif opcao == "s":

    saque = float(input("Informe o valor do seu saque"))

    if cont_saques == LIMITES_SAQUES :
       print("Saque não autorizado Limite excedido ", end="\n")
    elif saque>= limite:
        print("saque com valor não permitido ", end="\n")
    elif saque > saldo:
        print("Saque excedeu o saldo ", end="\n")
    else:
       print("Saque autorizado", end="\n")
       extrato+="Saque de R$:{saque: .2f}"
       cont_saques+=1
 else:
   print("Opção Inválida, tente de novo", end="\n")
