import os #importando esta biblioteca. Não precisei baixar nada, apenas puxei

os.system('cls') #aqui eu estou puxando um recurso desta biblioteca "os".
print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""") 
#aqui eu copiei e colei esse texto no site fsimbols q tem formatações legais para textos em terminais
print('1. Cadastrar restaurante')
print('2. Listar restaurantes.')
print('3. Ativar restaurante.')
print('4. Sair.\n')

opcao_escolhida = int(input('Escolha uma opção: '))
# opcao_escolhida = int(opcao_escolhida)
print(f'Você escolheu a opção {opcao_escolhida}.')

def finalizar_app():  #aqui estou definindo uma funçaõ. o "def" é como escrever "function" no javascript
    os.system('cls') #aqui eu estou puxando um recurso desta biblioteca "os".
    print('Encerrando o programa...\n')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    finalizar_app()