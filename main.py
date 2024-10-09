# Construção do menu

menu = """

======= MENU ======

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

===================
Digite a opcão desejada:
"""

# Váriaveis

saldo = 0
LIMITE= 500
numero_saque = 0
extrato = ''

# Estrutura de repetição While True:

while True:
  opcao = input(menu)


# if/elif/else para as estruturas condicionáis 

  
# Opção 1 Depósito 
  
  if opcao == '1':
    deposito = float(input('Digite o valor desejado:'))
    if deposito > 0:
      saldo += deposito
      print(f'Seu novo saldo é R${saldo}.')
      extrato += f"Depósito: R$ {deposito:.2f}\n"
    
    else:
      print('Operação inválida, digite outro valor.')



  # Opção 2 Saque

  if opcao == '2':
    if numero_saque == 3:
      print('Limte de saques diário excedido, tente novamente amanhã.')

    elif saldo <= 0:
      print(f'Saldo insuficiente, seu saldo é R${saldo}.')

  
    elif saldo > 0:
      saque = float(input('Digite o valor do saque:'))

      if saque > 500:
         print(f'Seu limite por saque é {LIMITE},selecione outro valor.')

      elif saque <= 0:
        print('Operação não realizada, selecione um valor válido.')

      else:
        saldo -= saque
        numero_saque += 1
        extrato += f"Saque: R$ {saque:.2f}\n"
        print(f'Você sacou R${saque},e seu novo saldo é R${saldo}.')

    


# Opção 3 Extrato
  
  elif opcao == '3':
    print("\n============EXTRATO==========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\n Saldo: R${saldo:.2f}")
    print('=============================')


# Opção com break para quebrar a estrutura de repetição 
  if opcao == '4':
    break